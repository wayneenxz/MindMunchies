# Setting Up MindMunchies Flask Project

This guide will help you set up the MindMunchies Flask project environment and run it locally.

## Prerequisites

Before you begin, ensure you have the following installed on your system:
- Python (3.7 or higher recommended, 3.10.14 recommended)
- Pip (Python package installer)

## Installation Steps

### 1. Clone the Repository

Clone the MindMunchies repository from GitHub:
```bash
git clone <repository-url>
cd MindMunchies
```
### 2. Create and Activate Virtual Environment (venv)
Navigate into the project directory and create a virtual environment called venv:
```bash
cd MindMunchies
python -m venv venv
```

Activate the virtual environment:

Windows (PowerShell):
```bash
.\venv\Scripts\Activate.ps1
```

### 3. Install Required Python Packages
Install the required packages using pip:
```bash
pip install -r requirements.txt
```

### 4. Set Up Database (if applicable)
```bash
flask db init
flask db migrate -m "Initial database migration"
flask db upgrade
```
### 5. Run the Flask Application
Run the Flask application:
```bash
flask run
```