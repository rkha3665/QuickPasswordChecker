import hashlib
import getpass
from urllib.request import urlopen
if __name__ == "__main__":
    password = getpass.getpass('Password:')
    myhash = hashlib.sha1(password.encode('utf-8'))
    hex_hash = myhash.hexdigest()
    five = hex_hash[:5]
    rest = hex_hash[5:]
    url = f'https://api.pwnedpasswords.com/range/{five}'
    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    data = html.split("\r\n")
    dictionary = dict(s.split(':') for s in data)
    if rest.upper() in dictionary:
        print(f'Password vulnerable, seen {dictionary[rest.upper()]} times')
    else:
        print(f'Password not seen')