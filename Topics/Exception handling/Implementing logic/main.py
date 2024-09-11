# try:
#       name, surname = input().split()
#       print(f"Welcome to our party, {name} {surname}")
# except ValueError:
#       print("You need to enter exactly 2 words. Try again!")

name_lst = input().split()
print(f"Welcome to our party, {name_lst[0]} {name_lst[1]}" if len(name_lst) == 2 else
      "You need to enter exactly 2 words. Try again!")
