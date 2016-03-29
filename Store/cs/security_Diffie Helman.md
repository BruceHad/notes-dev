In Public/Private key encryption each side has two keys. One known as the public key, this can be shared freely. The other is the private key, this must be kept private.

Once something has been encrypted by the public key, it can only be decrypted by it's private key.

When communicating, two sides use a shared secret key for the session. So the question is, how can the two sides, communicating on a public network, agree on a secret key for encryption.

One method is the [Diffie Helman Exchange][2]. 

Common analogy for the exchange uses colours instead of numbers.

Bob and Alice want to agree a shared secret, without communicating that secret to each other. 

So they agree a common colour (public) and each of them choose a colour for themselves (private). 

![Diffie-Hellman Colour Exchange](http://en.wikipedia.org/wiki/File:Diffie-Hellman_Key_Exchange.svg)

They each mix the public colour with their own private colour to come up with two new colours (public). These can then be swapped. And important aspect here is that the colours can't be extracted (basically reversing the calculation) to reveal the private colours. See below.

Now they mix the swapped colours with their own private colour to come up with the final colour. Since this final colour is made up of each of same three colours -- the public colour, Alice's Private Colour and Bob's private colour -- this final colour is the same on both sides. So they've agreed a common colour, that's a secret from anyone else, without revealing their private keys to anyone, including each other.

As I said, it's important that the calculation can't be reverse engineered (like extracting the public colour form the mixed colour). The basic algorithm makes use of the discrete logarithm problem:

Take the equation:

    A = g^a (mod p)

Where g, a
e.g.
    
    8 = 2^x (mod 11)

One solution to this is 3 since 2^3 % 11 = 8. But there are many other solutions to the problem, so it's difficult to figure out which solution is the correct one.

The original algorithms runs like so.

1. Alice and Bob agree to use a prime number p=23 and base g=5.

2. Alice chooses a secret integer a=6, then sends Bob A = g^a mod p

A = 5^6 mod 23
A = 15,625 mod 23
A = 8

3. Bob chooses a secret integer b=15, then sends Alice B = g^b mod p
B = 5^15 mod 23
B = 30,517,578,125 mod 23
B = 19

4. Alice computes s = B^a mod p
s = 19^6 mod 23
s = 47,045,881 mod 23
s = 2

5. Bob computes s = A^b mod p
s = 8^15 mod 23
s = 35,184,372,088,832 mod 23
s = 2

6. Alice and Bob now share a secret: s = 2. This is because 6*15 is the same as 15*6. So somebody who had known both these private integers might also have calculated s as follows:
s = 56*15 mod 23
s = 515*6 mod 23
s = 590 mod 23
s = 807,793,566,946,316,088,741,610,050,849,573,099,185,363,389,551,639,556,884,765,625 mod 23
s = 2

The important point here is that Alice tells Bob that she gets 8 and Bob tells Alice 9. Even if there is someone eavesdropping and therefore have the equation:

    8 = 5^x mod 23

Solving for x is very difficult as there are multiple potential solutions.
[1]: http://blog.hartleybrody.com/https-certificates/
[2]: http://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange
[3]: http://blog.markloiseau.com/2013/01/diffie-hellman-tutorial-in-python/
