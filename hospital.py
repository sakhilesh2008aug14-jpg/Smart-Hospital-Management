from abc import ABC, abstractmethod


class Person(ABC):
    """Base class for everyone registered in the hospital."""

    def __init__(self, name, age, phone):
        self.name = name
        self.age = age
        self.phone = phone

    @abstractmethod
    def display_details(self):
        """Display details specific to the person type."""
        pass


class Patient(Person):
    """Stores patient information and appointment details."""

    def __init__(self, patient_id, name, age, phone, illness):
        super().__init__(name, age, phone)
        self.patient_id = patient_id
        self.__illness = illness  # Encapsulation: private attribute
        self.appointments = []

    def get_illness(self):
        return self.__illness

    def add_appointment(self, doctor_name, date):
        self.appointments.append((doctor_name, date))

    def display_details(self):
        print(f"\nPatient ID : {self.patient_id}")
        print(f"Name       : {self.name}")
        print(f"Age        : {self.age}")
        print(f"Phone      : {self.phone}")
        print(f"Condition  : {self.__illness}")
        if self.appointments:
            print("Appointments:")
            for doctor, date in self.appointments:
                print(f"  - Dr. {doctor} on {date}")
        else:
            print("Appointments: None")


class Doctor(Person):
    """Stores doctor information."""

    def __init__(self, doctor_id, name, age, phone, specialization, fee):
        super().__init__(name, age, phone)
        self.doctor_id = doctor_id
        self.specialization = specialization
        self.fee = fee

    def display_details(self):
        print(
            f"\nDoctor ID: {self.doctor_id} | Dr. {self.name} | "
            f"Age: {self.age} | Phone: {self.phone} | "
            f"Specialization: {self.specialization} | Fee: Rs. {self.fee:.2f}"
        )


class Bill(ABC):
    """Abstract billing class."""

    @abstractmethod
    def calculate_bill(self):
        pass


class ConsultationBill(Bill):
    """Calculates a consultation bill."""

    def __init__(self, doctor_fee):
        self.doctor_fee = doctor_fee

    def calculate_bill(self):
        return self.doctor_fee


class FollowUpBill(Bill):
    """Calculates a discounted follow-up bill."""

    def __init__(self, doctor_fee):
        self.doctor_fee = doctor_fee

    def calculate_bill(self):
        return self.doctor_fee * 0.5


class Hospital:
    """Manages patients, doctors, appointments and billing."""

    def __init__(self, name):
        self.name = name
        self.patients = {}
        self.doctors = {}

    def add_patient(self, patient):
        if patient.patient_id in self.patients:
            print("A patient with that ID already exists.")
            return
        self.patients[patient.patient_id] = patient
        print("Patient registered successfully.")

    def add_doctor(self, doctor):
        if doctor.doctor_id in self.doctors:
            print("A doctor with that ID already exists.")
            return
        self.doctors[doctor.doctor_id] = doctor
        print("Doctor added successfully.")

    def show_doctors(self):
        if not self.doctors:
            print("No doctors are registered.")
            return
        print("\n--- DOCTOR LIST ---")
        for doctor in self.doctors.values():
            doctor.display_details()

    def show_patients(self):
        if not self.patients:
            print("No patients are registered.")
            return
        print("\n--- PATIENT LIST ---")
        for patient in self.patients.values():
            patient.display_details()

    def book_appointment(self, patient_id, doctor_id, date):
        patient = self.patients.get(patient_id)
        doctor = self.doctors.get(doctor_id)

        if patient is None:
            print("Patient ID not found.")
            return
        if doctor is None:
            print("Doctor ID not found.")
            return

        patient.add_appointment(doctor.name, date)
        print(f"Appointment booked with Dr. {doctor.name} on {date}.")

    def generate_bill(self, doctor_id, bill_type):
        doctor = self.doctors.get(doctor_id)
        if doctor is None:
            print("Doctor ID not found.")
            return

        if bill_type == "1":
            bill = ConsultationBill(doctor.fee)
            bill_name = "Consultation"
        elif bill_type == "2":
            bill = FollowUpBill(doctor.fee)
            bill_name = "Follow-up"
        else:
            print("Invalid bill type.")
            return

        # Polymorphism: the same method works with different bill objects.
        amount = bill.calculate_bill()
        print("\n------- HOSPITAL BILL -------")
        print(f"Hospital     : {self.name}")
        print(f"Doctor       : Dr. {doctor.name}")
        print(f"Bill type    : {bill_name}")
        print(f"Amount       : Rs. {amount:.2f}")
        print("-----------------------------")


def read_int(prompt, minimum=0):
    while True:
        try:
            value = int(input(prompt))
            if value < minimum:
                print(f"Enter a number greater than or equal to {minimum}.")
                continue
            return value
        except ValueError:
            print("Please enter a valid whole number.")


def read_text(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This field cannot be empty.")


def main():
    hospital = Hospital("SmartCare Hospital")

    # Sample doctors make it easy to test the program immediately.
    hospital.add_doctor(
        Doctor("D101", "Ananya", 38, "9876543210", "Cardiology", 700)
    )
    hospital.add_doctor(
        Doctor("D102", "Rahul", 42, "9876501234", "Dermatology", 500)
    )

    while True:
        print(f"\n===== {hospital.name.upper()} =====")
        print("1. Register patient")
        print("2. View patients")
        print("3. View doctors")
        print("4. Book appointment")
        print("5. Generate bill")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            patient_id = read_text("Enter patient ID: ")
            name = read_text("Enter patient name: ")
            age = read_int("Enter age: ", 1)
            phone = read_text("Enter phone number: ")
            illness = read_text("Enter reason for visit: ")
            hospital.add_patient(
                Patient(patient_id, name, age, phone, illness)
            )

        elif choice == "2":
            hospital.show_patients()

        elif choice == "3":
            hospital.show_doctors()

        elif choice == "4":
            patient_id = read_text("Enter patient ID: ")
            doctor_id = read_text("Enter doctor ID (D101/D102): ")
            date = read_text("Enter appointment date (e.g. 15-11-2026): ")
            hospital.book_appointment(patient_id, doctor_id, date)

        elif choice == "5":
            doctor_id = read_text("Enter doctor ID: ")
            print("1. New consultation")
            print("2. Follow-up (50% of consultation fee)")
            bill_type = input("Choose bill type (1/2): ").strip()
            hospital.generate_bill(doctor_id, bill_type)

        elif choice == "6":
            print("Thank you for using SmartCare Hospital Management System!")
            break

        else:
            print("Invalid choice. Please select a number from 1 to 6.")


if __name__ == "__main__":
    main()
