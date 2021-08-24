class Vehicle(object):

    def __init__(self, wheels, mileage):
        """
        Simple class

        :param wheels:
        :param mileage:
        """
        assert isinstance(wheels, int), "Wheels should be integer"
        assert isinstance(mileage, float), "Mileage should be actually float"
        # ============
        self._wheels = wheels
        self.mileage = mileage

    def __str__(self):
        return f"I am {self.__class__.__name__}, having {self._wheels} wheels and mileage {self.mileage}"


class Car(Vehicle):

    def __init__(self, wheels, mileage, type_):

        self.type_ = type_
        super(Car, self).__init__(wheels, mileage)


class Truck(Vehicle):

    def __init__(self, wheels, mileage, type_):

        self.type_ = type_
        super(Truck, self).__init__(wheels, mileage)

    def __str__(self):
        return f"I am {self.type_} {self.__class__.__name__}, having {self._wheels} wheels and mileage {self.mileage}"

    def who_am_i(self):
        print(self)


car = Car(4, 45.5, "passenger")
print(car)
truck = Truck(8, 17.4, "commercial")
# print(truck)
truck.who_am_i()
