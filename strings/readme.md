
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