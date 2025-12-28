# 🇺🇸 English version
[![lang ru](https://img.shields.io/badge/lang-ru-blue)](https://github.com/EmilioAugust/Text-Data-Masker/blob/main/README.ru.md)
[![lang en](https://img.shields.io/badge/lang-en-red)](https://github.com/EmilioAugust/Text-Data-Masker)

## 📰 Text Data Masker

Text Data Masker is a utility that scans text and hides sensitive information such as email addresses, phone numbers, and URLs.
Detected data is replaced with predefined placeholders to help protect privacy and prevent accidental data leaks.

---

## 🚀 Features
- Detects and masks **email addresses**
- Detects and masks **phone numbers**
- Detects and masks **URLs**
- Can be used for data anonymization

---

## 📦 Example Response
```bash
[
  {
    "original": "Original text"
    "anonymized": "Anonymized text"
    "entities_found": "EMAIL, PHONE, URL"
  }
]
```

---

## 🔧 Installation (local)

**1. Clone the repository**
```bash
git clone https://github.com/EmilioAugust/Text-Data-Masker.git
cd Text-Data-Masker
```
**2. Install dependencies**
```bash
pip install -r requirements.txt
```
**3. Run the server**
```bash
uvicorn main:app --reload
```
Open:
```bash
http://localhost:8000/docs
```

---

## 🐳 Docker Usage (recommended)

**1. Build the image**
```bash
docker compose up --build
```
**2. Open in browser**
```bash
http://localhost:8000/docs
```

---

## 📚 API Endpoints
```POST /anonymize```

Example:
```bash
/anonymize?query=phone
```

## 🛠️ Tech Stack

- Python 3.10+
- [FastAPI](https://fastapi.tiangolo.com/)
- Asyncio
- [Docker](https://www.docker.com/)

---

## 🤝 Contributing

PRs are welcome!
Feel free to add new sources or improve code structure.

---

## 📄 License

MIT — free for all use.
