#!/usr/bin/env python
# coding: utf-8

# In[1]:


x=10
if(x<15):
     print("the number is less than 15");


# In[2]:


x=10
if(x<15):
     print('the number is less than 15');


# In[4]:


x=10
if(x<15):
 print("the number is less than 15");


# In[11]:


x=10
if(x<15):
    print(x,"is less than 15")


# In[13]:


n=int(input("enter the number"))

if(n%2==0):
    print(n,"is even")
else:
 print(n,"is odd")


# In[14]:


n=int(input("enter the number"))

if n%2==0:
    print(n,"is even")
else:
    print(n,"is odd")


# In[ ]:


character=str(input("enter the character"))
if((character>="a") and (character<="z")):
    print("it is a character")
else:
    print("it is not a character")


# x=int(input("enter x value"))
# y=int(input("enter y value"))
# if(x>y):
#     print(x,"is greater")
# else:
#     print(y,"is greater")

# In[ ]:


a=1


# In[26]:


type(a)


# In[29]:


x=int(input("enter x value"))
y=int(input("enter y value"))
if(x==y):
    print(x**2)
else:
    print(x*y)


# In[33]:


str="world"
if("r" in str):
    print("r")
else:
    print("world")


# In[ ]:


str="world"
if("k" in str):
    print("r")
else:
    print("world")


# In[37]:


str="world"
character=str(input("enter the character"))
if("character" in str):
    print("r")
else:
    print("world")


# In[42]:


x=int(input("enter x value"))
if(x>0):
    print(x,"is positive number")
if(x<0):
    print(x,"is negative number")
if(x==0):
    print(x,"is equals to zero")


# 

# In[41]:


n=1
while(n<=15):   
    print(n)
    n=n+1;


# In[43]:


n=1
while(n<=10):   
    print(n)
    n=n+1;


# In[44]:


n=-22
while(n>=-45):   
    print(n)
    n=n-1;


# In[51]:


n=1
sum=0
while(n<=100):
        if(n%2==0):
             sum=sum+n;
          
        n=n+1;
print(sum)


# In[70]:


x=int(input("enter lower limit"))
y=int(input("enter upper limit"))
sum=0
while(x<=y):
    if(x%2==0):
             sum=sum+x;
          
    x=x+1;
print(sum)


# In[83]:


x=int(input("enter the number"));
while(x>0):
    r=x%10;
    print(r);
    x=x//10;

    


# In[ ]:


x=int(input("enter the number"))
sum=0
while(x!=0):
    r=x%10;
    if(r%2==0):
        sum=sum+r;
    x=x//10;
print(sum)        
        


# In[3]:


x=int(input("enter the number"))
while(x!=0):
    r=x%10;
    if(r==1):
        print("ONE")
    elif(r==2):
        print("TWO")
    elif(r==3):
        print("THREE")
    elif(r==4):
        print("FOUR") 
    elif(r==5):
        print("FIVE")        
    elif(r==6):
        print("SIX")        
    elif(r==7):
        print("SEVEN") 
    elif(r==8):
        print("EIGHT")
    elif(r==9):
        print("NINE")        
    else:
        print("ZERO")   
    x=x//10;    
        


# In[32]:


x=int(input("enter the number for counting"))
y=int(input("enter the number"))
z=int(input("enter the number"))
cnt=0
while(y<=z):
    temp=y;
    while(temp!=0):
        r=temp%10;
        if(x==r):
            cnt=cnt+1;
        temp=temp//10; 
        
    y=y+1;
print(cnt)
    


# In[38]:


k=4
s=8
if k>2:
    print k
else:
    print s


# In[51]:


def naturalNumbers(n):
    cnt=1
    while(cnt<=n):
        print(cnt,end=" ")
        cnt=cnt+1;
    print()
    return   
naturalNumbers(22);


# In[59]:


def factorial(n):
    fact=1
    while(n!=0):
        fact=fact*n;
        n=n-1;
    return fact;
print(factorial(5));
print(factorial(100));


# In[65]:


def factorial(n):
    fact=1
    while(n!=0):
        fact=fact*n;
        n=n-1;
    print(fact)    
    return fact;
factorial(4);
factorial(10);


# In[90]:


def palindrome(n1,n2):
    sum=0
    cnt=0
    while(n1!=n2):
        sum=0
        temp=n1;
        while(n1!=0):
            r=n1%10;
            sum=(sum*10)+r;
            n1=n1//10;
        if(temp==sum):
            cnt=cnt+1; 
        n1=temp;   
        n1=n1+1;
  
    return cnt;


print(palindrome(1,20));


# In[ ]:





# In[ ]:




