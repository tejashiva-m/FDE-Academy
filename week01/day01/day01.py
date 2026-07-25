name = input("What is your name? ")

while True:
    try:
        years_of_experience = int(input("How many years of experience do you have? "))
        break
    except ValueError:
        print("Please enter a valid number of years.")

favorite_cloud_provider = input("What is your favorite cloud provider? ")

print(f"\nWelcome {name}!")
print()
print(f"Experience : {years_of_experience} years")
print()
print(f"Primary Cloud : {favorite_cloud_provider}")
print()

if favorite_cloud_provider == "Azure":
    print("Azure is a great platform for enterprise AI.")
elif favorite_cloud_provider == "AWS":
    print("AWS powers many cloud-native applications.")
else:
    print("Great choice! Every cloud teaches valuable skills.")

print()
print("Your journey to becoming a Forward Deployed Engineer starts today!")
