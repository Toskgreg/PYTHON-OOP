import unittest
from Patient import Patient, children_patients, mature_patients



class StudentTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_child_can_go_to_hospital(self):
        """location should be hospital after the admission to hospital"""
        patients = children_patients("Tosk", "7yrs")
        patients.report_to_hospital()
        self.assertEqual("hospital", patients.location)

    def test_adult_can_go_to_hospital(self):
        """location should be equal to school after the report to school method"""
        patients = mature_patients("Tosk", "15yrs", "lion")
        patients.report_to_hospital()
        self.assertEqual("hospital", patients.location)

    def test_children_can_go_to_patient_ward(self):
        """status should be "in patient ward" after the go to class method for children"""
        patients = children_patients("Tosk", "7yrs")
        patients.go_to_patient_ward()
        self.assertTrue(patients.status == "in patient ward")
    def test_children_can_leave_class(self):
        """status should be "out of class" after the go to class method for children"""
        patients = children_patients("Tosk", "7yrs")
        patients.leave_patient_ward()
        self.assertTrue(patients.status == "out of patient ward")




    def test_calculate_fees_children(self):
        """calculate_fees should return 400 for children"""
        patients = children_patients("Tosk", "7yrs" )
        patients_fees = patients.calculate_fees()
        self.assertEqual(patients_fees, 400)

    def test_calculate_fees_adult_no_bus(self):
        """calculate_fees should return 400 with no bus fare """
        patients = mature_patients("Tosk", "15yrs", "lion")
        patients_fees = patients.calculate_fees()
        self.assertEqual(patients_fees, 400)

    def test_calculate_fees_adult_bus(self):
        """calculate_fees should return 500 if student uses bus"""
        patients = mature_patients("Tosk", "15yrs", "lion", True)
        patients_fees = patients.calculate_fees()
        self.assertEqual(patients_fees, 500)

    def test_pay_hospital_bills_with_string_input(self):
        """pay_hospital_bills should raise type error for non-numeric input"""
        patients = mature_patients("Tosk", "15yrs", "lion")
        self.assertRaises(TypeError, patients.pay_hospital_bills, '700')

    def test_pay_hospital_bills_success(self):
        """should change fees due attribute"""
        patients = children_patients("Tosk", "7yrs" )
        due_1 = patients._fees_due
        patients.pay_hospital_bills(300)
        due_2 = patients._fees_due
        self.assertEqual([due_1, due_2], [400, 100])

    def test_go_home_success(self):
        """location should be home after the go_home method for both children and adult"""
        patient1 =  children_patients("Tosk", "7yrs")
        patient2 =  mature_patients("Greg", "15yrs", "lion")
        patient1.go_home()
        patient2.go_home()
        self.assertEqual([patient1.location, patient2.location], ['home', 'home'])

    def test_go_to_quarantine_success(self):
        """for mature patients go_to_quarantine should change in_quarantine to true"""
        patients = mature_patients("Tosk", "15yrs", "lion")
        before_quarantine = patients.quarantine
        patients.go_to_quarantine()
        after_quarantine = patients.quarantine
        self.assertEqual([before_quarantine, after_quarantine], [ False, True])

    def test_leave_quarantine(self):
        """when student leaves quarantine the in_quarantine should change to False"""
        patients = mature_patients("Tosk", "15yrs", "lion")
        patients.go_to_quarantine()
        state1 = patients.quarantine
        patients.leave_quarantine()
        state2 = patients.quarantine
        self.assertEqual([state1, state2], [ True, False])
        