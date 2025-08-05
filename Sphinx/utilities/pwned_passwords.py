import hashlib
import requests

def check_pwned_password(password):
    # Step 1: SHA1 hash the password
    sha1_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix = sha1_password[:5]
    suffix = sha1_password[5:]

    # Step 2: Query the PwnedPasswords API using only the first 5 characters
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    response = requests.get(url)

    if response.status_code != 200:
        raise RuntimeError(f"API error: {response.status_code}")

    # Step 3: Search for the suffix in the response
    hashes = (line.split(':') for line in response.text.splitlines())
    for hash_suffix, count in hashes:
        if hash_suffix == suffix:
            return int(count)  # Password was pwned this many times

    return 0  # Not found, considered safe