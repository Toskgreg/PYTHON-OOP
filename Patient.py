class Patient:
    """Implementation of the Patient class """

    fee = 400

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        self.status = "out of patient ward"
        self.location = "hospital"
        self._fees_due = 0

    def calculate_fees(self):
       raise NotImplementedError("implemented by child classes")
    
    def report_to_hospital(self):
        self.location = "hospital"
    
    def go_to_patient_ward(self):
        """method changes status of Patient to in patient ward """
        self.status = "in patient ward"
    
    def leave_patient_ward(self):
        """Method changes status to out of patient ward"""
        self.status = "out of patient ward"
    
    def pay_hospital_bills(self,amount):
        """Method modifies the _fees_due attribute of the Patient object, returning a balance where applicable"""
        if self._fees_due == 0:
            return "no need for payment"
        elif amount > self._fees_due:
            self._fees_due = 0
            return amount - self._fees_due
        else:
            self._fees_due -= amount
        
    def go_home(self):
        """Method changes location attribute to home"""
        self.location = 'home'
        
    def __discharged(self):
        """Method called when patient is discharged from hospital"""
        return "You have been discharges"

class children_patients(Patient):
    """Implementing the children_patients class to cater for the young patients"""
    def __init__(self, name, grade):
        Patient.__init__(self, name, grade)
        self._fees_due = self.calculate_fees()

    def calculate_fees(self):
        return Patient.fee 

class mature_patients(Patient):
    """Implementing the mature_patients class to cater for the adult patients"""
    def __init__(self, name, grade, house, ambulance = False):
        Patient.__init__(self, name, grade)
        self.house = house
        self.ambulance = ambulance
        self.quarantine = False
        self._fees_due = self.calculate_fees()

    def calculate_fees(self):
        """Method calculates fees supposed to be paid by adult patient"""
        if self.ambulance:
            return Patient.fee + 100
        else:
            return Patient.fee

    def go_to_quarantine(self):
        """Method sets quarantine atttribute to True for adult patients"""
        self.quarantine = True
    
    def leave_quarantine(self):
        """"Method sets quarantine attribute to False as patient leaves quarantine"""
        self.quarantine = False

    