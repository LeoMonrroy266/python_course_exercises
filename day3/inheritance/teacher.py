#!/usr/bin/env python
from .person import Person

class Teacher(Person):
    def __init__(self,first_name, last_name, course):
        super(Teacher, self).__init__(first_name, last_name)
        self.course = course
    def printNameSubject(self):
        print(self.get_info(),self.course)
