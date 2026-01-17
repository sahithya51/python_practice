#Swapping two number without using third variable
a = int(input("Enter a :"))
b = int(input("Enter b :"))
a = a + b
b = a - b
a = a - b
print(a)
print(b)

#swapping using third variable

c = int(input("Enter c :"))
d = int(input("Enter d :"))
temp = c
c = d
d = temp
print(c)
print(d)