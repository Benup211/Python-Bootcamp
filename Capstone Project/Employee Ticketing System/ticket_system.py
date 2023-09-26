#################Abstract Class ->Person Creation#########
from abc import ABC,abstractmethod;
class Person(ABC):
    ####################abstract methods###################
    @abstractmethod
    def getFullName(self):
        pass;
    @abstractmethod
    def addRequest(self):
        pass;
    @abstractmethod
    def checkRequest(self):
        pass;
    @abstractmethod
    def addUser(self):
        pass;
#Creating Employee Class from Person
####################Employee Class#####################
class Employee(Person):
    #constructor
    def __init__(self,firstName,lastName,email,department):
        self._firstName=firstName;
        self._lastName=lastName;
        self._email=email;
        self._department=department;
    ##############Employee methods#####################
    ###############getter##############################
    def getFirstName(self):
        return (self._firstName);
    def getLastName(self):
        return (self._lastName);
    def getEmail(self):
        return (self._email);
    def getDepartment(self):
        return (self._department);
    ###################setter###########################
    def setFirstName(self,firstName):
        self._firstName=firstName;
    def setLastName(self,lastName):
        self._lastName=lastName;
    def setEmail(self,email):
        self._email=email;
    def setDepartment(self,department):
        self._department=department;
    ##################abstract methods##################
    def getFullName(self):
        return (self._firstName+" "+self._lastName);
    def addRequest(self):
        return "Request has been added";
    def addUser(self):
        return "User has been added";
    def checkRequest(self):
        return "Request checked";
    ####################additional methods#################
    def login(self):
        return (f"{self._email} has logged in");
    def logout(self):
        return (f"{self._email} has logged out");


################TeamLead Class##############################
class TeamLead(Person):
    def __init__(self,firstName,lastName,email,department):
        self._firstName=firstName;
        self._lastName=lastName;
        self._email=email;
        self._department=department;
        self._members=[];
    ##############TeamLead methods#####################
    ###############getter##############################
    def getFirstName(self):
        return (self._firstName);
    def getLastName(self):
        return (self._lastName);
    def getEmail(self):
        return (self._email);
    def getDepartment(self):
        return (self._department);
    ###################setter###########################
    def setFirstName(self,firstName):
        self._firstName=firstName;
    def setLastName(self,lastName):
        self._lastName=lastName;
    def setEmail(self,email):
        self._email=email;
    def setDepartment(self,department):
        self._department=department;
    ##################abstract methods##################
    def getFullName(self):
        return (self._firstName+" "+self._lastName);
    def addRequest(self):
        return "Request has been added";
    def addUser(self):
        return "User has been added";
    def checkRequest(self):
        return "Request checked";
    ####################additional methods#################
    def login(self):
        return (f"{self._email} has logged in");
    def logout(self):
        return (f"{self._email} has logged out");
    def addMember(self,memberValue):
        self._members.append(memberValue);
    def get_members(self):
        return (self._members);

########################Admin Class#########################
class Admin(Person):
    def __init__(self,firstName,lastName,email,department):
        self._firstName=firstName;
        self._lastName=lastName;
        self._email=email;
        self._department=department;
    ##############Employee methods#####################
    ###############getter##############################
    def getFirstName(self):
        return (self._firstName);
    def getLastName(self):
        return (self._lastName);
    def getEmail(self):
        return (self._email);
    def getDepartment(self):
        return (self._department);
    ###################setter###########################
    def setFirstName(self,firstName):
        self._firstName=firstName;
    def setLastName(self,lastName):
        self._lastName=lastName;
    def setEmail(self,email):
        self._email=email;
    def setDepartment(self,department):
        self._department=department;
    ##################abstract methods##################
    def getFullName(self):
        return (self._firstName+" "+self._lastName);
    def addRequest(self):
        return "Request has been added";
    def addUser(self):
        return "User has been added";
    def checkRequest(self):
        return "Request checked";
    ####################additional methods#################
    def login(self):
        return (f"{self._email} has logged in");
    def logout(self):
        return (f"{self._email} has logged out");

#########################Request class######################
class Request():
    def __init__(self,name,requester,dataRequested):
        self._name=name;
        self._requester=requester;
        self._dataRequested=dataRequested;
        self._status="";
    #getter
    def getName(self):
        return (self._name);
    def getRequester(self):
        return (self._requester);
    def getDataRequested(self):
        return (self._dataRequested);
    def get_Status(self):
        return (self._status);
    #setter
    def setName(self,name):
        self._name=name;
    def setRequester(self,requester):
        self._requester=requester;
    def setDataRequested(self,dataRequested):
        self._dataRequested=dataRequested;
    def set_status(self,status):
        self._status=status
    ########################methods############################
    def closeRequest(self):
        return (f"Request {self._name} has been {self._status}");
    def cancelRequest(self):
        return (f"Request {self._name} has been cancelled");
    def updateRequest(self):
        return (f"Request {self._name} has been updated");

if __name__ == '__main__':
    employee1 = Employee("John", "Doe", "djohn@mail.com", "Marketing");
    employee2 = Employee("Jane", "Smith", "sjane@mail.com", "Marketing");
    employee3 = Employee("Robert", "Patterson", "probert@mail.com", "Sales");
    employee4 = Employee("Brandon", "Smith", "sbrandon@mail.com", "Sales");
    admin1 = Admin("Monika", "Justin", "jmonika@mail.com", "Marketing");
    teamLead1 = TeamLead("Michael", "Specter", "smichael@mail.com", "Sales");
    req1 = Request("New hire orientation", teamLead1, "27-Jul-2021");
    req2 = Request("Laptop repair", employee1, "1-Jul-2021");
    ##############checking value of instances if it is correct or not################
    assert employee1.getFullName() == "John Doe", "Full name should be John Doe"
    assert admin1.getFullName() == "Monika Justin", "Full name should be Monika Justin" 
    assert teamLead1.getFullName() == "Michael Specter", "Full name should be Michael Specter"
    assert employee2.login() == "sjane@mail.com has logged in"
    assert employee2.addRequest() == "Request has been added"
    assert employee2.logout() == "sjane@mail.com has logged out"
    teamLead1.addMember(employee3);
    teamLead1.addMember(employee4);
    for indiv_emp in teamLead1.get_members(): 
        print(indiv_emp.getFullName());
    assert admin1.addUser() == "User has been added";
    req2.set_status("closed"); 
    print(req2.closeRequest());