guess = int(input("input 1~10 int number: "))
secret = 8
print("secret type is",type(secret))
print("guess type is:",type(guess))
print("============int guess=============")
guess=int(guess)
print("guess type is:",type(guess))

while True:
    
    if guess < secret:
        print("too low")
        guess = int(input("input 1~10 int number: "))
    elif guess > secret:
        print("too high")
        guess = int(input("input 1~10 int number: "))
    elif guess == secret:
        break

print("yes! yor are right")