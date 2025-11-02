ChatGPT said:

Here’s a short, practical README you can use for your Tshirt Mockups project:

# Tshirt Mockups

A simple Django + Celery project to generate custom T-shirt mockups with text overlays.

## Features
- Generate T-shirt mockups in different colors.
- Asynchronous processing using Celery.
- Stores generated mockups in the database.
- REST API endpoints for task management and listing mockups.

## Installation
1. Clone the repository:  
   ```bash
   git clone https://github.com/ignnoree/Tshirt_mockups.git
   cd Tshirt_mockups


Create and activate a virtual environment:

python -m venv .venv
source .venv/Scripts/activate  # Windows


Install dependencies:

pip install -r requirements.txt


Run migrations:

python manage.py migrate


Start Django server:

python manage.py runserver


Start Celery worker:

celery -A project worker -l info

API Endpoints

POST /api/tasks/start/ – Start a new mockup generation task.

GET /api/tasks/status/<task_id>/ – Check task status and results.

GET /api/mockups/ – List all generated mockups with pagination.

Notes

Generated images are stored in media/mockups/.

Example URL format: http://127.0.0.1:8000/media/mockups/blue_Hello_World.png.
