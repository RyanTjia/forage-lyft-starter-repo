from abc import ABC

from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine
from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery
from tires.carrigan_tires import CarriganTires
from tires.octoprime_tires import OctoprimeTires

from car import Car

class CarFactory(ABC):
	def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, last_service_tires):
		return Car(CapuletEngine(current_mileage, last_service_mileage), SpindlerBattery(last_service_date, current_date), CarriganTires(last_service_tires))

	def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage, last_service_tires):	
		return Car(WilloughbyEngine(current_mileage, last_service_mileage), SpindlerBattery(last_service_date, current_date), CarriganTires(last_service_tires))

	def create_palindrome(current_date, last_service_date, warning_light_is_on, last_service_tires):
		return Car(SternmanEngine(warning_light_is_on), SpindlerBattery(last_service_date, current_date), CarriganTires(last_service_tires))

	def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage, last_service_tires):
		return Car(WilloughbyEngine(current_mileage, last_service_mileage), NubbinBattery(last_service_date, current_date), OctoprimeTires(last_service_tires))

	def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage, last_service_tires):
		return Car(CapuletEngine(current_mileage, last_service_mileage), NubbinBattery(last_service_date, current_date), OctoprimeTires(last_service_tires))
