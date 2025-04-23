import os
from tvom import calculate_future_ordinary_annuity, calculcate_present_ordinary_annuity
from tvom import calculate_future_annuity_due, calculate_present_annuity_due 


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def main():

    lst = ["Ordinary Annuity", "Annuity Due", "Future", "Present"]

    clear_terminal()

    print("Choose Annuity: ")
    print("1. Ordinary Annuity")
    print("2. Annuity Due")
    annuity = int(input("Enter choice (1 or 2): "))

    clear_terminal()
    print(f"Annuity picked: {lst[-1 + annuity]}")
    print("")
    print("Choose calculation: ")
    print("1. Future Value")
    print("2. Present Value")
    p_or_f_value = int(input("Enter choice (1 or 2):"))

    clear_terminal()
    print(f"Annuity picked: {lst[-1 + annuity]}")
    print(f"Calculation picked: {lst[1 + p_or_f_value]} value")
    print("")
    C = int(input("Enter the amount deposited per year (C): "))
    r = float(input("Enter interest rate (in %): ")) / 100
    n = int(input("Enter number of years (n): "))
    


    if (annuity == 1):
        if (p_or_f_value == 1):
            value = calculate_future_ordinary_annuity(C, r, n)
        elif (p_or_f_value == 2):
            value = calculcate_present_ordinary_annuity(C, r, n)
    elif (annuity == 2):
        if (p_or_f_value == 1):
            value = calculate_future_annuity_due(C, r, n)
        elif (p_or_f_value == 2):
            value = calculate_present_annuity_due(C, r, n)
    else:
        print("Wrong input")


    clear_terminal()
    print(f"Annuity picked: {lst[-1 + annuity]}")
    print(f"Calculation picked: {lst[1 + p_or_f_value]} value")
    print(f"Deposit every year: ${C}")
    print(f"Interest Rate: {r:.2f}")
    print(f"Number of years: {n}")
    print("")
    print(f"{lst[1 + p_or_f_value]} Value = ${value:.2f}")


if __name__ == "__main__":
    main()