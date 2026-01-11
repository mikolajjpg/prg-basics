#Identify at least 3 states and 3 behaviors for your smartphone.
 # Then, for the listed states and behaviors, 
#create a class with attributes and methods. 
#Try to use verbs in method names as they describe activities. 
#Finally, create a smartphone object, call its methods and display object’s properties.

class Phone():

    def __init__(self):
        self.charging = False
        self.is_on = False
        self.recording = False


    def connect_charger(self):
        self.charging = True

    def turn_on(self):
        self.is_on = True

    def start_recording(self):
        self.recording = True



    def display_info(self):
    
        if self.charging:
            print(f'The phone is being charged.')
        else: 
            print(f'The phone is not being charged.')

        if self.is_on:
            print(f'The phone is on.')
        else: 
            print(f'The phone is off.')   

        if self.recording:
            print(f'The phone is recording.')
        else: 
            print(f'The phone is not recording.')

def main():

    my_phone = Phone()

    my_phone.display_info()


    my_phone.turn_on()
    my_phone.connect_charger()

    my_phone.display_info()

if __name__ =="__main__":
    main()
        



