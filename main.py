import string

password = input("Enter your password: ")

uppercase = any([1 if c in string.ascii_uppercase else 0 for c in password])
lowercase = any([1 if c in string.ascii_lowercase else 0 for c in password])
special = any([1 if c in string.punctuation else 0 for c in password])
digit = any([1 if c in string.digits else 0 for c in password])

characters = [uppercase, lowercase, special, digit]

score = 0

length = len(password)

with open("common.txt", "r") as f:
    common = f.read().splitlines()

if password in common:
    print("Password found in a common password list. Score: 0/7")
    exit()
if length > 8:
    score += 1
if length > 10:
    score += 1
if length > 12:
    score += 1
if length > 15:
    score += 1

print(f"Password length is {str(length)},  adding {str(score)} points.")

if sum(characters) > 1:
    score += 1
if sum(characters) > 2:
    score += 1
if sum(characters) > 3:
    score += 1

print(f"Password has {str(sum(characters))} different characters, adding {str(sum(characters) - 1)} points.")

if score < 4:
    print(f"The password is quite weak! Score: {str(score)}")
elif score == 4:
    print(f"The password is ok! Score: {str(score)}")
elif score > 4 and score < 6:
    print(f"The password is good! Score: {str(score)}")
elif score >= 6:
    print(f"The password is strong! Score: {str(score)}")
