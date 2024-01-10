age=int(input("enter your age:- "))
gen=input("enter your gender(M for male and F for female):- ")
marital=input("enter marital status(Y for yes and N for no):- ")

if gen=='f' or gen=='F':
    print('she work in urden area only')
elif gen=='m' or gen=='M':
    if age>=20 and age<40:
        print('Employee is male between the age of 20 and 40 then he can work anywhere')
    if age>=40 and age<=60:
        print('Employee is male between the age of 40 and 60 then he work in urban area only')
    else:
        print('Error')
else:
    print('Error')
        

