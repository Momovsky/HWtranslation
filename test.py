import hashlib

with open('DE.txt', 'rb') as file:
    content = file.read()
    print(content)
    md5hash = hashlib.md5()
    md5hash.update(content)
    digest = md5hash.hexdigest()

    print(digest)