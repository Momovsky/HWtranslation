import hashlib

def get_md5(filename):
    with open(filename, 'rb') as file:
        content = file.read()
        md5hash = hashlib.md5()
        md5hash.update(content)
        digest_md5 = md5hash.hexdigest()
    return(digest_md5)

def get_sha(filename):
    with open(filename, 'rb') as file:
        content = file.read()
        sha = hashlib.sha256()
        sha.update(content)
        digest_sha = sha.hexdigest()
    return(digest_sha)
