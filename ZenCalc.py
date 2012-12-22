print("#=======================================#")
print("#            ZenOokami Codes            #")
print("#        http://essenceofzen.tk         #")
print("#=======================================#")
print("#          ~    /| ZEN |\   ~           #")
print("#              / |_____| \              #")
print("#             |           |             #")
print("#             |  __   __  |             #")
print("#             <  \/   \/  >             #")
print("#              <         >              #")
print("#                \  v  /                #")
print("#                 \___/                 #")
print("#           `~-::Ookami*::-~`           #")
print("#=======================================#")
print("# _____ _            _    _       _  __ #")
print("#|_   _| |          | |  | |     | |/ _|#")
print("#  | | | |__   ___  | |  | | ___ | | |_ #")
print("#  | | | '_ \ / _ \ | |/\| |/ _ \| |  _|#")
print("#  | | | | | |  __/ \  /\  / (_) | | |  #")
print("#  \_/ |_| |_|\___|  \/  \/ \___/|_|_|  #")
print("#=======================================#")
print("#           Complex Calculator          #")
print("#             Version: 0.2.8            #")
print("#=======================================#")
#Imports and Client-side Settings================
import time
import py_compile
py_compile.compile("ZenCalc.py")

#Global Variables================================
number1 = 0
number2 = 0
answer = 0
storage = 0

temporary_list = []

base = 0
exponent = 0

x1 = 0
x2 = 0
x_sum = 0
y1 = 0
y2 = 0
y_sum = 0
slope = 0

user_input = 0

#Experimental For customization
custom_variables = []
custom_x = []
custom_y = []





#Functions========================================
def power():
    base = float(input("Input base: "))
    exponent = int(input("Input exponent: "))
    start = 0
    answer = 1
    for number in range(exponent):
        answer *= base
        print(str(base) + "^" + str(exponent) + " = " + str(answer))
    
        

def multiply():
    number1 = float(input("Input number1: "))
    number2 = float(input("Input number2: "))
    answer = number1 * number2
    print(str(number1) + " + " + str(number2) + " = " + str(answer))
    

def divide():
    loop=1
    while loop==1:    
        number1 = float(input("Input number1: "))
        number2 = float(input("Input number2: "))
        if number2 == 0:
            print("Cannot divide by 0...)")
        else:
            answer = number1 / number2
            loop = 0
            print(answer)
    
    
def addition():
    number1 = float(input("Input number1: "))
    number2 = float(input("Input number2: "))
    answer = number1 + number2
    print(answer)
    
    
def subtraction():
    number1 = float(input("Input number1: "))
    number2 = float(input("Input number2: "))
    answer = number1 - number2
    
    

def factors():
    number1 = input("First Number: ")
    number2 = input("How many checks: ")
    storage = 0
    for number in range(0, int(number2)):
        answer = int(number1) * (storage + 1)
        temporary_list.append(answer)
        storage += 1
    print(temporary_list)
            

def slope():
    x1 = float(input("Input x1: "))
    x2 = float(input("Input x2: "))
    y1 = float(input("Input y1: "))
    y2 = float(input("Input y2: "))
    x_sum = x1 - x2
    y_sum = y1 - y2
    slope = y_sum / x_sum
    print("The slope is: " + str(slope))
    

def decimal_to_percent():
    number1 = float(input("Input number: "))
    if number1 < 1 :
        answer= number1 * 100
        print(str(answer) + "%")
    else:
        number2 = float(input(str(number1) + " out of how many?: "))
        answer = number1 / number2 * 100
        print(str(answer) + "%")
    

def percent_to_decimal():
    number1 = float(input("Input percentage, without the %: "))
    answer = number1 / 100




def programmer_tools():
        print("|==========================================|")
        print("| Programmer Tools                         |")
        print("|==========================================|")
        print("|:Operations:                              |")
        print("| [Dec to Bin]                             |")
        print("| [Dec to Hex]                             |")
        print("| [Dec to Octal]                           |")
        print("| [Bin to Dec]                             |")
        print("| [Bin to Hex]                             |")
        print("| [Bin to Octal]                           |")
        print("|                                          |")
        print("|                                          |")
        print("| [Exit]                                   |")
        print("|==========================================|")
#****************************************
        
def formulas():
        print("|==========================================|")
        print("| Formulas                                 |")
        print("|==========================================|")
        print("|:Operations:                              |")
        print("| [1] y=mx-b {Includes optional exponents} |")
        print("|                                          |")
        print("| [Exit]                                   |")
        print("|==========================================|")

def ymxb():
    y = 0
    m = input("Please enter the slope in the form of a decimal or whole number: ")
    x = 0
    x_exponent = 0
    mx_exponent = 0
    b = input("Input [b]: ")
    b_exponent = 0

    user_choice =
    
    



#Main=======================================================
def main():
    main_loop = 1
    while main_loop == 1:
            
        print("|==========================================|")
        print("| Main Menu                                |")
        print("|==========================================|")
        print("|:Operations:                              |")
        print("| *[Check Variables]                       |")
        print("| *[Small Graph]                           |")
        print("| *[Programmer Tools]                      |")
        print("| *[Formulas]                              |")
        print("|                                          |")
        print("|                                          |")
        print("| [Add]                                    |")
        print("| [Subtract]                               |")
        print("| [Multiply]                               |")
        print("| [Divide]                                 |")
        print("| [Factors]                                |")
        print("| [Exponent]                               |")
        print("| [Slope]                                  |")
        print("| [Decimal to Percent]                     |")
        print("| [Percent to Decimal]                     |")
        print("| [Exit]                                   |")
        print("|==========================================|")
        
        user_input = input("What Operation would you like to perform?: ").lower()
        if user_input == "add":
            addition()
        elif user_input == "subtract":
            subtraction()
        elif user_input == "multiply":
            multiply()
        elif user_input == "divide":
            divide()
        elif user_input == "exponent":
            power()
        elif user_input == "slope":
            slope()
        elif user_input == "decimal to percent":
            decimal_to_percent()
        elif user_input == "factors":
            factors()

        elif user_input == "exit":
            main_loop = 0
        else:
            print("Invalid Input, try again.")
            
        
        


main()
