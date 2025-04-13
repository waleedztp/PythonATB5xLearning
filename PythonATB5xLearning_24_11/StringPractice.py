name = input("Enter your name: ")
print(name)
print(name.upper())

# print("Hello\nWorld") will throw error as \n is an escape sequence, in such cases use r as shown below
print(r"Hello\nWorld")
print("Hello\tWorld")
print(r"Hello\tWaleed")
print("Hello\bWorld")
print(r"Hello\bWorld")

my_list = [2,4,6,8,10]
target = 12
is_present = False

for i in range(len(my_list)):
    for j in range(1, len(my_list)):
        if i != j and my_list[i] + my_list[j] == target:
            is_present = True
            break
    if is_present:
        print("Combination exists..")
        break