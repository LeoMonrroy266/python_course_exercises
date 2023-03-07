#!/usr/bin/python3
class Birds:
    def __init__(self):
        ''' Constructor for this class. '''
        # Create some member animals
        self.members = ['Sparrow', 'Robin', 'Duck']
        self.dangerous = []
        self.harmless = ['Sparrow', 'Robin', 'Duck']
        self.state = ''

    def printMembers(self):
        translate = {'': '', 0: 'harmless', 1: 'dangerous'}
        print(f'Printing members of the {translate[self.state]} Birds class')
        for member in self.members:
            print('\t%s ' % member)

    def Dangerous(self):
        self.members = self.dangerous
        self.state = 1
        return self

    def Harmless(self):
        self.members = self.harmless
        self.state = 1
        return self
