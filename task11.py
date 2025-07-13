nums = list(range(1, 21))

juft_raqam= list(filter(
    lambda n: n % 2 == 0,
    nums
))
kvadrat_raqam = list(map(
    lambda a: a **2,
    juft_raqam
))
print("juft sonlar:", juft_raqam)
print("kvadrat_sonlar:", kvadrat_raqam)
