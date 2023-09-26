#defining Camper class and defining constructor and methods
class Camper():
    def __init__(self,name,batch,course_type):
        self.name=name;
        self.batch=batch;
        self.course_type=course_type;
    def career_track(self):
        print(f"Currently enrolled in the {self.course_type} program");
    def info(self):
        print(f"My name is {self.name} of batch {self.batch}");
#Creating zuitt_camper instance of class Camper i.e method
zuitt_camper=Camper("BENUP GHIMIRE","BEC003","Python BootCamp");
#Printing the values of variable and method of zuitt_camper instances
print("\nCamper Information:")
print(f"Camper Name:{zuitt_camper.name}\nCamper Batch:{zuitt_camper.batch}\nCamper Course:{zuitt_camper.course_type}\n");
zuitt_camper.info();
zuitt_camper.career_track();
print("\n");
