name = input('Enter name of student')
chemistry = int(input('Enter marks of chemistry'))
physics =  int(input('Enter marks of physice'))
maths = int(input('Enter marks of mathematics'))
urdu = int(input('Enter marks of urdu'))
islamiat = int(input('Enter marks of islamiat'))

total = chemistry + physics + maths + urdu + islamiat
avg = total / 500
per = avg * 100
z = int(per)

print(z)
if z >= 80:
    print("The Grade of student "+name+" is A1")
elif z >= 70 and z < 80:
    print("The Grade of student "+name+" is A")
elif z >= 60 and z < 70:
    print("The Grade of student " + name + " is B")
elif 45 <= z and z < 60:
    print("The Grade of student " + name + " is C")
else:
    print("The Grade of student " + name + " is Fail")


