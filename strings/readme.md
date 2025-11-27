# Python Strings

---

## String Basics

- **Double quotes** — Use `"text"` to define a string.  
	_Example: `s = "hello"`_
- **Escape characters** — Use `\` to insert special characters.  
	_Example: `"Line1\nLine2"`_
- **Raw strings** — Prefix with `r` to ignore escape sequences.  
	_Example: `r"C:\\path\\file"`_
- **Triple quotes** — Use `'''` or `"""` for multi-line strings.  
	_Example: `'''multi\nline'''`_
- **Multiline Comments** — Use triple quotes for block comments.  
	_Example: `"""This is a comment"""`_
- **Indexing and Slicing Strings** — Access parts of a string with `[]`.  
	_Example: `s[0]`, `s[1:4]`_
- **The `in` and `not in` Operators** — Check for substring presence.  
	_Example: `'a' in 'cat'` returns `True`_
- **f-strings** — Embed expressions inside string literals.  
	_Example: `f"Value: {x}"`_

## String Methods

- **upper()** — Converts all characters to uppercase.  
	_Example: `'abc'.upper()  # 'ABC'`_
- **lower()** — Converts all characters to lowercase.  
	_Example: `'ABC'.lower()  # 'abc'`_
- **isupper()** — Checks if all characters are uppercase.  
	_Example: `'ABC'.isupper()  # True`_
- **islower()** — Checks if all characters are lowercase.  
	_Example: `'abc'.islower()  # True`_
- **isalpha()** — Checks if all characters are alphabetic.  
	_Example: `'abc'.isalpha()  # True`_
- **isalnum()** — Checks if all characters are alphanumeric.  
	_Example: `'abc123'.isalnum()  # True`_
- **isdecimal()** — Checks if all characters are decimals.  
	_Example: `'123'.isdecimal()  # True`_
- **isspace()** — Checks if all characters are whitespace.  
	_Example: `'   '.isspace()  # True`_
- **istitle()** — Checks if string is titlecased.  
	_Example: `'Hello World'.istitle()  # True`_

- **title()** — Converts string to title case.  
	_Example: `'hello world'.title()  # 'Hello World'`_
- **capitalize()** — Capitalizes the first character of the string.  
	_Example: `'hello'.capitalize()  # 'Hello'`_
- **startswith()** — Checks if string starts with a substring.  
	_Example: `'hello'.startswith('he')  # True`_
- **endswith()** — Checks if string ends with a substring.  
	_Example: `'hello'.endswith('lo')  # True`_
- **join()** — Joins iterable elements into a string with a separator.  
	_Example: `', '.join(['a', 'b'])  # 'a, b'`_
- **split()** — Splits a string into a list by a separator.  
	_Example: `'a,b,c'.split(',')  # ['a', 'b', 'c']`_
	_Example: `'hello world'.split()  # ['hello', 'world']`_
- **partition()** — Splits string at the first occurrence of a separator.
	_Example: `'hello world'.partition(' ')  # ('hello', ' ', 'world')`_
- **rjust()** — Right-aligns a string within a given width.	
	_Example: `'cat'.rjust(5)  # '  cat'`_
	_Example: `'Hello'.rjust(10, '*')  # '**********Hello'`_
- **ljust()** — Left-aligns a string within a given width.	
	_Example: `'cat'.ljust(5)  # 'cat  '`_
- **center()** — Centers a string within a given width.	
	_Example: `'cat'.center(5)  # ' cat '`_
- **strip()** — Removes leading and trailing whitespace.  
	_Example: `'  hello  '.strip()  # 'hello'`_	
- **rstrip()** — Removes trailing whitespace.  
	_Example: `'  hello  '.rstrip()  # '  hello'`_
- **lstrip()** — Removes leading whitespace.  
	_Example: `'  hello  '.lstrip()  # 'hello  '`_
- **ord()** — Returns the Unicode code point of a character.  
	_Example: `ord('a')  # 97`_
- **chr()** — Returns the character for a Unicode code point.  
	_Example: `chr(97)  # 'a'`_
- **replace()** — Replaces occurrences of a substring with another.  
	_Example: `'hello'.replace('l', 'x')  # 'hexxo'`_
- **find()** — Returns the lowest index of a substring.
	_Example: `'hello'.find('e')  # 1`_
- **removeprefix()** — Removes a specified prefix from the string.  
	_Example: `'unhappy'.removeprefix('un')  # 'happy'`_
- **removesuffix()** — Removes a specified suffix from the string.  
	_Example: `'running'.removesuffix('ing')  # 'run'`_	
	



