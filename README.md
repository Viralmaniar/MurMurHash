# MurMurHash
This little tool is to calculate a MurmurHash value of a favicon to hunt phishing websites on the Shodan platform.

```bash
❯ python3 MurMurHash.py https://www.paypalobjects.com/webstatic/icon/pp32.png
Go to https://www.shodan.io/search?query=http.favicon.hash%3A48485760
```

# What is MurMurHash?
MurmurHash is a non-cryptographic hash function suitable for general hash-based lookup. The name comes from two basic operations, multiply (MU) and rotate (R), used in its inner loop. The current version is MurmurHash3 which yields a 32-bit or 128-bit hash value. When using 128-bits, the x86 and x64 versions do not produce the same values, as the algorithms are optimized for their respective platforms. MurmurHash3 was released alongside SMHasher—a hash function test suite. 

Further reading on: https://en.wikipedia.org/wiki/MurmurHash

# How to install?
<pre>
git clone https://github.com/Viralmaniar/MurMurHash.git
cd MurMurHash
python3 -m pip install -r requirements.txt
python MurMurHash.py
</pre>

# Detailed Blog:

https://isc.sans.edu/diary/Hunting+phishing+websites+with+favicon+hashes/27326

# Hunting Phish Events for Paypal & Tesla:

After reading about hunting of phishing websites using favicon hashes I thought to generalise it to accept Favicon URLs for quick analysis on the Shodan. 

Looking for a favicon icon file on the orginal website of Paypal:

![image](https://user-images.githubusercontent.com/3501170/116244994-d59cc780-a7ab-11eb-8185-68e5d06b092a.png)

Using `MurMurHash.py` file generating hash of the icon:
```bash
❯ python3 MurMurHash.py https://www.paypalobjects.com/webstatic/icon/pp32.png
Go to https://www.shodan.io/search?query=http.favicon.hash%3A48485760
```

Searching on Shodan for Paypal phishing domains/IPs:
- https://www.shodan.io/search?query=http.favicon.hash%3A309020573 
![image](https://user-images.githubusercontent.com/3501170/116245172-04b33900-a7ac-11eb-9356-fac258a7b8ea.png)

Validating Shodan results:

![image](https://user-images.githubusercontent.com/3501170/116245681-8c00ac80-a7ac-11eb-8e21-e9c942a94041.png)

![image](https://user-images.githubusercontent.com/3501170/116245886-c702e000-a7ac-11eb-98d4-d12c76377d37.png)

Now, let's search for Tesla icon on the original site:

![image](https://user-images.githubusercontent.com/3501170/116247177-ef3f0e80-a7ad-11eb-9edb-7428569a2035.png)

Searching on Shodan for Tesla phishing domains/IPs:
![image](https://user-images.githubusercontent.com/3501170/116783829-50c7eb80-aad4-11eb-85f1-48fef9e89a0a.png)

 - https://www.shodan.io/search?query=http.favicon.hash%3A476528568

![image](https://user-images.githubusercontent.com/3501170/116245987-e39f1800-a7ac-11eb-948b-39b722861db6.png)

Validating Shodan results:

![image](https://user-images.githubusercontent.com/3501170/116247540-4e9d1e80-a7ae-11eb-9cfa-d4db76d1b3ec.png)

# Questions?

Twitter: [@ManiarViral](https://twitter.com/maniarviral) <BR>
LinkedIn: https://au.linkedin.com/in/viralmaniar

