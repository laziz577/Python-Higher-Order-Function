sentence = "Functional programming in Python is very powerful and elegant"

task = sentence.split()

len_tasks = sorted(task, key = lambda a: len(a), reverse = True)[:3]
print(len_tasks)