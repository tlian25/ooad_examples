from typing import List
from enum import Enum

# Enumerated Properties for GuitarSpec

class Builder(Enum):
    ANY = 0
    FENDER = 1
    MARTIN = 2
    GIBSON = 3
    COLLINGS = 4
    OLSON = 5
    RYAN = 6
    PRS = 7

class Wood(Enum):
    INDIAN_ROSEWOOD = 1
    BRAZILIAN_ROSEWOOD = 2
    MAHOGANY = 3
    MAPLE = 4
    COCOBOLO = 5
    CEDAR = 6
    ADIRONDACK = 7
    ALDER = 8
    SITKA = 9


class NumStrings(Enum):
    SIX = 6
    TWELVE = 12

class Type(Enum):
    ACOUSTIC = 1
    ELECTRIC = 2





class GuitarSpec:
    def __init__(self, builder:Builder, 
                       numstrings:NumStrings,
                       model:str,
                       type:Type,
                       backWood:Wood,
                       topWood:Wood):

        self._builder = builder
        self._numstrings = numstrings
        self._model = model
        self._type = type
        self._backWood = backWood
        self._topWood = topWood


    def matches(self, other) -> bool:
        if self._builder != other._builder:
            return False
        if self._model != other._model:
            return False
        if self._type != other._type:
            return False
        if self._numstrings != other._numstrings:
            return False
        if self._backWood != other._backWood:
            return False
        if self._topWood != other._topWood:
            return False

        return True
        
        





class Guitar:
    def __init__(self, serialNumber:str, price:float, spec:GuitarSpec): 
        self._serialNumber = serialNumber
        self._price = price
        self._spec = spec

    def __eq__(self, other):
        return self._serialNumber == other._serialNumber

    def getSerialNumber(self):
        return self._serialNumber

    def getPrice(self):
        return self._price

    def getSpec(self):
        return self._spec





class Inventory:
    def __init__(self, guitars:List[Guitar]=[]):
        self._guitars = guitars


    def addGuitar(self, guitar:Guitar) -> None:
        self._guitars.append(guitar)

    
    # Gets guitar based on serial number
    def getGuitar(self, serialnum:str) -> Guitar:
        
        for guitar in self._guitars:
            if guitar.getSerialNumber() == serialnum:
                return guitar

        return None


    # Takes in a client's ideal guitar and returns
    # a guitar from inventory that matches specs
    def search(self, searchspec:GuitarSpec) -> List[Guitar]:
        
        matches = []
        for guitar in self._guitars:
            if guitar.getSpec().matches(searchspec):
                matches.append(guitar)

        return matches

    
        