num = input("Enter any number:")
while not num.isdigit():
    print("Please do not enter other characters.")
    num = input("Enter number again:")

num = int(num)
if num % 2 == 0:
    print(f"{num} is an even number ")
else:
    print(f"{num} is an odd number ")