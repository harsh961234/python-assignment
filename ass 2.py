str1="welcom to USA. usa is awesome,in't it?"
count=0
split1=str1.split()

##count= [i for i in split1 if i=="USA." or i=="usa"]
##print(len(count))

for i in split1:
    if i=="USA." or i=="usa":
        count+=1
print("number of time usa occured is:",count)
        
