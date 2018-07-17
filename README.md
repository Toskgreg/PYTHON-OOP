#PROJECT TO TEST PROPER KNOWLEDGE OF OOP
<a href="https://codeclimate.com/github/Toskgreg/PYTHON-OOP/maintainability"><img src="https://api.codeclimate.com/v1/badges/ded5dccb81e8a9542355/maintainability" /></a>
[![Build Status](https://travis-ci.org/Toskgreg/PYTHON-OOP.svg?branch=develop)](https://travis-ci.org/Toskgreg/PYTHON-OOP)
[![Coverage Status](https://coveralls.io/repos/github/Toskgreg/PYTHON-OOP/badge.svg?branch=develop)](https://coveralls.io/github/Toskgreg/PYTHON-OOP?branch=develop)
Modelling patients in a hospital using OOP principles .
Because of time constraints I use a very simplistic real life model of patients in a hospital to demonstrate my understanding of OOP.

I demonstrate inheritance by the childrenpatient and adultpatient classes inheriting from the parent class patient.
Methods report_to_hospital, go_to_hospital, leave_hospital, pay_fees and go_home are all implemented once in the parent class and inherite
by the child classes.

I demonstrate encapsulation by using a private variable _fees_due, which can be altered through the pay_fees method, I also implement a private method __discharged in the patient class. 

I demonstrate polymorphism by using and an abstract method calculate_fees which is defined in the parent class but implemented
by the child classes in different ways which also overriding. 

I use the adultpatient class constructor to demonstrate overloading. adultpatient("Tosk", "16yrs", "lion", True)
and adultpatient("Greg", "15years", "Tiger") are both valid calls to the constructor.

