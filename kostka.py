#!/usr/bin/env python3

class Kostka:
    '''
    Trida reprezentujici hraci kostku.
    '''


    def __init__(self, pocet_sten=6):
        self.__pocet_sten = pocet_sten

    def __str__(self):
        return f'Kostka s {self.__pocet_sten} stenami.'

    def hod(self):
        import random
        return random.randint(1,self.__pocet_sten)

    def get_pocet_sten(self):
        return self.__pocet_sten
    
    def set_pocet_sten(self, novy_pocet_sten):
        try:
            novy_pocet_sten = int(novy_pocet_sten)
            if novy_pocet_sten > 0:
                self.__pocet_sten = novy_pocet_sten
            else:
                print('Pocet sten musi byt > 0.')
        except:
            print('Pocet sten musi byt kladne cele cislo.')
            