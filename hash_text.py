import hashlib
def hash_text():
    a_string = input('insert your sentence\n')
    hashed_string = hashlib.sha256(a_string.encode('utf-8')).hexdigest()
    print(hashed_string)