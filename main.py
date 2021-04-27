# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

names_conv = name1 + name2
lower_case_string = names_conv.lower()

t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")

true = t+r+u+e


l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")
love = l+o+v+e 

sum3=int(str(true) + str(love))

print(f"your score is  {sum3}")

if ((sum3<10) or (sum3>90)):
 print(f"Your love score is {sum3}, you go together like trump and melania. ")
elif ((sum3>=40) and (sum3<=50)):
 print(f"Your love score is {sum3}, you are alright together. ")

else:
  print(f"your love score is {sum3}")
