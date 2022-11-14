class Car:
    # properties
    wheels = 4
    engine = 1
    # methods
    def start_engine(self):
        print("engine started!")
        
    def run(self):
            print("I am running!")
            print("bruh bruh!")

class Car2022(Car):
    # properties
    led_light = 1
    cam_360 = 1
    # methods
    def run_smart(self):
        print("I am running, smart mode!")

my_car = Car()
print(f"My car has {my_car.wheels} wheels.")
print(f"My car has {my_car.engine} engine")
my_car.start_engine()
print(my_car.start_engine()) #None
my_car.run()

my_2022_car = Car2022()
print(f"My 2022 car has {my_2022_car.wheels} wheels.")
print(f"My 2022 car has {my_2022_car.engine} engine")
print(f"My 2022 car has {my_2022_car.led_light} LED light.")
print(f"My 2022 car has {my_2022_car.cam_360} 360 CAM.")
#my_2022_car.run()
my_2022_car.run_smart()
