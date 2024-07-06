import random
print("Enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")
ch= int(input("Enter your choice :"))
print("User choice:",ch)
cmp_ch=random.randint(1,3)
print("Computer choice:",cmp_ch)
if(cmp_ch==ch):
    print("Its a draw")
elif(cmp_ch>ch):
    print("User lose,Computer wins")
elif(ch>cmp_ch):
    print("Computer lose,User wins")
elif cmp_ch==1 and ch==3:
    print("User lose,Computer wins")
elif ch==1 and cmp_ch==3:
    print("User wins.Computer loses")
print("thanks for playing")
