# A comment, this is so you can read your program later.
# Anything after the # is ignored by python.
# intentionally creating a merge conflict

print("I could have code like this.") # and the comment after is ignored

# You can also use a comment to "disable" or comment out code:
# print("This won't run.")

print("This will run.")
print("Okay, not much happening here")
color = input("Enter either 'red' or 'blue': ")

if color == 'red':
    print("Red is my favorite color")
    print('Red demands a loop')
    for red in range(1, 100):
        print(red, ' Red')
else:
    print('#' * 30)
    print("Blue is the color of budgies")
