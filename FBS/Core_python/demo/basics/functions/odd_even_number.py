def even_oddNumber(num):
    if(num % 2 == 0):
        print(f"{num} is even number")
    else:
        print(f"{num} is odd number")

num = int(input("enter the number: "))

even_oddNumber(num)