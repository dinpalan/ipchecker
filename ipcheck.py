#! /usr/bin/env python3
#SHEBANG
#copyright (c) Dinesh_Kumar_Palanivelu #Save file as <title>.py in your preferred location. Then start typing
import re
from loguru import logger
from time import sleep
#import modules with methods in this space


def ipchecker():
    while True:
        ip=input('enter a valid ip address:\n')
        a=ip.split('.')
        try:
            if ( (len(a)==4) and ( 1<=int(a[0])<=223) and (int(a[0])!=127) and (int(a[0])!=169 or int (a[1])!=254) and (0<= int(a[1])<=255) and (0<=int(a[2]) <=255) and (0<=int(a[3])<=255)):
                print('Valid ip address')
                break
        except ValueError:
            print('please enter an integer')
        else:
            if (int(a[0])==127):
                answer=input('This is a loopback ip address do you wish to continue(yes/no):')
                if answer=='yes' or answer=='y':
                    continue
                else:
                    break
            print('bad ip')
            continue
    return ip 

       
      
def dikupaipchecker():
#write your main function here 
       try:
              ipchecker()
          
       except KeyboardInterrupt:
              print("Exiting because of program interpreted by user"); print("Thanks for using my application");       
              
if __name__=='__main__':
       dikupaipchecker() 
