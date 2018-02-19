**Question 1**

Assign to L the list consisting of the first five letters ['A','B','C','D','E']. Next, use L in an expression whose value is [(0, ’A’), (1, ’B’), (2, ’C’), (3, ’D’), (4, ’E’)].  Your expression should use a range and a zip, but should not use a comprehension. 

```python
L = ['A','B','C','D','E']
numberList = range(0,len(L))
results = list(zip(L,numberList))
print(results)
```
**Question 2**

Suppose dlist is a list of dictionaries and k is a key that appears in all the dictionaries in dlist. Write a comprehension that evaluates to the list whose ith element is the value corresponding to key k in the ith dictionary in dlist. Test your comprehension with some data. comprehension. Here are some example data: 

dlist = [{'James':'Sean', 'director':'Terence'}, {'James':'Roger', 'director':'Lewis'}, {'James':'Pierce', 'director':'Roger'}] 

k = 'James'

```python
dlist = [{'James':'Sean', 'director':'Terence'}, {'James':'Roger','director':'Lewis'}, {'James':'Pierce', 'director':'Roger'}]
k = 'James'
b = [d[k] for d in dlist]
print(b)
```
**Question 3**

Using range, write a comprehension whose value is a dictionary. The keys should be the integers from 0 to 99 and the value corresponding to a key should be the square of the key.

```python
keys = [i for i in range(10)]
values = [x**2 for x in range(100)]
dict = {keys[i]: values[i] for i in range(len(keys))}
print(dict)
```
**Question 4**

Suppose d is a dictionary that maps some employee IDs (a subset of the integers from 0 to n - 1) to salaries. Suppose L is an n-element list whose ith element is the name of employee number i. Your goal is to write a comprehension whose value is a dictionary mapping employee names to salaries. You can assume that employee names are distinct. However, not every employee ID is represented in d. 
Test your comprehension with the following data: 

id2salary = {0:1000.0, 3:990, 1:1200.50} 

names = ['Larry', 'Curly', ' ', 'Moe']


```python
id2salary = {0: 1000.0, 3: 990, 1: 1200.50}
names = ['Larry', 'Curly', '', 'Moe']
name2salary = {names[i]: id2salary[i] for i in range(0, len(names)) if i in id2salary}
print(name2salary)
```
