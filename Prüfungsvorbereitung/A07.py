def fizzbuzz(value):
    if value % 3 == 0 and value % 5 != 0:
        return "Fizz"
    elif value % 5 == 0 and value % 3 != 0:
        return "Buzz"
    elif value % 3 == 0 and value % 5 == 0:
        return "FizzBuzz"
    else:
        return value
    
for i in range(1, 101):
    print(i, fizzbuzz(i), sep=" -> ")
    