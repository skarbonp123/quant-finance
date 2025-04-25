from tvom import generate_bond_cash_flow, calculate_bond_valuation
from tvom import calculate_bond_valuation_from_ytm, approximate_ytm

face_value = 1000
coupon_rate = 0.05
years = 2
discount_rate = 0.03
frequency = 2

# print(generate_bond_cash_flow(face_value, coupon_rate, years))
print()
# print(calculate_bond_valuation(face_value, coupon_rate, years, discount_rate, frequency))


face_value = 1000
coupon_rate = 0.04
years = 10
price = 1000

ytm = approximate_ytm(face_value, coupon_rate, years, price)
print(f"Approximate YTM: {ytm * 100 :.3f}%")

