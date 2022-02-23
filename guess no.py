import random
name = input("Enter your name: ")
print("good luck", name, "guess the no. between the range you decided")
r1 = int(input("enter the range starting point:"))
r2 = int(input("enter the range ending point:"))
random_no = random.randint(r1, r2)
total = 0

    
for i in range(r2):
    guesed = int(input("guess the no.:"))
    if guesed == random_no:
       total += 1
       print("correct, your total guess = ", total)
       break
    if guesed > random_no:
       print("your number is too high")
       total += 1
    if guesed < random_no:
       print("your number is too low")
       total += 1


    


