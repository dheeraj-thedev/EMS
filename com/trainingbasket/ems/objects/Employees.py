class Date:
    def __init__(self,day,month,year):
        self.day=day
        self.month=month
        self.year=year

    def __str__(self):
        return  "{}-{}-{}".format(self.day,self.month,self.year)

class Employee(object): #
    tempId=0
    def __init__(self,name,age,contactnumber,email,salary,dob,doj):
        Employee.tempId= Employee.tempId+1
        self.id=Employee.tempId
        self.name=name
        self.age=age
        self.contactnumber=contactnumber
        self.email=email
        self.salary=float( salary)
        self.dob=dob
        self.doj=doj

    def __str__(self):
        return "Name : {}\n Age : {}\n Conatct No :{}\n  Email : {}\n Salary : {}\n DOB :{}\n  DOJ :{}\n "\
            .format(self.id,self.name,self.age,self.contactnumber,self.email,self.salary,self.dob,self.doj)


class Manager(Employee):
    def __init__(self,department,name,age,contactnumber,email,salary,dob,doj):
        super(Manager, self).__init__(name,age,contactnumber,email,salary,dob,doj)
        self.department=department

    def __str__(self):
        return "{} {}".format( super(Manager, self).__str__(),self.department)

class CEO(Employee):
    pass
class Engineer(Employee):
    pass


if __name__ == '__main__':
    m=Manager(
        name='Dheeraj',
        age=30,
        department='R&D',
        contactnumber='9718910927',
        email='bond@gmail.com',
        salary=1.5,
        dob=Date(17,10,1989),
        doj=Date(1,1,2011)
              )

    print(m)
