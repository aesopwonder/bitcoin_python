##################################################################
# Created by Andrew Nguyen
# September 22 2017
# Testing Python bitcoin library
##################################################################
from bitcoin import *
##################################################################
#                               Code
##################################################################
privkey = random_key()#generate private key
pubkey = privtopub(privkey) #generated public key from private key
addr = pubtoaddr(pubkey) #generate address from public key
h = history('1NPrfWgJfkANmd1jt88A141PjhiarT8d9U')#find history of example address
##################################################################
#                               Output
##################################################################
print("**************************************************")
print(" ")
print("             PYTHON LIBRARY TESTING")
print(" ")
print("**************************************************")
print(" ")
print("This is an example of a private key \n-> " + privkey)
print(" ")
print("**************************************************")
print(" ")
privkey = sha256("this would be a very poor choice of a key")
print("This is an example of a poor choice of private key... \n(sha256 of 'this would be a very poor choice of a key') \n-> " + privkey)
print(" ")
print("**************************************************")
print(" ")
print("This is an example of a public key \n-> " + pubkey)
print(" ")
print("**************************************************")
print(" ")
print("This is an example of a bitcoin address \n->" +  addr)
print(" ")
print("**************************************************")
print(" ")
print"This is an example of a bitcoin address history \n->",
print (h)
print(" ")
print("**************************************************")
print(" ")
print("*************************************************")
print("*****           ***          ***            *****")
print("*****  *******  *******  *******  ***************")
print("*****  *******  *******  *******  ***************")
print("*****  *******  *******  *******  ***************")
print("*****           *******  *******  ***************")
print("*****  *******  *******  *******  ***************")
print("*****  *******  *******  *******  ***************")
print("*****  *******  *******  *******  ***************")
print("*****  *******  *******  *******  ***************")
print("*****           *******  *******          *******")
print("*************************************************")
print(" ")