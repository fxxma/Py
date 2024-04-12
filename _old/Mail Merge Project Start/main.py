PLACEHOLDER = "[name]"

with open("Mail Merge Project Start/Input/Names/invited_names.txt") as names_file :
    names = names_file.readlines()
    print(names)
