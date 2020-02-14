#printing a statement

print (" Hello Group B")

#---------------------------------------


#variables && strings

a=123
b=1.23
c="hello"
print(a,b,c)


#checking the type of variable

print(type(a),type(b),type(c))


#assigning variables in same line!!!

a,b=2,"python"

print(a,b)
#--------------------------------------
#lists

list=[1,2,3,4,5,6]
print(list)

#lists can contail lists of lists...!!!

a=[[1,2],[3,4],[5,6]]
print(a)

print(a[1])

#using ''+'' operator in list!!

b=[1,2,3]
c=[2,3,4]
print(b + c)

#addition in lists!!!

print(b[1] + c[0])

#--------------------------------------

#operators

print(1+2)     #addition
print(10/5)    #division
print(5-2)     #subraction
print(2*8)     #multiplication
print(10%4)    #modulas(remainder)
print(2**2)    #square
print(3**3)    #cubic

print ("Group B  "* 10)




#---------------------------------------

string1 =" hello world"

print(string1.upper())
print(string1.lower())

af = string1.split(" ")
print(af)

#---------------------------------------

#conditions

a= 5
print(a==5)
print(a==9)
print(a>9)


#----------------------------------------


#Boolean operators


name = "Bill"
age = 22
if name == "Bill" and age == 22:
    print("Your name is Bill and you are 22 years old.")

if name == "Bill" or name == "Jack":
    print("Your name is either Bill or Jack.")


#in operator

nam= "Bill"

if nam in ["Bill","Jack"]:
    print("you are either BIll or Jack")
    
    
#if statement

if age==22:
    print("age is 22")
    
else:
    print("age is not 22")
    
    
#is operator


x = [1,2,3]
y = [1,2,3]
print(x == y) # Prints out True
print(x is y) # Prints out False


#not operator

print(not False) # Prints out True
print((not False) == (False)) # Prints out False
