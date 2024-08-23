# Django CLI Application for Rewriting Property Information Using Ollama

## Table of Contents

1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Prerequisites](#prerequisites)
4. [Installation](#installation)
   - [Clone the Repository](#clone-the-repository)
   - [Set Up Virtual Environment](#set-up-virtual-environment)
   - [Install Dependencies](#install-dependencies)
5. [Configuration](#configuration)
   - [Configure PostgreSQL](#configure-postgresql)
6. [Database Setup](#database-setup)
   - [Apply Migrations](#apply-migrations)
   - [Create Superuser](#create-superuser)
7. [Running the Application](#running-the-application)
   - [Start Development Server](#start-development-server)
   - [Execute CLI Application](#execute-cli-application)
8. [Usage](#usage)
9. [Contributing](#contributing)
10. [License](#license)

## Project Overview

This Django CLI application interacts with a PostgreSQL database to rewrite property titles and descriptions using the Ollama model `gemma2:2b`. It also generates and stores summaries of property information in a separate table within the same database.

## Features

- **Data Retrieval:** Fetches property data (title, description, location, amenities) from an external PostgreSQL database.
- **Title and Description Rewrite:** Utilizes the Ollama model `gemma2:2b` to generate improved titles and descriptions for each property.
- **Summary Generation:** Creates a summary of the property information using the Ollama model and stores it in a new summary table.
- **Database Interaction:** All data is handled using Django ORM, ensuring smooth interaction with the PostgreSQL database.

## Prerequisites

Ensure you have the following installed:

- Python 3.8+
- PostgreSQL
- Django
- Ollama (with access to the `gemma2:2b` model)

## Installation

### Clone the Repository

```bash
git clone https://github.com/samayunPathan/Property-rewriter-ollama-django.git
```
#### Go to directory 
```bash
cd Property-rewriter-ollama-django
```

### Set Up Virtual Environment
```bash
python3 -m venv venv
```
### Active virtual environment
```bash
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
### Install Dependencies
```bash
pip install -r requirements.txt
```
## Configuration
### Configure PostgreSQL

> [!NOTE]
> Create `.env` file in your project directory with the following ,to clear understand this repo has `.env.sample` file
``` bash
host=localhost
port=port number
user=your_user_name
dbname=your_db_name
password=your_db_password
```

## Database Setup
### Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```
### Create Superuser
```bash
python manage.py createsuperuser
```
## Running the Application
### Start Development Server
```bash
python manage.py runserver
```
Access the Django admin panel at http://127.0.0.1:8000/admin/ and log in with your superuser credentials.

### Execute CLI Application


```bash
python manage.py rewriter
```
## Usage
The rewriter command executes the entire process, including fetching data, rewriting titles and descriptions, and generating summaries.

## Contributing
Contributions to this project are welcome. Please fork the repository and submit a pull request with your changes.

## License
[Specify your license here, e.g., MIT, GPL, etc.]

This outline provides the structure for the `README.md` file. You can fill in additional details specific to your project as needed.
