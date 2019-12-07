Principal = 100000
Annual_interest_rate = 0.02
year = 10
interest = Principal * (Annual_interest_rate * year)
print("單利率利息：")
print(interest)

total_money = Principal * (1 + Annual_interest_rate)** year
print("複利本金和：")
print(int(total_money))
print(round(total_money))