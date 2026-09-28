class Employee:
    def __init__(self,name,l_name,pay):
            self.name=name
            self.l_name = l_name
            self.pay=pay
            self.email = name+"."+l_name+"@gmail.com"
    def full(self):
          return f"{self.name} {self.l_name} : {self.pay}\n{self.email}\n"

emp_1=Employee("Ali","Aliyev",1500)
emp_2=Employee("Samad","Samadzada",2000)
print(emp_1.full())
print(emp_2.full())

