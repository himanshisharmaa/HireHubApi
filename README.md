# HireHub API 

HireHub API is a RESTful web service built using Django and Django REST Framework.  
It allows users to register, login, and perform CRUD operations on Job Listings, with full authentication, permissions, pagination, filtering, and professional API documentation.

---

##  Features

- User Authentication using JWT (SimpleJWT)
- CRUD APIs for Jobs (Create, Read, Update, Delete)
- Owner-based Permissions (Only the owner can edit/delete their job posts)
- Pagination for job listings (5 jobs per page)
- Filtering by Location and Company Name
- Searching by Title, Description, and Company Name
- Auto-generated API Documentation (Redoc / Swagger)
- Admin Panel for easy data management

---

##  Technologies Used

- Python 3
- Django
- Django REST Framework (DRF)
- SimpleJWT (Authentication)
- PostgreSQL (or SQLite for development)
- drf-yasg (for API Documentation)

---

##  Getting Started (Local Setup)

Follow these steps to run the project locally:

### 1. Clone the repository


              git clone https://github.com/<your-github-username>/hirehub-api.git
              cd hirehub-api

            
### 2. Create a Virtual Environment
              python -m venv env
              
#### Activate it:
  - Windows:
    
              .\env\Scripts\activate
    
  - Linux/Mac:
      
              source env/bin/activate

### 3. Install Dependencies

              pip install -r requirements.txt

 ### 4. Apply Migrations

              python manage.py makemigrations
              python manage.py migrate
 

 ### 5. Create a Superuser
              python manage.py createsuperuser

### 6. Run the server

              python manage.py runserver
