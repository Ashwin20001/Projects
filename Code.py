#!/usr/bin/env python
# coding: utf-8

# In[57]:


import os
import threading 
from threading import*
import time
import json

lock=threading.Lock() #thread safe
database={} 

def create(string,json1,timelimit=0):#for create operation
    lock.acquire(1)
    if string in database:
        print("Error:String is already available in the Database, input another string")
        lock.release()
    else:
        if(string.isalpha()):
            if len(database)<(1024*1020*1024) and len(json1)<=(16*1024*1024):
                if timelimit==0:
                    l=[json1,timelimit]
                else:
                    l=[json1,time.time()+timelimit]
                if len(string)<=32:
                        database[string]=l
                        lock.release()
                else:
                    print("String is too long")
                    lock.release()
            else:
                print("Error:Database is full")
                lock.release()
        else:
            print("Error:Input should only be in string format ")
            lock.release()

def read(string):#for read operation
    lock.acquire(1)
    if string not in database:
        print("Error:Input String is not available in the database. Try again")
        lock.release()
    else:
        if database[string][1]!=0:
            if time.time()<database[string][1]:
                d=(string,database[string][0])
                print(":".join(d))
                lock.release()
            else:
                print("Error:Time limit has been exceeded for",string)
                lock.release()
        else:
            d=(string,database[string][0])
            print(":".join(d))
            lock.release()

def delete(string):#for delete operation
    lock.acquire(1)
    if string not in database:
        print("Error:Input String is not available in the database. Try again")
        lock.release()
    else:
        if database[string][1]!=0:
            if time.time()<database[string][1]:
                del database[string]
                print("Data is successfully deleted")
                lock.release()
            else:
                print("Error:Time limit has been exceeded for",string)
                lock.release()
        else:
            del database[string]
            print("Data is successfully deleted")
            lock.release()
def file():#for file creation
    file_name=input("File Name")
    file=open(file_name,'x')
    file.write(str(database))
    print("Loctaion of the file: ",os.path.realpath(file_name))
    