# Write a program to find the greatest of three numbers
n1=1
n2=2
n3=3
print("n1 is greater") if n1>n2 and n1>n3 else print("n2 is greater") if n2>n1 and n2>n3 else print("n3 is greater")

# Write a program to classify a character entered by the user as a vowel, consonant, or neither.
n="p"
if n in ["a", "e", "i", "o", "u"]:
    print(f"{n} is vowel")
elif n.isalpha():
    print(f"{n} is consonant")
else:
    print("neither")

# Calculate the grade of a student based on the marks they score:
#     90-100: Grade A
#     80-89: Grade B
#     70-79: Grade C
#     <70: Fail
marks=8
if marks>100:
    print("invalid")
elif marks<=100 and marks>=90:
    print("grade A") 
elif marks<=89 and marks>=80:
    print("grade B")
elif marks<=79 and marks>=70:
    print("grade C")
elif marks<70:
    print("Fail")
else:
    print("invalid input")