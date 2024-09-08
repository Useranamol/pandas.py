import pandas as pd

s = pd.Series(['  Hello  ', ' World  ', 'Python'])
stripped_strings = s.str.strip()
print(stripped_strings)

# original_strings = pd.Series(['Hello', 'World', 'Python'])
# lowercase_strings = original_strings.str.lower()
# uppercase_strings = original_strings.str.upper()
# print(lowercase_strings)
# print(uppercase_strings)
g = pd.Series(['hello', 'world', 'python'])
capitalized_strings = g.str.capitalize()
print(capitalized_strings)