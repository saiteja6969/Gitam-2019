#!/usr/bin/env python
# coding: utf-8

# In[9]:


def even(n):
    cnt=0;
    sum=0
    while(cnt!=n):
        if(cnt%2==0):  
            sum=sum+cnt;
        cnt=cnt+1; 
    return sum;
print(even(10));
print(even(5));


# In[15]:


def factors(n):
    i=1;
    while(i<n):
        if(n%i==0):
            print(i,end=" ");
        i=i+1;
    return i;
print(factors(50));


#  list=

# In[20]:


list=[1,5,7,9,33]
print(list)
print(list[0])
print(list[4])


# In[21]:


list=["fgyyg","ydjyg","qhqish"]
for x in (list):
    print(x);


# In[29]:


list=["fgyyg","ydjyg","qhqish","dy","tasf","uwysy"]
for x in (list):
    print(x,end =" ");
print()
print(list[2:5]);    
print(list[0:4]);
print(list[:5]); 


# In[40]:


list=[1,5,7,9,33,45,67,89,90]
for x in list:
    print(x,end =" ")
print()
print(list[1:-1])
print(list[2:-2])
print(list[3:-2])
print(list[::2])
print(list[::3])
print(list[20:-20])
print(list[::-3])
print(list[-3])
print(list[-1])


# In[68]:


list=["fgyyg","ydjyg","qhqish","dy","tasf","uwysy"]
print(list)
list[3]=96;
print(list)
del list[4]
print(list)
list[1]=96654654;
print(list)
list2=[1,5,7,9,33,45,67,89,90]
list2.insert(5,98)
print (list2)
print(len(list))
print(len(list+list2))
list.append(6756);
print(list)
print(list.count(96))
list2.pop(1)
print (list2)
list2.append(756,4,


# In[69]:


list=["fgyyg","ydjyg","qhqish","dy","tasf","uwysy"]
list.insert(2,"kst")
print(list)


# In[95]:


list=["fgyyg","ydjyg","qhqish","dy","tasf","uwysy"]
list.insert(2,"kst")
print(list)
print(list)
list.insert(1,"dy")
print(list)
list.insert(7,"kst")
print(list)
list.insert(90,"kst")
print(list)
print(len(list))
print(list)
list.remove("dy")
print(list)
list.reverse()
print(list)


# In[83]:


print(list)


# In[100]:


list=["fgyyg","ydjyg","qhqish","dy","tasf","uwysy"]
list.remove("dy")
print(list)
list.reverse()
print(list)
x=list[4]
print(x)
print (x[::-1])


# In[102]:


def ls(a,s):
    flag=0
    for i in range(len(a)):
        if a[i]==s:
            flag=1;
            break;
    if(flag!=0):
        print("Found")        
    else:
          print("Not Found")
a=[1,2,3,4,5]    
ls(a,5)


# In[111]:


def lsd(a,s):
    flag=0
    for i in range(len(a)):
        if a[i]==s:
            flag=flag+1;

      
    if(flag>=2):
        print("duplicate element found",flag,"times" )
    
a=[1,2,3,4,5,6,867,1,3,65,3,5,3,6767,3,45,3,4334]    
lsd(a,999)


# In[ ]:




