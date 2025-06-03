import uuid

class System:
    def __init__(self, name=None):
        self.id = uuid.uuid1()
        self.name=name
        self.sensors=[]


    def __len__(self):
        return len(self.sensors)


    def change_name(self, new_name):
        self.name=new_name


    def add_camera(self, name=None):
        new_sensor = Sensor(self, system=self, name=name)
        self.sensors.append(new_sensor)




class Sensor:
    def __init__(self, system: System, name = None):
        self.id = len(system)
        self.system = system
        if name == None:
            self.name = f"Sensor {self.id}"
        else:
            self.name=name
        self.ip = None
    
    
    

    

