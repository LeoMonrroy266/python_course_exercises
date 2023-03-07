#!/usr/bin/python3
class Fish:
    def __init__(self):
        ''' Constructor for this class. '''
        # Create some member animals
        self.members = ['Salmon', 'Shark', 'Cod']
        self.harmless = ['Salmon', 'Cod']
        self.dangerous = ['Shark']
        self.state = ''

    def printMembers(self):
        translate = {'':'', 0:'harmless', 1:'dangerous'}
        print(f'Printing members of the {translate[self.state]} Fish class')
        for member in self.members:
            print('\t%s ' % member)

    def Dangerous(self):
        self.members = self.dangerous
        self.state = 1
        return self

    def Harmless(self):
        self.members = self.harmless
        self.state = 0
        return self

