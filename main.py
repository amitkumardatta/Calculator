#Enter first digit then second the operator
print ('This a basic calculator')
bro = float(input("Enter The First Number\n" ))
print(bro)
far = float(input("Enter the Second number\n"))
print(far)
ops = input("Enter the operator\n")

if ops =="+":
    print ('Addition')
elif ops =="-":
    print ('Subtraction')
elif ops =="*":
    print ('Multiplication')
elif ops =="x":
    print ('Multiplication')
elif ops =="/":
    print ('Division')
elif ops =="%":
    print ('Percentage')
elif ops =="a":
    print ('add')
elif ops =="s":
    print ('sub')
elif ops =="m":
    print ('mul')
elif ops =="d":
    print ('div')
elif ops =="p":
    print ('per')
elif ops =="A":
    print ('add')
elif ops =="S":
    print ('sub')
elif ops =="M":
    print ('mul')
elif ops =="D":
    print ('div')
elif ops =="P":
    print ('per')

print("\nYour Expression and Answer is:" )
print(bro)
print(ops)
print (far)
print("--------\n")

if ops =="+":
    print (bro+far)
elif ops =="-":
    print (bro-far)
elif ops =="*":
    print (bro*far)
elif ops =="x":
    print (bro*far)
elif ops =="/":
    print (bro/far)
elif ops =="%":
    print (bro%far)
elif ops =="a":
    print (bro+far)
elif ops =="s":
    print (bro-far)
elif ops =="m":
    print (bro*far)
elif ops =="d":
    print (bro/far)
elif ops =="p":
    print (bro%far)
elif ops =="A":
    print (bro+far)
elif ops =="S":
    print (bro-far)
elif ops =="M":
    print (bro*far)
elif ops =="D":
    print (bro/far)
elif ops =="P":
    print (bro%far)
else:
    print ("INVALID INPUT\n")
    print ('D D O')


print ("Created by Amit Kumar Datta")