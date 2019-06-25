#!/usr/bin/env python
# coding: utf-8

# In[14]:


def binarysearch(a,lindex,rindex,taritem):
   while lindex<=rindex:
       mindex=lindex+(rindex-lindex)//2;
       if a[mindex]==taritem:
           return mindex
       if a[mindex]>taritem:
           rindex=mindex-1
       else:
           lindex=mindex+1
   return -1
list1=[1,34,56,76,77,78,79,80,85,86,99,100,101]
res=binarysearch(list1,0,12,100)
if res!=-1:
   print("ITEM IS FOUND")
else:
    print("ITEM IS not FOUND")              
           
       


# In[ ]:


# def binarysearch(a,lindex,rindex,taritem):
    while lindex<=rindex:
        mindex=lindex+(rindex-lindex)//2;
        if a[mindex]==taritem:
            return mindex
        if a[mindex]>taritem:
            rindex=mindex-1
        else:
            lindex=mindex+1
    return -1
list1=[1,34,56,76,77,78,79,80,85,86,99,100,101]
res=binarysearch(list1,0,6,80) 
if res!=-1:
    print("ITEM IS FOUND")
else:
     print("ITEM IS not FOUND")


# In[16]:


def bubbleSort(a):
    for i in range(len(a)-1):
        for j in range(len(a)-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
    for i in range(len(a)):
        print(a[i],end=" ")
list2=[87463,56,67,89,9,7,45,675]
bubbleSort(list2)


# In[27]:


str="trfuftdftf"
print(str)
str2="""ygfgd ggeuiu
      uguw
      yeuuh
        yhiuhi
        python"""

print(str2)


# In[28]:


list1=[1,34,56,76,77,78,79,80,85,86,99,100,101]
list1.sort()
print(list1)


# In[43]:


str="PYTHON"
print(str)
print("str[0]= ",str[0])
print("str[2]= ",str[2])
print("str[4]= ",str[4])
print("str[-4]= ",str[-4])
print("str[1:4]= ",str[1:4])
print("str[1:-2]= ",str[1:-2])
print("str[0::2]= ",str[0::2])
print("str[::-1]= ",str[::-1])
print("str[::-2]= ",str[::-2])


# In[46]:


def ispalindrome(s):
    if s==s[::-1]:
        return True
    else:
        return False
print(ispalindrome("nio"))  
print(ispalindrome("nioin"))  


# In[48]:


n=int(input("enter a number"))
cnt=0
while n!=0:
    cnt=cnt+1
    n=n//10
print(cnt)    


# In[51]:


def countOfChars(str):
    return len(str)
countOfChars("PYTHONPROGRAMMING")


# In[52]:


def countDigits(n):
    return len(n)
countDigits("97574")


# In[80]:


def countOfUpperCaseChars(str):
    cnt=0
    str=list(str)
    for i in range(len(str)):
        if ord(str[i])>=65 and ord(str[i])<=90:
            cnt=cnt+1;
         
        
    return cnt;


print(countOfUpperCaseChars('PYThjhfygkING'))
print(countOfUpperCaseChars('YEDWGFKUYGDSG'))


# In[72]:


str="H"
str1='i'
str1.isupper()


# In[75]:


str="H"
str1='i'
str1.islower()


# In[91]:


def printingdigits(str):
    
    str=list(str)
    for i in range(len(str)):
        if ord(str[i])>=48 and ord(str[i])<=57:
            print(str[i],end=" ")
         
        
    return ;


printingdigits('sad55467jjkx')


# In[89]:


ord('P')


# In[99]:


def printingdigits(str):
    sum=0
    str=list(str)
    for i in range(len(str)):
        if ord(str[i])>=48 and ord(str[i])<=57:
            a=int(str[i])
            sum=sum+a;     
        
    return sum;


print(printingdigits("sad554673jjkx"))


# In[102]:


def printingdigits(str):
    sum=0
    str=list(str)
    for i in range(len(str)):
        if ord(str[i])>=48 and ord(str[i])<=57:
            sum=sum+ord(str[i])-48;
            
               
         
        
    return sum;


print(printingdigits("sad5546735jjkx"))


# In[104]:


def countOfLowerCaseChars(str):
    cnt=0
    str=list(str)
    for i in range(len(str)):
        if ord(str[i])>=97 and ord(str[i])<=122:
            cnt=cnt+1;
         
        
    return cnt;


print(countOfLowerCaseChars('PYThjhfygkING'))
print(countOfLowerCaseChars('YEDWGFKUYGDSG'))


# In[107]:


def EvenSumdigits(str):
    sum=0
    str=list(str)
    for i in range(len(str)):
        if ord(str[i])>=48 and ord(str[i])<=57:
            
            a=int(str[i])
            
            if(a%2==0):
                sum=sum+a;     
        
    return sum;


print(EvenSumdigits("sad554673jjkx"))

print(EvenSumdigits("2sa3d4j5j8k0x2"))


# In[109]:


def printingdigits(str):
    sum=0
    str=list(str)
    for i in range(len(str)):
        if ord(str[i])>=48 and ord(str[i])<=57:
            
            if((ord(str[i])-48)%2==0):
                  sum=sum+(ord(str[i]))-48;  
                
            
               
         
        
    return sum;


print(printingdigits("sad5546735jjkx"))


# In[ ]:


def UpperTolower(str):
    cnt=0
    str=list(str)
    for i in range(len(str)):
        if ord(str[i])>=65 and ord(str[i])<=90:
            cnt=cnt+1;
         
        
    return cnt;


print(countOfUpperCaseChars('PYThjhfygkING'))
print(countOfUpperCaseChars('YEDWGFKUYGDSG'))

