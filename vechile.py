class Vechile:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        
    def start_vechile(self):
        print("Starting the vechile")
    
    def stop_vechile(self):
        print("Stopping the vechile")

class Car(Vechile):
    def __init___(self, make, model, doors_qty):
        super.__init__(make, model)
        self.doors_qty = doors_qty
    
    def locks_doors(self):
        # logic to looks the car door
        pass
    def unlook_doors(self):
        # logic for unlooking the door
        pass 
