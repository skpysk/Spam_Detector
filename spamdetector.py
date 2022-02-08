import os
x= input("Enter Which Spam Word Do You Found :  ")
def spamdetector(file , x) :
    with open (file, "r") as f :
        allfile = f.read()
    if x in allfile.lower() :
        return True
    else:
        return False
content = os.listdir()
found = 0
for i in content :
    if i.endswith(".txt"): # ager i ka end ".txt" he to he print kro
      result = spamdetector(i,x)
      if (result) :
          print (f"{x} is found in files {i} !!")
          found = found + 1
      else:
          print (f"{x} is not found in {i}")
print (f"******** {x} detector summary ********")
print(f"{found} files found with your {x}")