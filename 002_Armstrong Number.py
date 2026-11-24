# 1134 — Armstrong Number
# Problem statement:
# Given a positive integer n,return true if and only if it is an Armstrong number.A k‑digit number is
# an Armstrong number if the sum of the k‑th powers of its digits equals the number itself.
# Examples:
# 153 → true because it has 3 digits and 1**3 + 5**3 + 3**3 = 1+125+27 = 153
# 123 → false because 1**3 + 2**3 + 3**3 = 36 != 123
num = int(input())
digits = len(str(num))
if num<0:
    print(False)
else:
    temp = num
    res = 0
    while temp:
        res += (temp%10)**digits
        temp //= 10
    print(True if num==res else False)
