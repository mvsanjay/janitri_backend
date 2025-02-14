# Janitri Backend API (Flask)

This is a backend API for monitoring patient heart rate data. The project is built using Flask and MySQL.

## Features
✅ User Registration & Login  
✅ Patient Management  
✅ Heart Rate Recording & Retrieval  
✅ Database using MySQL  
✅ RESTful API with Flask  

## Installation & Setup
1. Clone this repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/janitri-backend.git
   cd janitri-backend
   
2. Set up a virtual environment:
   ```bash
    python -m venv venv
    source venv/bin/activate  # Windows: venv\Scripts\activate
   
3. Install dependencies:
   ```bash
    pip install -r requirements.txt
   
4. Set up the database:
   - Install MySQL.
   - Create a database named janitri.
   - Update .env file with your MySQL credentials.
   
5. Run the migrations:
   ```bash
    flask db upgrade
   
6. Start the server:
   ```bash
    flask run

## API Documentation
- **User Registration**: `POST /register`
- **User Login**: `POST /login`
- **Add Patient**: `POST /patients`
- **Get Patient Details**: `GET /patients/<patient_id>`
- **Record Heart Rate**: `POST /heart-rate`
- **Get Heart Rate Data**: `GET /heart-rate/<patient_id>`

## Assumptions
  - Authentication is not required as per the assignment.
  - Users are uniquely identified by their email.
