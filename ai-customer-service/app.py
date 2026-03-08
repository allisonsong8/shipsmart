from flask import Flask, request, jsonify, send_from_directory
from groq import Groq

app = Flask(__name__)

client = Groq(api_key="your_groq_api_key_here")

owner_settings = {
    "business_name": "My Shop",
    "common_issues": []
}

def build_system_prompt():
    base = f"""You are a friendly customer service assistant for a small business called "{owner_settings['business_name']}". 
You help customers with shipping questions, package tracking, tariff/import costs, and delivery issues.
Keep responses SHORT and conversational — 2-3 sentences max. Be warm and direct.
If a customer sends a photo of a product, acknowledge it warmly and ask what they'd like to know about shipping or customization.
If you don't know a tracking number's status, briefly explain and tell them what to do next."""

    if owner_settings["common_issues"]:
        issues = "\n".join(f"- {issue}" for issue in owner_settings["common_issues"])
        base += f"""

The store owner flagged these common issues — be especially helpful about them:
{issues}"""

    return base

@app.route("/")
def index():
    return send_from_directory(".", "index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "")
    image_url = data.get("image_url")  # Cloudinary URL if customer attached a photo

    # Build message content — include image context if provided
    if image_url:
        content = f"{user_message}\n\n[Customer attached a product photo: {image_url}]"
    else:
        content = user_message

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": build_system_prompt()},
                {"role": "user", "content": content}
            ],
            max_tokens=150
        )
        return jsonify({"reply": response.choices[0].message.content})
    except Exception as e:
        print("Error:", e)
        return jsonify({"reply": f"Sorry, something went wrong: {str(e)}"}), 500

@app.route("/settings", methods=["GET"])
def get_settings():
    return jsonify(owner_settings)

@app.route("/settings", methods=["POST"])
def update_settings():
    data = request.json
    if "business_name" in data:
        owner_settings["business_name"] = data["business_name"]
    if "common_issues" in data:
        owner_settings["common_issues"] = data["common_issues"]
    return jsonify({"status": "ok", "settings": owner_settings})

if __name__ == "__main__":
    app.run(debug=True)
