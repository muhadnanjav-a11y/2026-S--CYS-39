def square(n):
    print(n * n)

num = int(input("Enter a number: "))
num1 = int(input("Enter another number: "))
square(num)

sum = lambda x, y: x + y
print(sum(num, num1))
lambda_square = lambda x: x * x
print(lambda_square(num))

num_list = [1, 2, 3, 4, 5]
squared_list = list(map(lambda x: x * x, num_list))
print(squared_list)

