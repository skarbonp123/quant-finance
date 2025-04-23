from tvom import calculate_continuous_comp_fv, calculate_continuous_comp_pv

pv_input = 1000
r = 0.07
t = 5

fv = calculate_continuous_comp_fv(pv_input, r, t)
print(f"Future Value (continuous): ${fv:.2f}")

fv_input = 1419.07
pv = calculate_continuous_comp_pv(fv_input, r, t)
print(f"Present Value (continuous) ${pv:.2f}")