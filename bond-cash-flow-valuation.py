from tvom import generate_bond_cash_flow, calculate_bond_valuation

face_value = 1000
coupon_rate = 0.05
years = 2
discount_rate = 0.03
frequency = 2

print(generate_bond_cash_flow(face_value, coupon_rate, years))
print()
print(calculate_bond_valuation(face_value, coupon_rate, years, discount_rate, frequency))

