Amount=int(input("Enter your Number:"))
n1=Amount//100
n2=(Amount%100)//50
n3=((Amount%100)%50)//10
print("Hundread ruppee =",n1)
print("Fifty ruppee =",n2)
print("Ten ruppee",n3)