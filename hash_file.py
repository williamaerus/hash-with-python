import hashlib
import os
def hash_file():
    """"This function returns the SHA-1 hash
        of the file passed into it"""
    #a = filename
    # make a hash object
    h = hashlib.sha1()
    filename = input('insert the path of the file:  ')
    # open file for reading in binary mode
    with open(filename,'rb') as file:

        # loop till the end of the file
        chunk = 0
        while chunk != b'':
            # read only 1024 bytes at a time
            chunk = file.read(1024)
            h.update(chunk)
            
    # return the hex representation of digest
    return h.hexdigest()
v = hash_file()
print(v)
    
#os.system("script2.py 1")