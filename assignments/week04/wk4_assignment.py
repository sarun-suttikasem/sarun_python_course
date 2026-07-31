name = input("Enter your name: ")
letters = list(name)
counter = 0

for char in letters:
    if char == 'a' or char == 'A':
        counter = counter + 1
    elif char == 'e' or char == 'E':
        counter = counter + 1
    elif char == 'i' or char == 'I':
        counter = counter + 1
    elif char == 'o' or char == 'O':
        counter = counter + 1
    elif char == 'u' or char == 'U':
        counter = counter + 1

print(f"You have {counter} vowels")

