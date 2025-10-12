import sys

upperAlpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowerAlpha = 'abcdefghijklmnopqrstuvwxyz'
Numbers = '123456789'
SpecialChar = '!@#$%&*'

def Validate(Password):
    if len(Password) >= 8:
        print('Rule 1: Length >= 8 ✔')
        if any(items in upperAlpha for items in Password):
            print('Rule 2: Contains uppercase ✔')
            if any(items in lowerAlpha for items in Password):
                print('Rule 3: Contains lowercase ✔')
                if any(items in Numbers for items in Password):
                    print('Rule 4: Contains digit ✔')
                    if any(items in SpecialChar for items in Password):
                        print('Rule 5: Contains special character ✔')
                        print('Strong Password')
                    else:
                        print('Moderate Password')
                else:
                    print('Moderate Password')
            else:
                print('Weak password')
        else:
            print('Weak Password')
    else:
        print('Weak Password')

Password = input('Enter your password: ')
Validate(Password)
Input = input('Would you like to test another password? ')
if Input.lower() == 'no':
    sys.exit()
elif Input.lower() == 'yes':
    Password = input('Enter your password: ')
    Validate(Password)

# ideal code:

# import sys

# # Define valid character sets
# UPPERCASE = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# LOWERCASE = 'abcdefghijklmnopqrstuvwxyz'
# NUMBERS = '0123456789'
# SPECIALS = '!@#$%&*'

# def validate_password(password):
#     """Validates a password and reports which rules are met."""

#     rules = {
#         "Length >= 8": len(password) >= 8,
#         "Contains uppercase": any(ch in UPPERCASE for ch in password),
#         "Contains lowercase": any(ch in LOWERCASE for ch in password),
#         "Contains digit": any(ch in NUMBERS for ch in password),
#         "Contains special character": any(ch in SPECIALS for ch in password)
#     }

#     # Output each rule and whether it passed
#     print("\nPassword Validation Results:")
#     for rule, passed in rules.items():
#         print(f"{rule}: {'✔' if passed else '✖'}")

#     # Determine strength
#     passed_rules = sum(rules.values())
#     if passed_rules == 5:
#         strength = "Strong Password"
#     elif passed_rules >= 3:
#         strength = "Moderate Password"
#     else:
#         strength = "Weak Password"

#     print(f"\nOverall Result: {strength}\n")
#     return strength


# # Main Program Loop
# while True:
#     password = input("Enter your password: ")
#     validate_password(password)

#     again = input("Would you like to test another password? (yes/no): ").strip().lower()
#     if again == "no":
#         print("Exiting program...")
#         sys.exit()