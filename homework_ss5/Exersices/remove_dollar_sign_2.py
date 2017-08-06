def remove_dollar_sign(_string):
     removed_string = _string.replace("$", "")
     print(removed_string)
     return removed_string
     
string_with_no_dollars = remove_dollar_sign("$80% percent of $life is to showing $up")

if string_with_no_dollars == "80% percent of life is to showing up":
    print("Your function is correct")
else:
    print("Oops, there's a bug")
