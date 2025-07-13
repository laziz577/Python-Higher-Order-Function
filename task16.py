data = [123, "apple", "banana", "cat", 456, "mango", "elephant"]
text = list(filter(lambda a: isinstance(a,str) and len(a) > 5,data))
print(text)