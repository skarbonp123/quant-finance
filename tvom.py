import math

# ---------------- BASIC PV AND FV ----------------

def calculate_present_value(fv: float, r: float, n: int) -> float:
    """
    Calculates the present value of a future amount using discrete compounding.
    Formula: PV = FV / (1 + r)^n
    """
    return fv / (1 + r) ** n


def calculate_future_value(pv: float, r: float, n: int) -> float:
    """
    Calculates the future value of a present amount using discrete compounding.
    Formula: FV = PV * (1 + r)^n
    """
    return pv * (1 + r) ** n


# ----------- CONTINUOUS COMPOUNDING -----------

def calculate_continuous_comp_fv(pv: float, r: float, t: int) -> float:
    """
    Calculates future value with continuous compounding.
    FV = PV * e^(rt)
    """
    return pv * math.exp(r * t)


def calculate_continuous_comp_pv(fv: float, r: float, t: int) -> float:
    """
    Calculates present value with continuous compounding.
    PV = FV * e^(-rt)
    """
    return fv * math.exp(-r * t)


# ---------------- ANNUITIES ----------------

def calculate_future_ordinary_annuity(C: float, r: float, n: int) -> float:
    """
    Calculates future value of an ordinary annuity.
    Payments are made at the end of each period.
    Formula: FV = C * [((1 + r)^n - 1) / r]
    """
    return C * (((1 + r) ** n - 1) / r)


def calculate_present_ordinary_annuity(C: float, r: float, n: int) -> float:
    """
    Calculates present value of an ordinary annuity.
    Payments are made at the end of each period.
    Formula: PV = C * [(1 - (1 + r)^(-n)) / r]
    """
    return C * ((1 - (1 + r) ** (-n)) / r)


def calculate_future_annuity_due(C: float, r: float, n: int) -> float:
    """
    Calculates future value of an annuity due.
    Payments are made at the beginning of each period.
    Formula: FV = FV of ordinary annuity * (1 + r)
    """
    return  calculate_future_ordinary_annuity(C, r, n) * (1 + r)


def calculate_present_annuity_due(C: float, r: float, n: int) -> float:
    """
    Calculates present value of an annuity due.
    Payments are made at the beginning of each period.
    Formula: PV = PV of ordinary annuity * (1 + r)
    """
    return calculate_present_ordinary_annuity(C, r, n) * (1 + r)


# --------- DISCOUNTED CASH FLOW ---------

def discounted_cash_flow(cash_flows: list[float], r: float) -> list:
    """
    Calculates the present value of a series of future cash flows using discrete discounting.
    Returns:
        - List of individual discounted values per period
        - Total present value (sum of all discounted flows)
    """
    pv_values = []
    pv_total = 0
    t = 1

    for cf in cash_flows:
        current = cf / ((1 + r) ** t)
        pv_total += current
        pv_values.append(current)
        t += 1

    return [pv_values, pv_total]


# --------- BOND CASH FLOW AND VALUATION ---------

def generate_bond_cash_flow(face_value: float, coupon_rate: float, years: int, frequency: int = 1) -> list[float]:
    """ 
    Generates the list of cash flows for a coupon bond.
    
    face_value: Amount repaid at maturity
    coupon_rate: Annual coupon rate (e.g., 0.05 for 5%)
    years: Total years to maturity
    frequency: How often coupons are paid (default: 1 for annual)
    
    Returns: List of cash flows in order
    """
    cash_flows = []
    coupon_payment = (face_value * coupon_rate) / frequency
    
    for i in range(0, (frequency * years)):
        cash_flows.append(coupon_payment)

    cash_flows[-1] += face_value

    return cash_flows


def calculate_bond_valuation(face_value: float, coupon_rate: float, years: int, discount_rate: float, frequency: int = 1) -> float:
    """
    Calculates the fair value of a bond using its cash flows and a given discount rate.
    """
    cash_flows = generate_bond_cash_flow(face_value, coupon_rate, years, frequency)
    _, pv_total = discounted_cash_flow(cash_flows, discount_rate / frequency)
    
    return pv_total


# --------------- YIELD TO MATURITY --------------

def calculate_bond_valuation_from_ytm(face_value: float, coupon_rate: float, years: int, ytm: float, frequency: int = 1) -> float:
    """
    Calculates the fair value of a bond using its cash flows and yield to maturity as the discount rate. (Identical to the method above)
    """
    cash_flows = generate_bond_cash_flow(face_value, coupon_rate, years, frequency)
    _, pv_total = discounted_cash_flow(cash_flows, ytm / frequency)
    
    return pv_total


def approximate_ytm(face_value: float, coupon_rate: float, years: int, price: float, frequency: int = 1, tolerance: float = 1e-6, max_iterations: int = 1000) -> float:
    """
    Approximates the Yield to Maturity (YTM) given market price and bond details.
    """
    low = 0.0001
    high = 1.0
    iterations = 0

    while (iterations < max_iterations):
        
        ytm = (high + low ) / 2
        ytm_price = calculate_bond_valuation_from_ytm(face_value, coupon_rate, years, ytm, frequency)
        
        if (abs(ytm_price - price) < tolerance):
            return ytm
        
        if (ytm_price < price):
            high = ytm
        else:
            low = ytm
        
        iterations += 1

    return ytm