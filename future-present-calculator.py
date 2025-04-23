from tvom import calculate_present_value, calculate_future_value


def main():
    print("Choose calculation:")
    print("1. Future Value")
    print("2. Present Value")

    choice = int(input("Enter your choice (1 or 2): "))

    r = float(input("Enter annual interest rate (in %): ")) / 100
    n = int(input("Enter number of years (n): "))
    
    if (choice == 1):
        pv = float(input("Enter Present Value ($): "))
        fv = calculate_future_value(pv, r, n)
        print(f"Future Value = ${fv:.2f}")
    elif (choice == 2):
        fv = float(input("Enter Future Value ($): "))
        pv = calculate_present_value(fv, r, n)
        print(f"Present Value = ${pv:.2f}")


if __name__ == "__main__":
    main()