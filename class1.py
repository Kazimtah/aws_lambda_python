class Linuxuser:
    def __init__(self, username, group, shell):
        self.username = username 
        self.group = group
        self.shell = shell
    
    def show_info(self):
        print(f"Username: {self.username}, group: {self.group}, shell: {self.shell}")

username = Linuxuser("kazim", "wheel", "/bin/bash")
username.show_info()

class Service:
    def __init__(self, service_name):
        self.service_name = service_name
    
    # This function will show the status of the serivice
    def status(self):
        print(f"Status of  {self.service_name}")
    #This function will stop the sevices
    def stop(self):
        print(f"Stop {self.service_name}")

    #This function will start the services
    def start(self):
        print(f"Starting")
service_name1 = Service("apache2")
service_name1.status()
service_name1.start()
service_name1.stop()

class Portchecker:
    def __init__(self, port_number):
        self.port_number = port_number
    
    def portcheker(self):
<<<<<<< HEAD
        if 1<=self.port_number<=65535:
=======
        if 1 <=self.port_number <= 65535:
>>>>>>> list_dictionary
            print("You entered the right port number")
        else:
            print("Please enter the correct port number")

p = Portchecker(22)
<<<<<<< HEAD
p.portcheker()
=======
p.portcheker()
print(isinstance(p, Portchecker))
print(dir(p))
print(issubclass(object,Portchecker))
print(issubclass(Portchecker, object))
>>>>>>> list_dictionary
