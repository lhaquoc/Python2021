def input_params():
    initial_w = float(input("w:"))
    delta_w = float(input("delta_w:"))
    years = int(input("years:"))
    return initial_w, delta_w, years

def calculation(w1, delta_w, years):
    for i in range(1,years):
        w = w1 + delta_w*i
        print(f"Nam thu {i}: {w}")
