# ===========================
# 7. ITERATING AND COUNTING
# ===========================

print("\n=== ITERATING THROUGH STRING ===")
count = 0

text = input("insert text: ")
char = input("character to find: ")

for letter in text:
    if letter == char:
        count += 1
print(f"{count} letters '{char}' found in '{text}'")

#PASSWORD

PW = input("Enter Password: ")

if len(PW) >= 8 and PW.isalnum() == False:
    print("Your Password is strong")

else:
    print("Your Password is not strong")

