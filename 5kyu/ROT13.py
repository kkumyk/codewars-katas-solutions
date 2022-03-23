"""

ROT13 - 5ky
https://www.codewars.com/kata/52223df9e8f98c7aa7000062

How can you tell an extrovert from an introvert at NSA? Va gur ryringbef, gur rkgebireg ybbxf ng gur BGURE thl'f fubrf.

I found this joke on USENET, but the punchline is scrambled. Maybe you can decipher it? According to Wikipedia, ROT13 (http://en.wikipedia.org/wiki/ROT13) is frequently used to obfuscate jokes on USENET.

Hint: For this task you're only supposed to substitute characters. Not spaces, punctuation, numbers etc. Test examples:

rot13("EBG13 rknzcyr.") == "ROT13 example."; rot13("This is my first ROT13 excercise!" == "Guvf vf zl svefg EBG13 rkprepvfr!"

http://exampleproblems.com/wiki/index.php/ROT13
"""


def rot13(message):
    a = ''
    for n in message:
        if n.isupper():  # string method that checks if the character is in upper case
            if n <= 'M':
                a += chr(ord(n) + 13)
                # print(a)
            else:
                a += chr(ord(n) - 13)
                # print(a)
        elif n.islower():
            if n <= 'm':
                a += chr(ord(n) + 13)
            else:
                a += chr(ord(n) - 13)
        else:
            a += n
    return a


print(rot13("Va gur ryringbef, gur rkgebireg ybbxf ng gur BGURE thl'f fubrf."))
