import unittest
import datetime

from car_factory import CarFactory

class TestCalliope(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        current_date = datetime.date.today()
        last_service_date = current_date.replace(year = current_date.year - 3)
        current_mileage = 100
        last_service_mileage = 0

        car = CarFactory.create_calliope(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        current_date = datetime.date.today()
        last_service_date = current_date.replace(year = current_date.year - 1)
        current_mileage = 250
        last_service_mileage = 0

        car = CarFactory.create_calliope(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())

    def test_engine_should__be_serviced(self):
        current_date = datetime.date.today()
        last_service_date = datetime.date.today()
        current_mileage = 30001
        last_service_mileage = 0

        car = CarFactory.create_calliope(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_date = datetime.date.today()
        last_service_date = datetime.date.today()
        current_mileage = 29999
        last_service_mileage = 0

        car = CarFactory.create_calliope(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())


class TestGlissade(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        current_date = datetime.date.today()
        last_service_date = current_date.replace(year = current_date.year - 6)
        current_mileage = 300
        last_service_mileage = 0

        car = CarFactory.create_glissade(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        current_date = datetime.date.today()
        last_service_date = current_date.replace(year = current_date.year - 1)
        current_mileage = 350
        last_service_mileage = 0

        car = CarFactory.create_glissade(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())

    def test_engine_should__be_serviced(self):
        current_date = datetime.date.today()
        last_service_date = datetime.date.today()
        current_mileage = 60001
        last_service_mileage = 0

        car = CarFactory.create_glissade(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_date = datetime.date.today()
        last_service_date = datetime.date.today()
        current_mileage = 59999
        last_service_mileage = 0

        car = CarFactory.create_glissade(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())


class TestPalindrome(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        current_date = datetime.date.today()
        last_service_date = current_date.replace(year = current_date.year - 2)
        warning_light_is_on = False
        
        car = CarFactory.create_palindrome(current_date, last_service_date, warning_light_is_on)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        current_date = datetime.date.today()
        last_service_date = current_date.replace(year = current_date.year - 1)
        warning_light_is_on = False

        car = CarFactory.create_palindrome(current_date, last_service_date, warning_light_is_on)
        self.assertFalse(car.needs_service())

    def test_engine_should__be_serviced(self):
        current_date = datetime.date.today()
        last_service_date = datetime.date.today()
        warning_light_is_on = True

        car = CarFactory.create_palindrome(current_date, last_service_date, warning_light_is_on)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_date = datetime.date.today()
        last_service_date = datetime.date.today()
        warning_light_is_on = False

        car = CarFactory.create_palindrome(current_date, last_service_date, warning_light_is_on)
        self.assertFalse(car.needs_service())


class TestRorschach(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        current_date = datetime.date.today()
        last_service_date = current_date.replace(year = current_date.year - 4)
        current_mileage = 400
        last_service_mileage = 0

        car = CarFactory.create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        current_date = datetime.date.today()
        last_service_date = current_date.replace(year = current_date.year - 3)
        current_mileage = 450
        last_service_mileage = 0

        car = CarFactory.create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())

    def test_engine_should__be_serviced(self):
        current_date = datetime.date.today()
        last_service_date = datetime.date.today()
        current_mileage = 75000
        last_service_mileage = 0

        car = CarFactory.create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_date = datetime.date.today()
        last_service_date = datetime.date.today()
        current_mileage = 35000
        last_service_mileage = 0

        car = CarFactory.create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())


class TestThovex(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        current_date = datetime.date.today()
        last_service_date = current_date.replace(year = current_date.year - 6)
        current_mileage = 500
        last_service_mileage = 0

        car = CarFactory.create_thovex(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        current_date = datetime.date.today()
        last_service_date = current_date.replace(year = current_date.year - 2)
        current_mileage = 550
        last_service_mileage = 0

        car = CarFactory.create_thovex(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())

    def test_engine_should__be_serviced(self):
        current_date = datetime.date.today()
        last_service_date = datetime.date.today()
        current_mileage = 30000
        last_service_mileage = 0

        car = CarFactory.create_thovex(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_date = datetime.date.today()
        last_service_date = datetime.date.today()
        current_mileage = 15000
        last_service_mileage = 0

        car = CarFactory.create_thovex(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())


if __name__ == '__main__':
    unittest.main()
