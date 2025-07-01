from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import PatientRecords, AnthropometricData

# Database configuration
DATABASE_URL = "mysql+pymysql://myuser:mypassword@localhost:3306/mydatabase"
engine = create_engine(DATABASE_URL)  # Create a connection to the database
Session = sessionmaker(bind=engine)  # Create a session factory
session = Session()  # Initialize a session to interact with the database

# Initialize Flask app
app = Flask(__name__)

# Home Page: Display all patients
@app.route("/")
def index():
    patients = session.query(PatientRecords).all()  # Query all patients from the database
    return render_template("index.html", patients=patients)  # Render the template with patient data

# Add Patient Page: Handle form submission to add a new patient
@app.route("/add", methods=["GET", "POST"])
def add_patient():
    if request.method == "POST":
        # Retrieve form data
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        date_of_birth = request.form["date_of_birth"]

        # Create a new patient object
        new_patient = PatientRecords(
            first_name=first_name,
            last_name=last_name,
            date_of_birth=date_of_birth
        )
        session.add(new_patient)  # Add the new patient to the session
        session.commit()  # Commit the transaction to save the data
        return redirect(url_for("index"))  # Redirect to the home page
    return render_template("add_patient.html")  # Render the form for GET requests

# Edit Patient Page: Handle form submission to update an existing patient
@app.route("/edit/<int:patient_id>", methods=["GET", "POST"])
def edit_patient(patient_id):
    patient = session.query(PatientRecords).get(patient_id)  # Retrieve the patient by ID
    if request.method == "POST":
        # Update patient details with form data
        patient.first_name = request.form["first_name"]
        patient.last_name = request.form["last_name"]
        patient.date_of_birth = request.form["date_of_birth"]
        session.commit()  # Commit the changes to the database
        return redirect(url_for("index"))  # Redirect to the home page
    return render_template("edit_patient.html", patient=patient)  # Render the edit form

# Delete Patient Page: Delete a patient by ID
@app.route("/delete/<int:patient_id>")
def delete_patient(patient_id):
    patient = session.query(PatientRecords).get(patient_id)  # Retrieve the patient by ID
    session.delete(patient)  # Delete the patient from the session
    session.commit()  # Commit the transaction to apply the deletion
    return redirect(url_for("index"))  # Redirect to the home page

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)  # Start the app in debug mode for development