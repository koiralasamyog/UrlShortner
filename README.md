# URL Shortener

A **simple, fast, and reliable URL shortener** built with **Django**.  
Features include:  
- User authentication (register, login, logout)  
- Generate short URLs with **Base62 encoding**  
- Optional **custom short URLs**  
- URL expiration dates  
- Click tracking / analytics  
- **Edit and delete URLs**  
- **QR code generation** for easy sharing  
- Responsive and clean UI with **Bootstrap**

## **Tech Stack**

**Backend: Django**

**Frontend: HTML, Bootstrap 4**

**Database: SQLite (default)**

**QR Codes: qrcode and Pillow**

## **Features**

1. **User Authentication**  
   - Only registered users can create and manage URLs.  

2. **URL Shortening**  
   - Automatic Base62 short key generation.  
   - Option to customize short URLs.  
   - Set expiration dates.  

3. **URL Management**  
   - List all your created URLs.  
   - Edit original URL, custom short URL, and expiration.  
   - Delete URLs.  

4. **Analytics & QR Codes**  
   - Track number of clicks.  
   - QR code for each short URL.  

---

## **Installation**

1. **Clone the repository:**

```bash
git clone https://github.com/koiralasamyog/UrlShortener.git
cd UrlShortener
```

2. **Create and activate a virtual environment:**

```bash
python -m venv venv
source venv/bin/activate  # Linux / macOS
venv\Scripts\activate     # Windows
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

4. **Apply database migrations**

```bash
python manage.py migrate
```

5. **Create a superuser (optional for admin)**

```bash
python manage.py createsuperuser
```

6. **Run the development server**

```bash
python manage.py runserver
```
Open http://127.0.0.1:8000 in your browser.
