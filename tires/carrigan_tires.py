from abc import ABC
from tires.tires import Tires

class CarriganTires(Tires, ABC):
    def __init__(self, last_service_tires):
        self.last_service_tires = last_service_tires

    def needs_service(self):

    	#Sorts the array from least to greatest
        self.last_service_tires.sort()

    	#Should return true if the last element is 0.9 or greater, since
    	#we only need to check if at least one element is 0.9 or greater
        return self.last_service_tires[3] >= 0.9