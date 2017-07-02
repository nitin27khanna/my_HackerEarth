string = input()
def rev_string(string):
    index = len(string)
    rev_str = ""
    while index :
        rev_str += string[index-1]
        index = index - 1
    return rev_str
#string_r = string[::-1]
string_r = rev_string(string)
if string_r == string:
    print ("YES")
else:
    print("NO")
