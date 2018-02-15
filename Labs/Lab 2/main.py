# Question 1
print("\nQuestion 1")
L = ['A','B','C','D','E']
numberList = range(0,len(L))
results = list(zip(L,numberList))
print(results)

# Question 2
print("\nQuestion 2")
dlist = [{'James':'Sean', 'director':'Terence'}, {'James':'Roger',
         'director':'Lewis'}, {'James':'Pierce', 'director':'Roger'}]
k = 'James'
b = [d[k] for d in dlist]
print(b)

# Question 3
print("\nQuestion 3")
keys = [i for i in range(10)]
values = [x**2 for x in range(100)]
dict = {keys[i]: values[i] for i in range(len(keys))}
print(dict)

# Question 4
print("\nQuestion 4")
id2salary = {0: 1000.0, 3: 990, 1: 1200.50}
names = ['Larry', 'Curly', '', 'Moe']
name2salary = {names[i]: id2salary[i] for i in range(0, len(names)) if i in id2salary}
print(name2salary)