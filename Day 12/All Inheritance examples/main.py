import single_inheritance
import multilevel_inheritance
import multiple_inheritance
import hierarchical_inheritance
import hybrid_inheritance

ch = 0

while ch != 6:

    print("\n-------------------------------------------------------")
    print("       PYTHON INHERITANCE DEMONSTRATION PROJECT")
    print("-------------------------------------------------------")
    print("1. Single Inheritance")
    print("2. Multilevel Inheritance")
    print("3. Multiple Inheritance")
    print("4. Hierarchical Inheritance")
    print("5. Hybrid Inheritance")
    print("6. Exit")
    print("-------------------------------------------------------")

    ch = int(input("Enter your choice (1-6): "))

    match ch:

        case 1:
            print("\n=======================================================")
            print("SINGLE INHERITANCE |  Appliance -> WashingMachine")
            print("=======================================================")
            print("     Appliance")
            print("        |")
            print("    WashingMachine")
            print("-------------------------------------------------------")

            single_inheritance.run_demo()

        case 2:
            print("\n=======================================================")
            print("MULTILEVEL INHERITANCE | Animal -> Mammal -> Dog")
            print("=======================================================")
            print("    Animal")
            print("       |")
            print("    Mammal")
            print("       |")
            print("      Dog")
            print("-------------------------------------------------------")

            multilevel_inheritance.run_demo()

        case 3:
            print("\n=======================================================")
            print("MULTIPLE INHERITANCE | Camera + Phone -> Smartphone")
            print("=======================================================")
            print("  Camera     Phone")
            print("      \\     /")
            print("    Smartphone")
            print("-------------------------------------------------------")

            multiple_inheritance.run_demo()

        case 4:
            print("\n=======================================================")
            print("HIERARCHICAL INHERITANCE | Shape -> Circle, Rectangle, Triangle")
            print("=======================================================")
            print("            Shape")
            print("     _________|_________")
            print("    |         |         |")
            print(" Circle  Rectangle  Triangle")
            print("-------------------------------------------------------")

            hierarchical_inheritance.run_demo()

        case 5:
            print("\n=======================================================")
            print("HYBRID INHERITANCE | Person -> Student/Teacher -> Teaching Assistant")
            print("=======================================================")
            print("          Person")
            print("       _____|_____")
            print("      |           |")
            print("   Student     Teacher")
            print("      |___________|")
            print("            |")
            print("   TeachingAssistant")
            print("-------------------------------------------------------")

            hybrid_inheritance.run_demo()

        case 6:
            print("\nExiting the program. Goodbye!")

        case _:
            print("\nInvalid Choice! Please enter a number between 1 and 6.")

    if ch != 6:
        input("\nPress Enter to continue...")