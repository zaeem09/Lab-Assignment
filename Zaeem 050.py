Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
academic_tuple=('name','father name','red number','CNIC number','CGPA')
Zaeem_registration=('SP24-BBA-050')
fruit_tuple=('apple','banana','cherry')
numbers_tuple=(2,4,6,8,9)
mixed_tuple=(1,'apple',5,'true',4.8)
single_item_tuple=(9,)
fruit=('apple','banana','cherry')
print(fruits_tuple[0])
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    print(fruits_tuple[0])
NameError: name 'fruits_tuple' is not defined. Did you mean: 'fruit_tuple'?
print(fruit_tuple[0])
apple
print(fruit_tuple[1])
banana
print(fruit_tuple[-1])
cherry
print(fruit_tuple[-2])
banana
>>> fruit_tuple=('apple','banana','cherry')
>>> fruit_tuple[0]='blueberry'
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    fruit_tuple[0]='blueberry'
TypeError: 'tuple' object does not support item assignment
>>> 
>>> # Concatenation
>>> tuple1=(1,2,3)
>>> tuple2=(4,5,6)
>>> combined_tuple=tuple1+tuple2
>>> print(combined_tuple)
(1, 2, 3, 4, 5, 6)
>>> tuple1=('hello',)
>>> repeated_tuple=tuple1*3
>>> print(repeated_tuple)
('hello', 'hello', 'hello')
>>> 
>>> # Tuple Slicing
>>> numbers = (0, 1, 2, 3, 4, 5, 6)
>>> print(numbers[1:4])
(1, 2, 3)
>>> print(numbers[:3])
(0, 1, 2)
>>> print(numbers[4:])
(4, 5, 6)
>>> 
>>> # Tuple Methods
>>> fruits_tuple = ('apple', 'banana', 'cherry', 'apple')
>>> print(fruits_tuple.count('apple'))
2
>>> print(fruits.index('cherry'))
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    print(fruits.index('cherry'))
NameError: name 'fruits' is not defined. Did you mean: 'fruit'?
>>> print(fruit.index('cherry'))
2
>>> tuple1=('cherry')
>>> print(tuple1.count('r'))
2
>>> a_count=sum(fruit.count('a') for fruit in fruit)
>>> print("fruit'a':",a_count)
fruit'a': 4
