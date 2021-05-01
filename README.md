# MurMurHash
This little tool is to calculate a MurmurHash value of a favicon to hunt phishing websites on the Shodan platform.

![image](https://user-images.githubusercontent.com/3501170/116244718-89518780-a7ab-11eb-8072-f64ff34eb54f.png)


# Little Bit on MurMurHash
MurmurHash is a non-cryptographic hash function suitable for general hash-based lookup. The name comes from two basic operations, multiply (MU) and rotate (R), used in its inner loop. The current version is MurmurHash3 which yields a 32-bit or 128-bit hash value. When using 128-bits, the x86 and x64 versions do not produce the same values, as the algorithms are optimized for their respective platforms. MurmurHash3 was released alongside SMHasher—a hash function test suite. 

Further reading on: https://en.wikipedia.org/wiki/MurmurHash

# Hunting Phishing

After reading about 


https://www.shodan.io/search?query=http.favicon.hash%3A309020573 <BR>
https://www.shodan.io/search?query=http.favicon.hash%3A476528568

