from flask import Blueprint, request, jsonify
from models import HeartRate, db

heart_rate_bp = Blueprint('heart_rate', __name__)

@heart_rate_bp.route('/patients/<int:id>/heart_rate', methods=['POST'])
def record_heart_rate(id):
    data = request.get_json()
    new_entry = HeartRate(patient_id=id, bpm=data['bpm'])
    db.session.add(new_entry)
    db.session.commit()
    return jsonify({"message": "Heart rate recorded"}), 201

@heart_rate_bp.route('/patients/<int:id>/heart_rate', methods=['GET'])
def get_heart_rate(id):
    heart_rates = HeartRate.query.filter_by(patient_id=id).all()
    return jsonify([{"timestamp": hr.timestamp, "bpm": hr.bpm} for hr in heart_rates]), 200
