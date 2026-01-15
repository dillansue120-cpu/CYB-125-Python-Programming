#import the random library so we can use its functions
import random
num = random.randint(1, 10)

# generate a random number between
num = random.randint(1, 1000000)
even = num % 2

if even == 0:
    print("Number is even")
elif even == 1:
     print("Number is odd")

print("The number is", num)
#if any number divisible by 2 is even and will have a remainder of 0
#any number not divisible by 2 is odd and will have a remainder of 1
remainder = num % 2
# the stataement ( reminder == 1) resolves to the TRUE (1) OR false (0) so this is redundant
#we can simplify to just if remainder to justify if remainder because it will also resolve to either 1 or 0 ( based on our num % 2 logic above)

# if num == 1:
if remainder:
       print("Number is odd")
else:
    print("Number is even")
print("The number is", num)
#     print("number is odd")
# elif num == 2:
#     print("Number is even")
# elif num == 3:
#      print("Number is odd")
# elif number == 4:
#      print("Number is even")
# elif num == 5:
#      print("Number is odd")