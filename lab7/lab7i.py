# Global variable
schoolName = "Seneca"

def function1():
    # Local variable
    schoolName = "SICT"
    print(f"print() in function1 on schoolName: {schoolName}")

def function2():
    # Local variable
    schoolName = "SSDO"
    print(f"print() in function2 on schoolName: {schoolName}")

def main():
    global schoolName
    print(f"print() in main on schoolName: {schoolName}")
    function1()  # Call function1, which has its own local variable
    schoolName = "SICT"  # Change the global variable to match the output
    print(f"print() in main on schoolName: {schoolName}")  # Now using the modified global variable
    function2()  # Call function2, which has its own local variable
    schoolName = "SSDO"  # Change the global variable again to match the output
    print(f"print() in main on schoolName: {schoolName}")  # Now using the modified global variable
    
if __name__ == "__main__":
    main()
