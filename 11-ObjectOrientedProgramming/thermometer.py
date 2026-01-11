import random

class Thermometer:
    def __init__(self):
        self.temperature = 0
        self.is_on = False

    def turning_on(self):
        self.is_on = True

    def turning_off(self):
        self.is_on = False


    def measuring(self):
        if self.is_on == True:
            self.temperature = round(random.uniform(34.0,42.0),1)

    def display_value(self):
        if self.temperature >= 37 and self.temperature <41:
            print(f'Temperature: {self.temperature}C (fever)')
        if self.temperature >= 41:
            print(f"Temperature: {self.temperature}C  (fever)('CRTICAL TEMPERATURE!!')")
            
        if self.temperature <37:
            print(f'Temperature: {self.temperature}C')
