# Save the input in this variable
ticket = int(input())

# Add up the digits for each half
half1 = (ticket // 100000) + ((ticket % 100000) // 10000) + ((ticket % 10000) // 1000)
half2 = ((ticket % 1000) // 100) + ((ticket % 100) // 10) + (ticket % 10)

# Thanks to you, this code will work
if half1 == half2:
    print("Lucky")
else:
    print("Ordinary")


