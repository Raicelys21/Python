def parens_pairs(n):
    parens_checker(n, 0, "")

def parens_checker(l, r, value_to_print):
    if l == 0 and r == 0:
        print(value_to_print)
    if l > 0:
        parens_checker(l - 1, r + 1, value_to_print + "(")
    if r > l:
        parens_checker(l, r - 1, value_to_print + ")")

parens_pairs(2)