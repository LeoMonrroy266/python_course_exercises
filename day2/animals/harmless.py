#!/usr/bin/python

from . import *
class harmless:

    @staticmethod
    def Birds():
        harmless_birds = Birds().Harmless()
        return harmless_birds

    @staticmethod
    def Mammals():
        harmless_Mammals = Mammals().Harmless()
        return harmless_Mammals

    @staticmethod
    def Fish():
        harmless_fish = Fish().Harmless()
        return harmless_fish
