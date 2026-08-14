#Learning string methods
name = "I'M ABHINAV"
name2 = "i'm abhinav"
print(len(name))
print(len(name2))
print("changing case")
print(name2.upper())
print(name.lower())
print(name.title())
print(name2.title())
print(name2.capitalize())

print("removing whitespace")
print(name.strip())
print(name.lstrip())
print(name.rstrip())

print("finding an replacing")
print(name.find("H"))
print(name.replace("ABHINV","MESSI FAN"))
print(name2.replace("abhinav","messi fan"))


print("splitting and joining")
print(name.split())
print(name2.split())
c ="book, laptop, banana"
objects= c.split(",")
print(objects)
new_text = "-".join(c)
print(new_text)

print("checking string properties")
text2="abhinav7710"
print(text2.isalpha())
print(text2.isdigit())
print(text2.isalnum())
print(text2.isspace())