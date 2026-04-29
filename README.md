# Stock Management System (Desafio Kenner)

A robust backend solution for inventory control, focusing on performance and scalability. This project was developed to solve real-world stock logic challenges using the Django framework.

## 🚀 Technologies Used
* [cite_start]**Backend:** Python 3.12+ and Django Framework 
* [cite_start]**Database:** MySQL (Relational modeling and CRUD operations) 
* [cite_start]**Environment:** Python Decouple (for .env management) and Git for version control 

## 🛠️ Key Features
* **Full CRUD:** Create, Read, Update, and Delete products and categories.
* [cite_start]**OOP Architecture:** Extensive use of Django Models inheritance and Meta classes for clean code.
* **Database Migrations:** Structured schema evolution via Django Migrations.

## ⚙️ How to Run
1. **Clone the repository:**
   `git clone https://github.com/joaopedrolouzada/desafio-kenner-estoque.git`
2. **Create and activate a virtual environment:**
   `python -m venv venv` 
   `source venv/bin/activate` (Linux/Mac) or `venv\Scripts\activate` (Windows)
3. **Install dependencies:**
   `pip install -r requirements.txt`
4. **Configure your .env:**
   Create a `.env` file and add your `SECRET_KEY` and database credentials.
5. **Run migrations and start server:**
   `python manage.py migrate`
   `python manage.py runserver`
