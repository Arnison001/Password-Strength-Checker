# 20_password_strength_checker.py
# Checks how strong a password is based on several rules.
# Demonstrates combining multiple conditions with "and"/"or",
# along with a for loop to inspect each character individually.

password = input("Enter a password to check: ")

has_digit = False
has_upper = False
has_lower = False

# Loop through every character in the password one at a time.
for char in password:
    if char.isdigit():
        has_digit = True
    elif char.isupper():
        has_upper = True
    elif char.islower():
        has_lower = True

is_long_enough = len(password) >= 8

print("\n--- Password Check ---")
print("At least 8 characters:", is_long_enough)
print("Contains a number:", has_digit)
print("Contains an uppercase letter:", has_upper)
print("Contains a lowercase letter:", has_lower)

# The password is only considered "strong" if ALL conditions are True.
if is_long_enough and has_digit and has_upper and has_lower:
    print("\nPassword strength: STRONG")
elif is_long_enough and (has_digit or has_upper):
    # Meets length and at least one extra rule - a reasonable middle ground.
    print("\nPassword strength: MEDIUM")
else:
    print("\nPassword strength: WEAK")
