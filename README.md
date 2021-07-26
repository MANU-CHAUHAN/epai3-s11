# EPAi S11



![](https://miro.medium.com/max/2000/1*dWd3B7F8zvMPERg2LpNgaA.jpeg)


----

### Link for notebook with repo cloned and code usage:

[Deepnote](https://deepnote.com/project/EPAI30ManuShared-lHtlJAM8Srqe0N5wrZgiWQ/%2Fs11.ipynb)

----

### Few points to remember:

- Lists, strings, and tuples are sequences. Dictionaries, sets, and many other *iterables* are not *sequences*.

- Iterators have exactly one job: return the “next” item in our iterable

- *Iterators are also Iterables*: You can pass iterators to the built-in `iter`function to get themselves back. That means that iterators are also iterables.

- Sequences are a very common type of iterable. Lists, tuples, and strings are all sequences.

- Sequences are iterables that have a specific set of features. They can be indexed starting from `0` and ending at one less than the length of the sequence, they have a length, and they can be sliced. Lists, tuples, strings, and *all other* sequences work this way.

- Lots of things in Python are iterables, but not all iterables are sequences. Sets, dictionaries, files, and generators are all iterables but none of these things are sequences.

  

  > Note: have included lazy property evaluation already here and in code



<u>Iterables:</u>

1. Can be passed to the `iter` function to get an iterator for them.
2. There is no 2. That’s *really* all that’s needed to be an iterable.

<u>Iterators:</u>

1. Can be passed to the `next` function which gives their next item or raises `StopIteration`
2. Return themselves when passed to the `iter` function.

<u>The inverse of these statements should also hold true. Which means:</u>

1. Anything that can be passed to `iter` without an error is an iterable.
2. Anything that can be passed to `next` without an error (except for `StopIteration`) is an iterator.
3. Anything that returns itself when passed to `iter` is an iterator.



Again:

- An iter**able** is something you're able to iterate over
- An iter**ator** is the agent that actually does the iterating over an iterable



| Object    | Iterable? | Iterator? |
| --------- | --------- | --------- |
| Iterable  | ✔️         | ❓         |
| Iterator  | ✔️         | ✔️         |
| Generator | ✔️         | ✔️         |
| List      | ✔️         | ❌         |

----

### Loop Gotchas: 🤨

1.

```python
>>> numbers = [1, 2, 3, 5, 7]
>>> squares = (n**2 for n in numbers)
>>> 9 in squares
True
>>> 9 in squares
False
>>> 

```



2.

```python
>>> numbers = [1, 2, 3, 5, 7]
>>> squares = (n**2 for n in numbers)

>>> tuple(squares)
(1, 4, 9, 25, 49)

>>> sum(squares)
0
```



----
----



## Debunking Python For Loops: what makes `for` loops tick ➿

#### What is an iterator?

> In python everything is an object and just like any other object in python an **iterator** is also an object but an object that can be **iterated upon** and will return one element at a time upon calling.

Iterators find their implementations all over in python. We’ll find iterators in list comprehensions, generators and as you might have guessed they are also implemented within “For Loops”.



#### How do iterators work?

As mentioned an iterator is an object that can be iterated upon. The necessary conditions for creating an iterator object is it must implement two special methods

- **__ iter __** method. This method returns an iterator object when called upon an iterable

  > *An* **iterable** *is an object from which we can get an iterator. E.g list, tuples, string.*

- **__ next __** method. This method returns an element from an iterable one at a time. It is used to iterate an iterator object.



```python
>>> nums = [1,2,3,4]

>>> num_iter = iter(nums)  # get an iterator over list of numbers `nums`

>>> next(num_iter)
1
>>> next(num_iter)
2
>>> next(num_iter)
3
>>> next(num_iter)
4
>>> next(num_iter)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
>>> 

```



### For Loop Behind the scenes

```python
num_iterator = iter(numbers)
while True:
    try:
        # get the next item
        number = next(num_iterator)
    except StopIteration:
        break
```





## Understanding the difference between `__getattr__` and `__getattribute__`  [src - SO](https://stackoverflow.com/questions/4295678/understanding-the-difference-between-getattr-and-getattribute)



With objects, you need to deal with their attributes. Ordinarily, we do `instance.attribute`. Sometimes we need more control (when we do not know the name of the attribute in advance).

For example, `instance.attribute` would become `getattr(instance, attribute_name)`. Using this model, we can get the attribute by supplying the *attribute_name* as a string.



### Use of `__getattr__`

You can also tell a class how to deal with attributes which it doesn't explicitly manage and do that via `__getattr__` method.

Python will call `__getattr__` method whenever you request an attribute that hasn't already been defined (so you can define what to do with it).

**Example:**

In the following example class **Count** has no `__getattr__` method. 

Now in main when I try to access both `obj1.mymin` and `obj1.mymax` attributes everything works fine. 

But when I try to access `obj1.mycurrent` attribute -- Python gives  `AttributeError: 'Count' object has no attribute 'mycurrent'`

```python
class Count():
    def __init__(self,mymin,mymax):
        self.mymin=mymin
        self.mymax=mymax

obj1 = Count(1,10)
print(obj1.mymin)
print(obj1.mymax)
print(obj1.mycurrent)  --> AttributeError: 'Count' object has no attribute 'mycurrent'
```



Now class **Count** has `__getattr__` method.

Now when we try to access `obj1.mycurrent`attribute -- python returns whatever I have implemented in my `__getattr__` method. 

In example whenever I **try to call an attribute which doesn't exist**, **python creates that attribute and sets it to integer value 0**.



```python
class Count:
    def __init__(self,mymin,mymax):
        self.mymin=mymin
        self.mymax=mymax    

    # default behaviour for new attributes is set here
    def __getattr__(self, item):
        self.__dict__[item]=0
        return 0

obj1 = Count(1,10)
print(obj1.mymin)
print(obj1.mymax)
print(obj1.mycurrent1)
```



### Caveats and use of `__getattribute__`

If you need to catch every attribute *regardless whether it exists or not*, use `__getattribute__`instead. The difference is that `__getattr__` only gets called for attributes that don't actually exist. If you set an attribute directly, referencing that attribute will retrieve it without calling `__getattr__`.

> `__getattribute__` is called all the times.

If you have `__getattribute__` method in your class, python invokes this method for every attribute regardless whether it exists or not. So why do we need `__getattribute__` method? 

One good reason is that you can prevent access to attributes and make them more secure as shown in the following example.

Whenever someone try to access my attributes that starts with substring **'cur'** python raises `AttributeError` exception. Otherwise it returns that attribute.

```python
class Count:

    def __init__(self,mymin,mymax):
        self.mymin=mymin
        self.mymax=mymax
        self.current=None
   
    def __getattribute__(self, item):
        if item.startswith('cur'):
            raise AttributeError
        return object.__getattribute__(self,item) 
        # or you can use ---return super().__getattribute__(item)

obj1 = Count(1,10)
print(obj1.mymin)
print(obj1.mymax)
print(obj1.current)
```



> **Important:** In order to avoid infinite recursion in `__getattribute__` method, its implementation should always call the base class method with the same name to access any attributes it needs. For example: `object.__getattribute__(self, name)` or `super().__getattribute__(item)`and not `self.__dict__[item]`



## Lazy evaluation and attributes in Python

Lazy evaluation is a useful pattern that can improve your code's efficiency in many situations.

Example:

```python
# The slow way
class Person:
    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation
        self.relatives = self._get_all_relatives()
        
    def _get_all_relatives():
        ...
        # This is an expensive operation
```



> This approach may cause initialization to take unnecessarily long, especially when you don't always need to access `Person relatives`.



Better approach:

```python
# Better

class Person:
    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation
        # Get all relatives   
        self._relatives = None 
        
        @ property
        def relatives(self):
        if self._relatives is None:
            self._relatives = ...
```



In this case, the list of relatives is only computed the first time `Person#relatives`is accessed. After that, it's stored in `Person#_relatives` to prevent repeated evaluations.



### Solution 1: Use `@property`

`properties` aren’t exactly the same concept as attributes in Python. Essentially, *properties* are decorated functions. And through the decoration, regular functions are converted into properties, which can be used as other attributes, such as supporting the dot-notation access.

```python
class User1:
    def __init__(self, username):
        self.username = username
        self._profile_data = None

        print(f"{self.__class__.__name__} instance created")

    @property
    def profile_data(self):
        if self._profile_data is None:
            print("self._profile_data is None")
            self._profile_data = self._get_profile_data()
        else:             
            print("self._profile_data is set")
            return self._profile_data

    def _get_profile_data(self):
        # get the data from the server and load it to memory...
        print("Run the expensive operation")
        fetched_data = "The mock data of a large size"
        return fetched_data

```

`_profile_data` is set to `None` and is set only when it is needed (lazyyyyy 🚶🏻‍♂️)



### Solution 2: Use the `__getattr__`

**With custom classes, instance objects have their attributes saved in a dictionary, which can be accessed using the special method `__dict__`. Specifically, this dictionary stores the attribute names as its keys and the corresponding attribute values as its values. Notably, if the dictionary doesn’t contain the specified attribute, the special method `__getattr__` will get called as a fallback mechanism.**



```python
# Updated User class with the __getattr__
class User2:
    def __init__(self, username):
        self.username = username
        print(f"{self.__class__.__name__} instance created")

    def __str__(self):
        return f"user {self.username}"

    def __getattr__(self, name):
        print(f"__getattr__ called for {name}")
        if name == "profile_data":
            profile_data = self._get_profile_data()
            setattr(self, name, profile_data)
            return profile_data
        else:
            raise AttributeError(f"{self} has no attribute called {name}.")

    def _get_profile_data(self):
        # get the data from the server and load it to memory...
        print("Run the expensive operation")
        fetched_data = "The mock data of a large size"
        return fetched_data
```



The above code has the following changes that are relevant to the implementation of lazy attributes using the `__getattr__` special method.

- The updated `__init__` method removes the attribute setting with the profile data. It’s a necessary change because if it’s set, even with a value of `None`, the attribute and its value will be stored in the object’s `__dict__` attribute. In that case, the special method `__getattr__` won’t get called.
- We also implement the `__str__` method, which will be used to display the object for informational purposes (i.e., in the raised exception in the `__getattr__` method).
- In the `__getattr__` method, we specified that when the `profile_data`attribute is accessed, we’ll fetch the data remotely and set the attribute using the `setattr` method.



### Decorator based approach for lazy evaluation of properties:

```python
import functools


def lazyprop(fn):
    attr_name = '_lazy_' + fn.__name__

    @property
    @functools.wraps(fn)
    def _lazyprop(self):
        if not hasattr(self, attr_name):
            setattr(self, attr_name, fn(self))
        return getattr(self, attr_name)

    return _lazyprop


class Test():
    @lazyprop
    def a(self):
        print('generating "a"')
        return range(5)

```




----


## Tasks:

1. To have a `Polygon` class with `properties` being loaded lazily 🚶🏻‍♂️
2. To have a `PolygonSequence` class which can generate list of `Polygon` objects and expose an Iterator as well, `PolygonIterator` implemented and exposed via `__iter__` of PolygonSeq class
3. To have relevant tests in test file
----

✌🏻


#### References:

- https://towardsdatascience.com/debunking-python-for-loops-is-it-really-a-for-loop-b33687b79070
- https://stackoverflow.com/questions/3278077/difference-between-getattr-vs-getattribute/3278104#3278104
- https://stevenloria.com/lazy-properties/
- https://betterprogramming.pub/how-to-create-lazy-attributes-to-improve-performance-in-python-b369fd72e1b6
- https://stackoverflow.com/questions/3012421/python-memoising-deferred-lookup-property-decorator
