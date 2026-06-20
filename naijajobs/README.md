# naijajobs

> *“NaijaJobs is a job listing website where Nigerian companies can post vacancies and job seekers can browse opportunities.”*  
> *“The spec below defines the visual language of the application.”*

## Project description
**NaijaJobs** is a Django-based job listing platform focused on the Nigerian market. Employers can register, post and manage job listings; job seekers can browse, search, filter, and view job details. The UI follows a warm, professional visual language (Forest Green primary, Nigerian Gold accent) with **Playfair Display** for headings and **DM Sans** for body/UI.

## Key features
- **Browse, search, and filter** job listings (server-side search using Django `Q` objects).  
- **Employer authentication & dashboard**: register, login, post, edit, delete listings.  
- **Admin moderation**: admin can moderate and deactivate listings.  
- **Responsive, accessible UI**: mobile-first breakpoints at **480px**, **768px**, and **1024px**; dark mode persisted in `localStorage`.  
- **Seeded sample data**: management command to populate ~20 realistic jobs.

## Tech stack
- **Framework:** Django `6.0.6`  
- **Frontend:** HTML, CSS (Grid & Flexbox), vanilla JS for small interactions (dark mode, client validation)  
- **Database:** SQLite (development) — swap to Postgres or other DB in production  
- **Auth:** Django built-in authentication  
- **Repository name:** `naijajobs`

## Setup instructions

### 1. Clone repository
```bash
git clone https://github.com/SOCRATES011/naijajobs.git
cd naijajobs

### 2.Create and activate a virtual environment
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate

### 3. Install Dependencies
```bash 
pip install Django==6.0.6
pip install pillow==12.2.0

### 4. Configure environment (recommended)
Create a .venv or set environment variables for production. Do not commit secrets.

Example .venv (development only):
SECRET_KEY=replace-with-your-secret
DEBUG=True

### 5. Database migrations and superuser
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

### 6. Seed sample data (optional) 
#### This creates a sample employer account (username: employer, password set in the seed command) and ~20 job listings.
```bash
python manage.py seed_jobs

### 7. Run the development server
```bash
python manage.py runserver
# Open http://127.0.0.1:8000/
# Admin: http://127.0.0.1:8000/admin/


Useful commands
Run tests (if any): python manage.py test

Collect static files (production): python manage.py collectstatic

Create migrations after model changes: python manage.py makemigrations then python manage.py migrate

Deploying / Publishing to GitHub
1. Add a .gitignore (exclude venv/, db.sqlite3, .env, staticfiles/, etc.).

2. Initialize git and push:
```bash
git init
git add .
git commit -m "Initial commit — NaijaJobs"
git branch -M main
git remote add origin https://github.com/SOCRATES011/naijajobs.git
git push -u origin main


Demo presentation video:
