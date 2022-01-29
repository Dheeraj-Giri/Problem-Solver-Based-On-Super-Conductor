import time


def ic():
    print('''\n1: Critical Current \t\t2: Critical Magnetic Field \t\t3: Radius \t\t4: Diameter''')

    find = int(input("What You Want To Find Out : "))
    try:
        match find:
            case 1:
                exp = "2*3.14*r*Hc"
                try:
                    Hc = float(eval(input("Enter the value of Hc: ")))
                    choice = input("Do you have radius (y/n)? ")
                    if choice == "y" or choice == "y":
                        r = float(eval(input("Enter the value of Radius in m : ")))
                    elif choice == "n" or choice == "N":
                        print("Since you have diameter value")
                        d = float(eval(input("Enter the diameter Value  in m : ")))
                        r = d / 2
                    print(f"Ic = {round(eval(exp), 3)} A")

                except Exception as e:
                    print("Error!! , Invalid Input!!!")

            case 2:
                exp = "Ic/(2*3.14*r)"
                try:
                    Ic = float(eval(input("Enter the value of Ic: ")))
                    choice = input("Do you have radius (y/n)? ")
                    if choice == "y" or choice == "y":
                        r = float(eval(input("Enter the value of Radius in m: ")))
                    elif choice == "n" or choice == "N":
                        print("Since you have diameter value")
                        d = float(eval(input("Enter the diameter Value in m: ")))
                        r = d / 2
                        print(r)
                    print(f"Hc = {round(eval(exp), 3)} A/m")

                except Exception as e:
                    print("Error!! , Invalid Input!!!")

            case 3:
                exp = "Ic/(2*3.14*Hc)"
                try:
                    Hc = float(eval(input("Enter the value of Hc: ")))
                    Ic = float(eval(input("Enter the value of Ic: ")))
                    print(f"R = {round(eval(exp), 3)} m")

                except Exception as e:
                    print("Error!! , Invalid Input!!!")

            case 4:
                exp = "2*r"
                try:
                    r = float(eval(input("Enter the value of Radius in m : ")))
                    result = eval(exp)
                    print("{:.3f}".format(result))

                except Exception as e:
                    print("Error!! , Invalid Input!!!")
    except Exception as e:
        print("Invalid Input !!!!")


def cmf():
    print(
        '''\n1) Hc : Critical Magnetic Field \t2) Ho : Magnetic Field at 0 Kelvin \t3) Tc : Critical/Transition Temprature \t4) T : Temprature of critical maganetic filed''')

    find = int(input("\nWhat You Want To Find Out :"))
    try:
        match find:
            case 1:
                exp = "Ho*(1-(T**2/Tc**2))"
                try:
                    Ho = float(eval(input("\nEnter the value of Ho in A/m: ")))
                    T = float(eval(input("Enter the value of T in Kelvin: ")))
                    Tc = float(eval(input("Enter the value of Tc in Kelvin: ")))
                    result = eval(exp)
                    print("Hc =", format(result, ".3f"), "A/m")
                except Exception as e:
                    print("Error!! Wrong Input")

            case 2:
                exp = "Hc/(1-(T**2/Tc**2))"
                try:
                    Hc = float(eval(input("\nEnter the value of Hc in A/m: ")))
                    T = float(eval(input("Enter the value of T in Kelvin: ")))
                    Tc = float(eval(input("Enter the value of Tc in Kelvin: ")))
                    result = eval(exp)
                    print("Ho =", format(result, ".3f"), "A/m")
                except Exception as e:
                    print("Error!! Wrong Input")

            case 3:
                exp = "T/((1-Hc/Ho)**0.5)"
                try:
                    T = float(eval(input("\nEnter the value of T in Kelvin: ")))
                    Ho = float(eval(input("Enter the value of Ho in A/m: ")))
                    Hc = float(eval(input("Enter the value of Hc in A/m: ")))
                    result = eval(exp)
                    print("Tc =", format(result, ".3f"), "K")
                except Exception as e:
                    print("Error!! Wrong Input")

            case 4:
                exp = "Tc*((1-Hc/Ho)**0.5)"
                try:
                    Tc = float(eval(input("\nEnter the value of Tc in Kelvin: ")))
                    Ho = float(eval(input("Enter the value of Ho in A/m: ")))
                    Hc = float(eval(input("Enter the value of Hc in A/m: ")))
                    result = eval(exp)
                    print("T =", format(result, ".3f"), "K")
                except Exception as e:
                    print("Error!! Wrong Input")

            case _:
                print("Error!!! INVALID INPUT!!!")
    except Exception as e:
        print("Invalid Input !!!!")


def MF():
    print(
        '''\n1) B: Magnetic field/induction \t\t\t2) H: intensity of magnetic field \n3) M: Magnetization of Material \t\t4) x: Magnetic susceptibily ''')

    find = int(input("What do you want : "))
    μo = 0.00000125663
    try:
        match find:
            case 1:
                try:
                    H = float(eval(input("\nEnter the vlue of H : ")))
                    choice = input("What do you have : \nM:Magnetization of Material \tx:Magnetic susceptibily \n")

                    if choice == "M" or choice == "m":
                        exp = "μo*(H+M)"
                        M = float(eval(input("Enter the vlue of M : ")))

                    elif choice == "X" or choice == "x":
                        exp = "μo*H*(1+x)"
                        x = float(eval(input("Enter the vlue of x: ")))

                    else:
                        print("Error !!, Invalid Input!!!")
                    print("B =", round(eval(exp), 3), "T")

                except Exception as f:
                    print("ERROR!!! , INVALID INPUT!!!")

            case 2:
                try:
                    B = float(eval(input("\nEnter the vlue of B : ")))
                    choice = input("What do you have : \nM:Magnetization of Material \tx:Magnetic susceptibily \n")

                    if choice == "M" or choice == "m":
                        exp = "B/μo-M"
                        M = float(eval(input("Enter the vlue of M : ")))

                    elif choice == "X" or choice == "x":
                        exp = "B/(μo*(1+x))"
                        x = float(eval(input("Enter the vlue of x: ")))

                    else:
                        print("Error !!, Invalid Input!!!")
                    print("H =", round(eval(exp), 3), "A/m")

                except Exception as f:
                    print("ERROR!!! , INVALID INPUT!!!")

            case 3:
                try:
                    H = float(eval(input("\nEnter the vlue of H : ")))
                    choice = input("What do you have : \nM:Magnetization of Material \tB:Magnetic Field \n")

                    if choice == "M" or choice == "m":
                        exp = "M/H"
                        M = float(eval(input("Enter the vlue of M : ")))

                    elif choice == "B" or choice == "b":
                        exp = "B/(μo*H)-1"
                        B = float(eval(input("Enter the vlue of B: ")))

                    else:
                        print("Error !!, Invalid Input!!!")
                    print("x =", round(eval(exp), 3), "Units")

                except Exception as f:
                    print("ERROR!!! , INVALID INPUT!!!")

            case 4:
                try:
                    H = float(eval(input("\nEnter the vlue of H : ")))
                    choice = input("What do you have : \nx:Magnetic Susceptibility \tB:Magnetic Field \n")

                    if choice == "x" or choice == "X":
                        exp = "H*x"
                        x = float(eval(input("Enter the vlue of x : ")))

                    elif choice == "B" or choice == "b":
                        exp = "B/μo-H"
                        B = float(eval(input("Enter the vlue of B: ")))

                    else:
                        print("Error !!, Invalid Input!!!")
                    print("M =", round(eval(exp), 3), "Am")

                except Exception as f:
                    print("ERROR!!! , INVALID INPUT!!!")

            case _:
                print("INVALID SELECTION!!!")
    except Exception as e:
        print("Invalid Input !!!!")


if __name__ == '__main__':

    name = input("\nEnter You Good Name : ")
    print(f"Hello, \"{name}\" Hope you are fine...")
    time.sleep(2)

    print("\n\t\t\t\t **** Welcome To Super-Conductor Problem Solver **** \n")

    time.sleep(1)
    print("\nHere we are going to solve the problem based on super-conductivity")


    while True:
        print("\nSelect problem type based on topic : ")
        choice = int(input(
            "\nWhat You Want to do? \n\t1) Critical Magnetic Field \t2) Critical Current \t3) Magnetic Field \t4) Exit \nEnter Your Choice:  "))
        try:
            match choice:
                case 1:
                    cmf()
                case 2:
                    ic()
                case 3:
                    MF()
                case 4:
                    print("Thank You For Using Problem Solver...")
                case _:
                    print("Invalid Input ")
                    ch = input("Do you want to try again (y/n)? ")

                    if ch in ["y", "Y"]:
                        continue
                    else:
                        print("Thank You")
                        exit()
        except Exception as f:
            print("Error!!! , Invalid Input!!!")

    input("Press Enter To Exit")