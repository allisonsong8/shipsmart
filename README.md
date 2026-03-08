# ShipSmart 

An AI-powered customer support chatbot built for small business owners struggling with shipping delays, tariff questions, and package tracking.

Built with Flask, Groq (LLaMA 3.3 70B), and Cloudinary.

---

## Features

- 💬 AI chatbot that answers shipping, tariff, and tracking questions in real time
- 📷 Customers can upload product photos directly in the chat
- 🎨 Bead color preview — see how a charm looks in different colors
- 📦 Packaging preview — see how a product looks in the actual packaging
- ⚙️ Owner settings — customize the business name and common issues

---

## Requirements

- Python 3.8+
- A [Groq](https://groq.com) API key
- A [Cloudinary](https://cloudinary.com) account

---

## Setup

**1. Install dependencies**

```bash
pip install flask groq
```

**2. Add your Groq API key**

In `app.py`, replace the API key with your own:

```python
client = Groq(api_key="your_groq_api_key_here")
```

**3. Run the app**

```bash
python app.py
```

**4. Open in your browser**

```
http://localhost:5000
```

---

## Built With

- [Flask](https://flask.palletsprojects.com/) — Python web framework
- [Groq API](https://groq.com) — Fast LLaMA 3.3 70B inference
- [Cloudinary](https://cloudinary.com) — Image upload, background removal, and transformations

---


