# Question:
# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
# Suppose the following input is supplied to the program:
# 9
# Then, the output should be:
# 11106
# ----------------------------------------------------------------

# N*a=Na, for example  a="23", 2*a="2323",3*a="232323"
a = input()
total = int(a) + int(2*a) + int(3*a) + int(4*a)
print(total