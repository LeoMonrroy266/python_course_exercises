#!/usr/bin/env python
from .person import Person

class Student(Person):
    def __init__(self,first_name, last_name, subject):
        super(Student, self).__init__(first_name, last_name)
        self.subject = subject
    def printNameSubject(self):
        print(self.get_info(),self.subject)
