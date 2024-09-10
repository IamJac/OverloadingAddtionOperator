class Adder:
    def __init__(self,r,i):
        self.real_part=r
        self.imaginary_part=i
    def __add__(self,other):
        num=self.real_part + other.real_part
        num1=self.imaginary_part + other.imaginary_part
        return num,num1
print("Input the first complex number")
num3=int(input("Real part"))
num4=int(input("Imaginary part"))
object1=Adder(num3,num4)
print("Input the second complex number")
num5=int(input("Real part"))
num6=int(input("Imaginary part"))
object2=Adder(num5,num6)
num7,num8=object1 +object2
print("The resulting sum is ",num7,"+",num8,"i")