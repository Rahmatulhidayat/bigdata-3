Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> x = int(input("Please enter an integer: "))
Please enter an integer: 42
>>> if x < 8:
	x = 8
	print('Negative changed to eight')
elif x == 8:
	print('eight')
elif x == 9:
	print('nine')
else:
	print('more')

more
>>> 
>>> # Measure some strings:
>>> words = ['cat', 'window', 'defenestrate']
>>> for w in words:
	print(w, len(w))

	
cat 3
window 6
defenestrate 12
>>> 
>>> for w in words[:]:
	if len(w) > 6:
		words.insert(0, w)

		
>>> words
['defenestrate', 'cat', 'window', 'defenestrate']
>>> 
>>> for i in range(5):
	print(i)

	
0
1
2
3
4
>>> 
>>> for i in range(5, 10):
	print(i)

	
5
6
7
8
9
>>> 
>>> for i in range(0, 10, 3):
	print(i)

	
0
3
6
9
>>> for i in range(-10, -100, 30):
	print(i)

	
>>> for i in range(-10, -100, -30):
	print(i)

	
-10
-40
-70
>>> 
>>> a = ['Mary', 'had', 'a', 'little', 'lamb']
>>> for i in range(len(a)):
	print(i, a[i])

	
0 Mary
1 had
2 a
3 little
4 lamb
>>> 
>>> print(range(10))
range(0, 10)
>>> 
>>> list(range(5))
[0, 1, 2, 3, 4]
>>> 
>>> for n in range(2, 10):
	for x in range(2, n):
		if n % x == 0:
			print(n, 'equals', x, '*', n//x)
			break
		else
		
SyntaxError: invalid syntax
>>> 
>>> for n in range(2, 10):
	for x in range(2, n):
		if n % x == 0:
			print(n, 'equals', x, '*', n//x)
			break
		else:
			print(n, 'is a prime number')

			
3 is a prime number
4 equals 2 * 2
5 is a prime number
5 is a prime number
5 is a prime number
6 equals 2 * 3
7 is a prime number
7 is a prime number
7 is a prime number
7 is a prime number
7 is a prime number
8 equals 2 * 4
9 is a prime number
9 equals 3 * 3
>>> 
>>> for num in range(2, 10):
	if num % 2 == 0:
		print("Found an even number", num)
		continue
	print("Found a number", num)

	
Found an even number 2
Found a number 3
Found an even number 4
Found a number 5
Found an even number 6
Found a number 7
Found an even number 8
Found a number 9
>>> 
>>> while True:
	pass
KeyboardInterrupt
>>> 
>>> class MyEmptyClass:
	pass
KeyboardInterrupt
>>> def initlog(*args):
	pass
KeyboardInterrupt
>>> 
>>> def fib(n):
	a, b = 0, 1
	while a < n:
		print(a, end=' ')
		a, b = b, a+b
	print()

	
>>> fib(2000)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 
>>> 
>>> fib
<function fib at 0x00000227AB6CDBF8>
>>> f = fib
>>> f(100)
0 1 1 2 3 5 8 13 21 34 55 89 
>>> 
>>> fib(0)

>>> print(fib(0))

None
>>> 
>>> def fib2(n):
	result = []
	a, b = 0, 1
	while a < n:
		result.append(a)
		a, b = b, a+b
	return result

>>> f100 = fib2(100)
>>> f100
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
>>> 
>>> def ask_ok(prompt, retries=4, reminder='Please try again!'):
	while True:
		ok = input(prompt)
		if ok in ('y', 'ye', 'yes'):
			return True
		if ok in ('n', 'no', 'nop', 'nope'):
			return False
		retries = retries - 1
		if retries < 0:
			raise ValueError('invalid user response')
		print(reminder)

		
>>> 
>>> i = 5
>>> def f(arg=i):
	print(arg)

	
>>> i = 6
>>> f()
5
>>> 
>>> def f(a, L=[]):
	L.append(a)
		return L
	
SyntaxError: unexpected indent
>>> def f(a, L=[]):
	L.append(a)
	return L
print(f(1))
SyntaxError: invalid syntax
>>> def f(a, L=[]):
	L.append(a)
	return L
print(f(2))
SyntaxError: invalid syntax
>>> 
>>> def f(a, L=[]):
	L.append(a)
	return L
print(f(1))
print(f(2))
print(f(3))
SyntaxError: invalid syntax
>>> def f(a, L=[]):
	L.append(a)
	return L
f(1)
SyntaxError: invalid syntax
>>> 
>>> def f(a, L=[]):
	L.append(a)
	return L
print f(1)
SyntaxError: invalid syntax
>>> 
>>> def f(a, L=None):
	
KeyboardInterrupt
>>> def f(a, L=None):
	if L is None:
		L = []
	L.append(a)
	return L

>>> def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")

    
>>> 
>>> def function(a):
	pass

>>> function(0, a=0)
Traceback (most recent call last):
  File "<pyshell#149>", line 1, in <module>
    function(0, a=0)
TypeError: function() got multiple values for argument 'a'
>>> function(0, a=5)
Traceback (most recent call last):
  File "<pyshell#150>", line 1, in <module>
    function(0, a=5)
TypeError: function() got multiple values for argument 'a'
>>> 
>>> 
>>> def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

        
>>> cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")
-- Do you have any Limburger ?
-- I'm sorry, we're all out of Limburger
It's very runny, sir.
It's really very, VERY runny, sir.
----------------------------------------
shopkeeper : Michael Palin
client : John Cleese
sketch : Cheese Shop Sketch
>>> 
>>> def write_multiple_items(file, separator, *args):
	file.write(separator.join(args))

	
>>> def concat(*args, sep="/"):
	return sep.join(args)

>>> concat("earth", "mars", "venus")
'earth/mars/venus'
>>> concat("earth", "mars", "venus", sep=".")
'earth.mars.venus'
>>> 
>>> list(range(3, 6))
[3, 4, 5]
>>> list(range(*args))
Traceback (most recent call last):
  File "<pyshell#167>", line 1, in <module>
    list(range(*args))
NameError: name 'args' is not defined
>>> args = [3, 6]
>>> list(range(*args))
[3, 4, 5]
>>> 
>>> def parrot(voltage, state='a stiff', action='voom'):
	print("-- This parrot wouldn't", action, end=' ')
	print("if you put", voltage, "volts through it.", end=' ')
	print("E's", state, "!")

	
>>> d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
>>> parrot(**d)
-- This parrot wouldn't VOOM if you put four million volts through it. E's bleedin' demised !
>>> 
>>> def make_incrementor(n):
	return lambda x: x + n

>>> f = make_incrementor(42)
>>> f(0)
42
>>> f(1)
43
>>> f(2)
44
>>> 
>>> pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
>>> pairs.sort(key=lambda pair: pair[1])
>>> pairs
[(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]
>>> 
>>> pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five')]
>>> pairs.sort(key=lambda pair: pair[1])
>>> pairs
[(5, 'five'), (4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]
>>> [(5, 'five'), (4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]
[(5, 'five'), (4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]
>>> 
>>> def my_function():
	pass

>>> print(my_function.__doc__)
None
>>> 
>>> def f(ham: str, eggs: str = 'eggs') -> str:
	print("Annotations:", f.__annotations__)
	print("Arguments:", ham, eggs)
	return ham + ' and ' + eggs

>>> f('spam')
Annotations: {'ham': <class 'str'>, 'eggs': <class 'str'>, 'return': <class 'str'>}
Arguments: spam eggs
'spam and eggs'
>>> 

