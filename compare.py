import time
def compare():
    d = input("do you want to compare hashes of a file?: ")
    time.sleep(1)
    print("")
    print("if you want to compare hashes but you don't have still any\nyou can get it by running the other scripts hash_text.py and hash_file.py")
    time.sleep(1)
    a = input("insert the first hash:  ")
    print("saving")
    time.sleep(1)
    b = input("insert the second hash:  ")
    print("comparing strings")
    time.sleep(3)
    if a == b:
        print("text's are identical")
    else:
        print("texts are differen't")
        if d == "yes":
            print("if those are hashes of a file don't trust it")
compare()