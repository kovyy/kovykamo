#!/usr/bin/env python3



class Bojovnik:
    '''
    Trida reprezentujici bojovnika
    '''
    
    def __init__ (self, jmeno, zivot, utok, obrana, kostka):
        self.jmeno = jmeno
        self.zivot = zivot
        self.max_zivot = zivot 
        self.utok = utok
        self.obrana = obrana
        self.kostka = kostka
        self._zprava = ''

    def __str__(self):
        return str(self.jmeno) 

    @property 
    def nazivu(self):
        return self.zivot > 0

    def utoc(self, souper):
        uder = self.utok + self.kostka.hod()
        souper.bran_se(uder)
    

    def graficky_zivot(self):
        return self.graficky_ukazatel(self.zivot, self.max_zivot)
        


    def graficky_ukazatel(self, aktualni, maximalni):
        celkem = 20
        pocet = int(aktualni / maximalni * celkem)
        if pocet == 0 and self.nazivu:
            pocet == 1
        return f'[{"#" * pocet}{" "*(celkem-pocet)}]'

    def bran_se(self, uder):
        zraneni = uder - (self.obrana + self.kostka.hod())
        if zraneni > 0:
            self.zivot = self.zivot - zraneni
            zprava = f'{self.jmeno} utrpel zraneni o sile {zraneni}.'
            if self.zivot <= 0:
                self.zivot = 0
                
                zprava = zprava[:-1] + ' a zemrel.'
        else:
            zprava = f'{self.jmeno} zcela odrazil utok'
        self.set_zprava(zprava)

    def set_zprava(self, zprava):
        self._zprava = zprava 

    def get_zprava(self):
        return self._zprava




class Mag(Bojovnik):

    def __init__(self, jmeno, zivot, utok, obrana, kostka, mana, magicky_utok):
        super().__init__(jmeno, zivot, utok, obrana, kostka)
        self._mana = mana
        self._max_mana = mana
        self._magicky_utok = magicky_utok

    def utoc(self, souper):
        if self._mana < self._max_mana: 
            self._mana += 10 
            if self._mana > self._max_mana: self._mana = self._max_mana

            super().utoc(souper)
        else: 
            uder = self._magicky_utok + self.kostka.hod()
            self.__set_zprava = f'({self.jmeno} utoci magii za {uder}'
            self._mana = 0
            souper.bran_se(uder)

    def graficka_mana(self):
        return self.graficky_ukazatel(self._mana, self._max_mana)



