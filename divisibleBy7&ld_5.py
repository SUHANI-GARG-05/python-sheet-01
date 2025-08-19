num = int(input("Enter a number: "))

if (num % 7 == 0 or num % 10 == 5):
    print("Yes, divisible by 7 or last digit is 5")
else:
    print("No, it doesn't meet either condition")
