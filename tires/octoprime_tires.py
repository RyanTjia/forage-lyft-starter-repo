from abc import ABC
from tires.tires import Tires

class OctoprimeTires(Tires, ABC):
    def __init__(self, last_service_tires):
        self.last_service_tires = last_service_tires

    def needs_service(self):
        return sum(self.last_service_tires) >= 3.0