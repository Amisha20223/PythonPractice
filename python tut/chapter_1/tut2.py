s=input("Enter string: ")
if(len(s)<2):
    print("Empty")
else:
    print(s[:2]+s[-1]+s[-2])