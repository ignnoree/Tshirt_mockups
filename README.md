
# T-shirt Mockups Generator

A simple **Django + Celery project** to generate custom T-shirt mockups with text overlays.

---

## Features
- Generate T-shirt mockups in different colors.
- Asynchronous processing using Celery.
- Stores generated mockups in the database.
- REST API endpoints for task management and listing mockups.

---

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/ignnoree/Tshirt_mockups.git
cd Tshirt_mockups
````

### 2. Create and activate a virtual environment

**Windows:**

```bash
python -m venv .venv
.venv\Scripts\activate
```

**Linux / macOS:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run migrations

```bash
python manage.py migrate
```

### 5. Start Django server

```bash
python manage.py runserver
```

### 6. Start Celery worker

```bash
celery -A project worker -l info
```

---

## API Endpoints

* **POST** `/api/tasks/start/` – Start a new mockup generation task.
* **GET** `/api/tasks/status/<task_id>/` – Check task status and results.
* **GET** `/api/mockups/` – List all generated mockups with pagination.

---

## Notes

* Generated images are stored in `media/mockups/`.
* Example URL format: `http://127.0.0.1:8000/media/mockups/blue_Hello_World.png`.


