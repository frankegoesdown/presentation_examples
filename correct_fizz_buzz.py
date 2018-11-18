
for num in range(1, 101):
    print("fizz"*(num % 3 == 0)+"buzz"*(num % 5 == 0) or num)
