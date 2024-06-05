str =input("Enter a string:")
for ch in str:
    if(ch=='A' or ch=='a' or ch=='E' or ch =='e' or ch=='I'
    or ch=='i' or ch=='O' or ch=='o' or ch=='U' or ch=='u'):
        print(ch.swapcase(),end="")
    else:
        print(ch,end="")
    