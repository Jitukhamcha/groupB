def game(n):
    if n%3==0 and n%5==0:
        return("FizzBuzz")
    elif n%5==0:
        return("Buzz")
    elif n%3==0:
        return("Fizz")
    else:
        return n

num=int(input("enter number for game"))
print(game(num))

