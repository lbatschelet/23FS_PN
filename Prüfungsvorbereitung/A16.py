# (a)
num = int(input("Geben sie eine Zahle ein: "))
for i in range(0, num + 1, 2):
    print(i)

# (b)
num = int(input("Geben Sie eine Zahl ein: "))
lst = list(range(1, num + 1))
print(lst)

# (c)
def is_in_list(lst, value):
    if value not in lst:
        lst.append(value)

is_in_list(lst, 15)
print(lst)