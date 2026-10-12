def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multi(a,b):
    return a*b
def div(a,b):
    return a/b
def per(a,b):
    return (a/b)*100
def evenodd(a,b):
    if a//2==0:
             if a/2==0:
                print(a, "is even","\n")
             else:
                 print(a, "is odd","\n")
             if b//2==0:
                 print(b, "is even","\n")
             else:
                 print(b, "is odd","\n") 

def calc(a,b):
    a=x
    b=y

    i = 1
          
    while i !=7:
          print("press the number to perform the respective operation\n")
          print("1.addition")
          print("2.substraction")
          print("3.multiplication")
          print("4.division")
          print("5.check even/odd")
          print("6.calculate percentage of first wrt other")
          print("7.exit")
          i =int(input())
          while i<1 or i>7:
              print("wrong in put , enter between 1 and 7")
              i =int(input())
          if i==1:
              print("addition: ",add(a,b))
          elif i==2:
              print("substraction: ",sub(a,b))
          elif i==3:
              print("product: ",multi(a,b))
          elif i==4:
              if b==0:
                  print("cannot divide by 0","\n")
                  continue
              else:
                  print(div(a,b))
          elif i==5:
              evenodd(a,b)  
          elif i==6:
              print("percentage: ",per(a,b))
          else:
              print("exiting the program","\n")
              break

print("enter the numbers to be operated upon")
x=int(input("number 1:"))
y=int(input("number 2:"))
calc(x,y)



