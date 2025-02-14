# Janitri Backend Assignment

## Setup
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Run migrations: `flask db init && flask db migrate && flask db upgrade`
4. Start the server: `flask run`

## API Documentation
- **User Registration**: `POST /register`
- **User Login**: `POST /login`
- **Add Patient**: `POST /patients`
- **Get Patient Details**: `GET /patients/<patient_id>`
- **Record Heart Rate**: `POST /heart-rate`
- **Get Heart Rate Data**: `GET /heart-rate/<patient_id>`