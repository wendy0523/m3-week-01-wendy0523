def change_case(input_str, case):
    if case == "upper":
        return input_str.upper()
    elif case == "lower":
        return input_str.lower()
    else:
        return "請輸入upper或lower"
