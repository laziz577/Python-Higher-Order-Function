prices = ["$120", "$340", "$50", "$90"]
result = map(
    lambda num:float(num.replace("$"," ")),
    prices
)

print(list(result))

