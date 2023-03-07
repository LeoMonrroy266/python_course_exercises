from . import *
class dangerous:

    @staticmethod
    def Birds():
        dangerous_birds = Birds().Dangerous()
        return dangerous_birds

    @staticmethod
    def Mammals():
        dangerous_Mammals = Mammals().Dangerous()
        return dangerous_Mammals

    @staticmethod
    def Fish():
        dangerous_fish = Fish().Dangerous()
        return dangerous_fish
