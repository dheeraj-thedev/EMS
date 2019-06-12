class Employee(object):
    def __init__(self,name,age,contactNo,email):
        self.name=name
        self.age=age
        self.contactNo=contactNo
        self.email=email

    def __str__(self):
        return "NAMe: {} \nAge: {}\nConatcNumber :{} \nEmail Id :{}".format(
            self.name,self.age,self.contactNo,self.email
        )
if __name__ == '__main__':
    empList=[]
    while(input('Do you what to continue add employees press 1 to continues anykey to exit')=='1'):
        emp=Employee(
            email= input('Please ENter the EMail Addres'),#'dheeraj@ytrainingbasket.net',
            name=input('Please Enter The Employee Name'),
            contactNo=input('Plese Enter the contact Number'),
            age=int(input('Please ENter The Age'))
        )
        empList.append(emp)
    for d in empList:
        print(d)
