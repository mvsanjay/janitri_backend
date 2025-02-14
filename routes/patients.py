from flask import Blueprint, request, jsonify
from models import Patient, db

patients_bp = Blueprint('patients', __name__)

@patients_bp.route('/patients', methods=['POST'])
def add_patient():
    data = request.get_json()
    new_patient = Patient(user_id=data['user_id'], name=data['name'], age=data['age'], gender=data['gender'])
    db.session.add(new_patient)
    db.session.commit()
    return jsonify({"message": "Patient added successfully"}), 201

@patients_bp.route('/patients/<int:id>', methods=['GET'])
def get_patient(id):
    patient = Patient.query.get_or_404(id)
    return jsonify({"name": patient.name, "age": patient.age, "gender": patient.gender}), 200
