'''a=int(input("Enter the number"))
x=a
b=0
while a>0:
    c=a%10
    b=b*10+c
    a=a//10
print(b)
if b==x:
    print("palindrome")
else:
    print ("not palindrome")'''
    
'''a=int(input('Enter number'))
x=a
y=a
count=0
while a>0:
    count+=1
    a=a//10
print(count)
res=0
while x>0:
    c=x%10
    res=res+c**count
    x=x//10
print(res)
if res==y:
    print("Amstrong number")
else:
    print("Not an amstrong number")'''

'''a=int(input("Enter the number"))
sum=0
temp=a
while temp>0:
    digit=temp%10
    sum=sum+digit
    temp=temp//10
if a%sum==0:
    print("Harshad number")
else:
    print("Not a harshad number")'''


    



