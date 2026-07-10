print("2. Time Converter:")
print("   - Ask user for seconds")
print("   - Convert to hours, minutes, and remaining seconds")
print("   - Example: 3661 seconds = 1 hour, 1 minute, 1 second")
print()

sec = int(input("Enter your seconds: "))

hour = sec // 3600
sec_remain = sec % 3600
minute = sec_remain // 60
sec_remain = sec % 60

print(f"{sec} seconds = {hour} hours = {minute} = minutes = {sec_remain} = second")
