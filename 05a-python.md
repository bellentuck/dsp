# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Main similarities:
- Both lists and tuples are comma-separated sequences of values (elements)
- Most list operators also work on tuples

>> Main differences:
- Tuples are immutable (unmodifiable); lists are mutable (modifiable)
- Tuples can be return values of functions; lists cannot
- Tuples cannot be aliased and are therefore better means for passing a sequence as an argument to a function

>> A list is a sequence of elements; a tuple is an immutable, immutably ordered list. Both lists and tuples are comma-separated sequences of values (i.e., elements), and often both act the same way: both will split up strings into individual characters, for instance, and most list operators also work on tuples. Tuples, however, have no methods and cannot be aliased. "Using a tuple instead of a list is like having an implied `assert` statement that shows this data is constant, and that special thought (and a specific function) is required to override that" (Dive into Python, "Introducing Tuples"). Tuples' consistency makes them more quickly searchable than lists: immutable types are hashable; mutable types are not (Think Python, ch11). Variable-length arguments (gathered, `(*args)`, or scattered, `(*tuple)`) and return values (`return x, y`) are both tuples.

>> Most tuples but no lists will work as keys in dictionaries. Dictionary keys map to values via a hashtable, so dictionary keys must be hashable (so, immutable). So lists will absolutely not work. Tuples of strings, ints, floats, and other immutable types will. However, a tuple of lists "counts as mutable and isn't safe to use as a dictionary key" (Dive into Python). 

>> A footnote on the need for hashability in dictionary keys, from Think Python (ch11): "A hash is a function that takes a value (of any kind) and returns an integer. Dictionaries use these integers, called hash values, to store and look up key-value pairs. This system works fine if the keys are immutable. But if the keys are mutable, like lists, bad things happen. For example, when you create a key-value pair, Python hashes the key and stores it in the corresponding location. If you modify the key and then hash it again, it would go to a different location. In that case you might have two entries for the same key, or you might not be able to find a key. Either way, the dictionary wouldn’t work correctly."

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Sets are "unordered collections of unique elements" (Python Software Foundation, "The Python Standard Library," sect 8.7): like lists, sets are collections of elements; unlike lists, sets are unordered; and unlike lists, sets support only one instance of an element per set. Sets present ranges, not bundles, of items. "A set is a dictionary with no values. It has only unique keys. Its syntax is similar to that for a dictionary. But we omit the values, and can use complex, powerful set logic" (dotnetperls.com/set-python).

>> Here are some basic examples of using lists vs. sets:
```
$ a = ['sofa', 'pillows', 'pillows']
$ b = ['pillows', 'pillows', 'couch']
$ c = set(a)  # = set(['sofa', 'pillows'])
$ d = {'couch', 'pillows'}  # also a set

$ # add vs append: semantically equivalent, syntactically distinct
$ a.append('plastic coverings')
$ c.add('plastic coverings')
$ print a, c
['sofa', 'pillows', 'pillows', 'plastic coverings'] set(['sofa', 'pillows', 'plastic coverings'])

$ # concatination vs union: semantically similar, syntactically distinct 
$ print a + b
$ print c | d
['sofa', 'pillows', 'pillows', 'plastic coverings', 'pillows', 'pillows', 'couch']
set(['sofa', 'couch', 'pillows', 'plastic coverings'])

$ # concatination vs intersection: syntactically similar, semantically distinct
$ print a + b
$ print c & d
['sofa', 'pillows', 'pillows', 'plastic coverings', 'pillows', 'pillows', 'couch']
set(['pillows'])
```

>> Lists and sets can both be used to find and iterate over elements. Importing the module `timeit`, we can compare performance between lists and sets. The following is the code I used to run performance comparisons for iterating over elements and for finding them:
```
def iter_test(iterable):
    """Test: iterating over elements"""
    for i in iterable:
        pass

def in_test(iterable):
    """Test: finding elements"""
    for i in range(1000):
        if i in iterable:
            pass

from timeit import timeit
print "Avg iteration times:"
print "Sets: ", timeit(
    "iter_test(iterable)",
    setup="from __main__ import iter_test; iterable = set(range(10000))",
    number=10000)
print "Lists: ", timeit(
    "iter_test(iterable)",
    setup="from __main__ import iter_test; iterable = list(range(10000))",
    number=10000)

print "\nAvg find times:"
print "Sets: ", timeit(
    "in_test(iterable)",
    setup="from __main__ import in_test; iterable = set(range(1000))",
    number=10000)
print "Lists: ", timeit(
    "in_test(iterable)",
    setup="from __main__ import in_test; iterable = list(range(1000))",
    number=10000) 
```
>> Here's the output:
```
Avg iteration times:
Sets:  1.92396998405
Lists:  1.5951461792

Avg find times:
Sets:  0.887874126434
Lists:  96.5262088776
```
>> The major find here is that sets are significantly quicker at finding elements than are lists. Why? Because sets are implemented using hash tables and hash tables are awesomely efficient. "Whenever you add an object to a set, the position within the memory of the set object is determined using the hash of the object to be added. When testing for membership, all that needs to be done is basically to look if the object is at the position determined by its hash, so the speed of this operation does not depend on the size of the set. For lists, in contrast, the whole list needs to be searched, which will become slower as the list grows" (Stack Overflow, "What makes sets faster than lists in python?"). (Minor find: sets iterate over their contents more slowly than lists, which is to say neither data structure is generally faster than the other.)

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> `lambda`, and the form `lamba x: x`, is an alternate syntax or notation for functions in Python. Specifically `lambda` is used to create anonymous (unnamed) functions that do little pieces of work, often within other functions like `filter()`, `map()`, and `reduce()`, without the syntactic clutter of an explicitly defined function with explicitly returned output. 

>> In addition to using a `lambda` function within `filter()`, `map()`, and `reduce()`, which take function + list as arguments, we can use a `lambda` in the `key` argument to `sorted()`, which can take list + function:
```
$ cousin_tuples = [
      ("brean", "momma's boy", 25),
      ("rebna", "father's pride", 11),
      ("abner', "father's pain", 16),
      ("sue", "daddy's lil angel", 2),
]
$ sorted(cousin_tuples, key=lambda cousin: cousin[2])   # sort by age
[("sue", "daddy's lil angel", 2), ("rebna", "father's pride", 11), \
("abner', "father's pain", 16), ("brean", "momma's boy", 25),]
```
>> `sorted()` can take one or two arguments: the simplest version of sort just sorts a list in the default Python order. The two-argument version of sort takes in both `list` and `key` arguments. The `key` specifies how the list is to be sorted. "The value of the `key` parameter should be a function that takes a single argument and returns a key to use for sorting purposes. This technique is fast because the key function is called exactly once for each input record" (Python Wiki, "Sorting Mini-HOW TO"). `lambda`'s a perfect fit for the job.

>> Way way back when, the Spartan--i.e., Lacedaimonian--military used shields featuring the letter Lambda as a "heraldic" device (a sign that something was about to happen: namely, opening of a can of Spartan whoop-ass). As whimsical as it may be, I like to think of Lambda-the-anonymous-function-signifier as a kind of Spartan soldier--a one-of-many player in the bigger picture...

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> Comprehensions provide a quick-n-easy way to structure data. A list comprehension (see Python Software Foundation, "Data Structures", 5.1.4) consists of

>> `[` + `expression` + `for` clause (feat. `in`) + >=0 `for` and/or `if` clauses + `]`.

>> For instance, `[x*y for x in range(4) for y in range(3, 6) if x*y != 10]` will give us `[0, 4, 18]`. 

>> Two common applications of list comprehensions are "[a] to make new lists where each element is the result of some operations applied to each member of another sequence or iterable, or [b] to create a subsequence of those elements that satisfy a certain condition" (Python Software Foundation): 
```
$ reciprocals = [1/float(n) for n in range(1, 11)]  # common application [a]
$ reciprocals
[1.0, 0.5, 0.3333333333333333, 0.25, 0.2, 0.16666666666666666, \
0.14285714285714285, 0.125, 0.1111111111111111, 0.1]

$ evens = [x for x in range(11) if x%2 == 0 if x > 0]  # common application [b]
$ evens
[2, 4, 6, 8, 10]
```
>> Such operations may also be performed using a `lambda` + `map()` or `filter()`, respectively:
```
$ reciprocals = map(lambda n: 1/float(n), range(1, 11))
$ reciprocals
[1.0, 0.5, 0.3333333333333333, 0.25, 0.2, 0.16666666666666666, \
0.14285714285714285, 0.125, 0.1111111111111111, 0.1]

$ evens = filter(lambda x: x%2 == 0 and x > 0, range(11))
$ evens
[2, 4, 6, 8, 10]
```
>> How do these latter functions compare to the list comprehensions? Both strategies generate the same results, and often either is viable. List comprehensions are more efficient and easier to read, however, and so are preferred when possible. But comprehensions have their limits: "when the construction rule is too complicated to be expressed with `for` and `if` statements, or if the construction rule can change dynamically at runtime," list comprehensions are too simple (secnetix.de, "Python: List Comprehensions").

>> To finish things off here are the set and dictionary comprehension versions of `reciprocals` and `evens`, too!
```
# set comps:

$ reciprocals = {1/float(n) for n in range(1, 11)}
$ reciprocals
[1.0, 0.5, 0.3333333333333333, 0.25, 0.2, 0.16666666666666666, \
0.14285714285714285, 0.125, 0.1111111111111111, 0.1]

$ evens = {x for x in range(11) if x%2 == 0 if x > 0}
$ evens
{2, 4, 6, 8, 10}


# dict comps:

$ reciprocals = {n : 1/float(n) for n in range(1, 11)}  # {key:val for key}
$ reciprocals {1: 1.0, 2: 0.5, 3: 0.3333333333333333, 4: 0.25, 5: 0.2, \
6: 0.16666666666666666, 7: 0.14285714285714285, 8: 0.125, \
9: 0.1111111111111111, 10: 0.1}

$ evens {x : 'even' for x in range(11) if x%2 == 0 if x > 0}
$ evens
{2: 'even', 4: 'even', 6: 'even', 8: 'even', 10: 'even'}
```

---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 937

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> -82

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





