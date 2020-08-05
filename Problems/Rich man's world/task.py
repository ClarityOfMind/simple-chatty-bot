deposit = int(input())
min_deposit = 700000
interest = 7.1
saves = 0
years = 0

while deposit < min_deposit:
    deposit += (deposit * interest) / 100
    years += 1
print(years)
