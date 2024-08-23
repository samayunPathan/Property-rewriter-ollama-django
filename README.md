# Django CLI Application for Rewriting Property Information Using Ollama

## Project Overview

This project is a Django CLI application that interacts with a PostgreSQL database to rewrite property titles and descriptions using the Ollama model gemma2:2b. Additionally, the project generates and stores summaries of the property information into a separate table in the same database.

## Features

- Data Retrieval: Fetches property data (title, description, location, amenities) from an external PostgreSQL database.
- Title and Description Rewrite: Utilizes the Ollama model gemma2:2b to generate improved titles and descriptions for each property.
- Summary Generation: Creates a summary of the property information using the Ollama model and stores it in a new summary table.
- Database Interaction: All data is handled using Django ORM, ensuring smooth interaction with the PostgreSQL database.

## Prerequisites
Before running the project, make sure you have the following installed:

- Python 3.8+
- PostgreSQL
- Django 
- Ollama (with access to the gemma2:2b model)



### 2. Clone the Repository

```bash
git clone https://github.com/samayunPathan/Property-rewriter-ollama-django.git
```
Go to project directory
``` bash
cd Property-rewriter-ollama-django
```
### 3. Create a Virtual Environment
```bash
python3 -m venv venv # On Windows use `python -m venv venv`
```
Active virtual environment
```bash
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 4. Install Dependencies
``` bash 
pip install -r requirements.txt
```
### 5. Configure PostgreSQL

> [!NOTE]
> Create postgresql database.
> Create `.pg_service.conf` file in your ** home directory with the following content:

```bash
[django_model_db]
host=localhost
port=5432
dbname=scrapy_db
user=your_db_user
password=your_db_password
```
- Update the Django settings.py to use the service name:
``` bash 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'OPTIONS': {
            'service': 'scrapy_db',
        },
    }
}
```

### 6. Apply Migrations
``` bash
python manage.py makemigrations
python manage.py migrate
```
### 7. Create a Superuser
```bash
python manage.py createsuperuser
```
### 8. Run the Development Server
```bash 
python manage.py runserver
```
Access the Django admin panel at http://127.0.0.1:8000/admin/ and log in with your superuser credentials.

### 9. Migrate Data from Scrapy
```bash
python manage.py rewriter
```

## Usage
This command will execute the entire process, including fetching data, rewriting titles and descriptions, and generating summaries.
