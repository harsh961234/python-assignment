def show_employee(n,a,s=9000):
    print("employee name:",n,"\nage:",a,"\nsalary:",s)

name=input("Enter your name:")
age=int(input("Enter your age:"))
salary=input("Enter your salary:")

if(salary==""):
    show_employee(name,age)
else:
    show_employee(name,age,salary)
