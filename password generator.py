import string
import random
allchar=string.ascii_letters+string.digits+string.punctuation
length=int(input("enter length of password:"))
password=''.join(random.choices(allchar,k=length))
print("Your password is:",password)
