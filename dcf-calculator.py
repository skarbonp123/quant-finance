from tvom import discounted_cash_flow

def main():
    cash_flows = [200, 300, 400, 500]
    r = 0.1


    dcf_list, dcf_value = discounted_cash_flow(cash_flows, r)

    for i in range(0, len(dcf_list)):
        print(f"Value of Year {i + 1} cash flow: ${dcf_list[i]:.2f}")
    print(f"Total DCF Value: ${dcf_value:.2f}")

if __name__ == "__main__":
    main()