emails = ["ali@gmail.com", "vali@yahoo.com", "sami@gmail.com", "bek@outlook.com"]

result = list(filter( lambda a: a.endswith("@gmail.com"),emails))

print(result)