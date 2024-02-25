# Reserve a string
# It works for numbers also
def reserve_string(str):
    rev_str = ""
    for c in str:
        rev_str = c + rev_str
        print(rev_str + " updated string\n ")
    return rev_str


original_str = input("Enter a string: ")
original_str = original_str.lower()
rev_str = reserve_string(original_str)
print(rev_str)
# Palindrome str
if original_str == rev_str:
    print("Palindrome")
else:
    print("Not a Palindrome")
