**Question 1**

1.	Assign to L the list consisting of the first five letters ['A','B','C','D','E']. Next, use L in an expression whose value is [(0, ’A’), (1, ’B’), (2, ’C’), (3, ’D’), (4, ’E’)].  Your expression should use a range and a zip, but should not use a comprehension. 

```python
L = ['A','B','C','D','E']
numberList = range(0,len(L))
results = list(zip(L,numberList))
print(results)
```
