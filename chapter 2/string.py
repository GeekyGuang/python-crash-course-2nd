name = 'ada lovelace'
print(name.title())
print(name.upper())
print(name.lower())

first_name = 'ada'
last_name = 'lovelace'
full_name = f"{first_name}... {last_name}"
print(full_name)
# print(f"Hello, {full_name.title()}!")

message = f"Hello, {full_name.title()}!"
print(message)

print("Languages: \n\tPython\n\tC\n\tJavaScript")

favorite_language = '  python   '
print(favorite_language.lstrip())
print(favorite_language.rstrip())
print(favorite_language.strip())

favorite_language = favorite_language.strip()
print(favorite_language)
print('hello  '.rstrip())