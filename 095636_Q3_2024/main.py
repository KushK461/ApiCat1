class Vehicle:
    def __init__(self, registration_number, make, model):
        self.registration_number = registration_number
        self.make = make
        self.model = model
class Car(Vehicle):
    def __init__(self, registration_number, make, model, num_seats):
        super().__init__(registration_number, make, model)
        self.num_seats = num_seats

class Truck(Vehicle):
    def __init__(self, registration_number, make, model, cargo_capacity):
        super().__init__(registration_number, make, model)
        self.cargo_capacity = cargo_capacity

class Motorcycle(Vehicle):
    def __init__(self, registration_number, make, model, engine_capacity):
        super().__init__(registration_number, make, model)
        self.engine_capacity = engine_capacity

class Fleet:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def show_all_vehicles(self):
        for vehicle in self.vehicles:
            if isinstance(vehicle, Car):
                print(f"Car: {vehicle.make} {vehicle.model}, Seats: {vehicle.num_seats}, Registration: {vehicle.registration_number}")
            elif isinstance(vehicle, Truck):
                print(f"Truck: {vehicle.make} {vehicle.model}, Capacity: {vehicle.cargo_capacity}, Registration: {vehicle.registration_number}")
            elif isinstance(vehicle, Motorcycle):
                print(f"Motorcycle: {vehicle.make} {vehicle.model}, Engine Capacity: {vehicle.engine_capacity}, Registration: {vehicle.registration_number}")

    def search_vehicle_by_registration(self, registration_number):
        for vehicle in self.vehicles:
            if vehicle.registration_number == registration_number:
                return vehicle
        return None

if __name__ == "__main__":
    # Create instances of different vehicles
    car1 = Car("CAR1", "Porsche", "Cayenne", 4)
    truck1 = Truck("Lorry1", "ISUZU", "NQR Hybrid", "2500 kg")
    motorcycle1 = Motorcycle("MT1", "Bajaj", "BJ50", "450cc")
    fleet = Fleet()

    fleet.add_vehicle(car1)
    fleet.add_vehicle(truck1)
    fleet.add_vehicle(motorcycle1)

    print("All vehicles:")
    fleet.show_all_vehicles()

    search_registration_number = "MT1"
    found_vehicle = fleet.search_vehicle_by_registration(search_registration_number)
    if found_vehicle:
        print(f"\nVehicle found with registration number '{search_registration_number}':")
        if isinstance(found_vehicle, Car):
            print(f"Car: {found_vehicle.make} {found_vehicle.model}, Seats: {found_vehicle.num_seats}")
        elif isinstance(found_vehicle, Truck):
            print(f"Truck: {found_vehicle.make} {found_vehicle.model}, Capacity: {found_vehicle.cargo_capacity}")
        elif isinstance(found_vehicle, Motorcycle):
            print(f"Motorcycle: {found_vehicle.make} {found_vehicle.model}, Engine Capacity: {found_vehicle.engine_capacity}")
    else:
        print(f"\nVehicle with registration number '{search_registration_number}' not found.")
