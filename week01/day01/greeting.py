#Enter Name
#Enter Country
#Enter Favorite Programming Language

#========================================

# Welcome Teja!
# Country : India
# Favorite Language : Python
# Have a wonderful coding journey!

# ========================================

# If the language is Python, print a special encouraging message.
# If it's something else, print a different positive message.

name = input("Enter Name ")
country = input("Enter Country ")
favorite_language = input("Enter Favorite Programming Language ").strip().lower()

print(f"{'=' * 32}")
print()
print(f"Welcome {name}!")
print(f"Country : {country}")
print(f"Favorite Language : {favorite_language}")

if favorite_language == "python":
    print("Python is a versatile language! Keep up the great work!")
else:
    print(f"{favorite_language} is a great language! Keep learning and coding!")

print(f"\n{'=' * 32}")