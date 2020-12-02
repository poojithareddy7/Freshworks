import threading 
from threading import*
import time

dic={} 
def create(key,value,tout=0):
    if key in dic:
        print("error: this key already exists") 
    else:
        if(key.isalpha()):
            if len(dic)<(1024*1020*1024) and value<=(16*1024*1024): 
                if tout==0:
                    l=[value,tout]
                else:
                    l=[value,time.time()+tout]
                if len(key)<=32: 
                    dic[key]=l
            else:
                print("Memory limit exceeded")
        else:
            print("Invalind key_name")
      
def read(key):
    if key not in dic:
        print("given key does not exist in database.") 
    else:
        b=dic[key]
        if b[1]!=0:
            if time.time()<b[1]:
                stri=str(key)+":"+str(b[0]) 
                return stri
            else:
                print("error: time-to-live of",key,"has expired") 
        else:
            stri=str(key)+":"+str(b[0])
            return stri


def delete(key):
    if key not in dic:
        print("Please enter a valid key") 
    else:
        b=dic[key]
        if b[1]!=0:
            if time.time()<b[1]: 
                del dic[key]
                print("key is successfully deleted")
            else:
                print("error: time-to-live of",key,"has expired") 
        else:
            del dic[key]
            print("key is successfully deleted")

def modify(key,value):
    b=dic[key]
    if b[1]!=0:
        if time.time()<b[1]:
            if key not in dic:
                print(" given key does not exist in database.") 
            else:
                l=[]
                l.append(value)
                l.append(b[1])
                d[key]=l
        else:
            print("error: time-to-live of",key,"has expired") 
    else:
        if key not in dic:
            print("given key does not exist in database.") 
        else:
            l=[]
            l.append(value)
            l.append(b[1])
            dic[key]=l
