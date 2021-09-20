print("Perimeter of a Trapezoid Calculator")
print("""

        _____________
       /             \\
      /               \\
     /                 \\
    /___________________\\
    
""")

baseA = int(input("What is the length of base A?: "))
baseB = int(input("What is the length of base B?: "))
sideC = int(input("What is the length of side C?: "))
sideD = int(input("What is the length of side D?: "))
print("The perimeter of the trapezoid is ", baseA + baseB + sideC + sideD)



def PerimeterOfTrapezoid(BaseA, BaseB, SideC, SideD):
    print(f"Perimeter of the trapezoid is {int(BaseA) + int(BaseB) + int(SideC) + int(SideD)}")
print("The Length of Base A is 2")
print("The Length of Base B is 2")
print("The Length of Side C is 4")
print("The Length of Side D is 3")
PerimeterOfTrapezoid(2,2,4,3) 







