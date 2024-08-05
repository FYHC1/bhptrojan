import os
def run(**args):
    print("[*] In dirlister modele")
    files=os.listdir(args["."])

    return str(files)