print("Ratio Finder,Made By CoolPyparusDude")
try:
    r1 = float(input("Set First Number Of Ratio: "))
    r2 = float(input("Set Second Number Of Ratio: "))
    add1_2 = r1+r2
    ratio_no = float(input("Set Ratio Number: "))
    r = ratio_no/add1_2
    r1a = r*r1
    r2a = r*r2
    print("Well Well Well,The Ratio is",r1a,":",r2a)
except ValueError:
    print("Log Error:Why Words,Only Number Allowed")
except ZeroDivisionError:
    print("Log Error:Why Use Number 0,Only Number With A Value is Allowed")
input("Press Enter To Exit.")
