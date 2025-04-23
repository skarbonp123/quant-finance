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


# ----------- ANNUITIES -----------

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

