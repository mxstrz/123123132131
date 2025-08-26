#print( 200//21 )
#print( 200//11 )
#print( 200//221 )
#float
##input1 = float( input("Enter a number: ") )



Name = input("Enter your name: ")
print(f"Hello {Name}")

a = input("Enter a email: ")
if "@" not in a:
    print("one more time: Atempts 3")
    a = input("Enter a email: ")
    if "@" not in a:
        print("one more time: Atempts 2")
        a = input("Enter a email: ")
    if "." not in a:
        print("one more time: Atempts 1")
        a = input("Enter a email: ")
        if "@" not in a:
            print("Atempts 0")
            exit()
        else:
            print("Email is correct")


#print(f"Email: {a}")

b = input("Enter nomber ur phone: ")

#print(f"Phone number: {b}")

c = input("Enter a masawge: ")

#print(f"Message 1: {c}")

d = input("Enter a masawge: ")

#print(f"Message 2: {d}")

print(a,b,c,d)

