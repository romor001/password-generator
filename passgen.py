#!/usr/bin/env python
#
#  passgen.py
#
#  Python Password Generator
#


def numeric_password(Ndigits=6):
    """
    Generate numeric password
    defualt: 6 digit password

    """
    from random import random

    for i in range(2000):
        PASS = int(random() * (10 ** Ndigits))

    return PASS


def alpha_password(wordLen=8):
    import random

    for k in range(200):
        word = ''

        for i in range(wordLen):
            word += random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuz')

    print(word)


def alpha_lowercase(wordLen=8):
    import random

    for k in range(200):
        word = ''

        for i in range(wordLen):
            word += random.choice('abcdefghijklmnopqrstuz')

    print(word)


def alpha_uppercase(wordLen=8):
    import random

    for k in range(200):
        word = ''

        for i in range(wordLen):
            word += random.choice('abcdefghijklmnopqrstuz')

    print(word)


def alpha_num_password(wordLen=8):
    import random

    for k in range(200):
        word = ''

        for i in range(wordLen):
            word += random.choice('1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstu')

    print(word)


def strong_password(wordLen=8):
    import random

    for k in range(200):
        word = ''

        for i in range(wordLen):
            word += random.choice('-+_()*&$#@!<>;?|{}"1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstu')

    print(word)


def passphrase(pass_len=4, min_word_len=4, seed="seed.txt"):
    """
    pass_len: Password length
    min_word: Minimum
    seed:     Text file containing a big text
    """
    import random
    import re

    fp = open(seed)
    txt = fp.read()
    fp.close()

    chars = [',', '!', ';', '$', '%', '@', '&', '*', '<', '>', '.', "'", ':', '?', '"','-']
    txt = re.sub('[%s]' % ''.join(chars), '', txt)

    words = txt.split()

    #print(word)s
    print(pass_len)

    print(len(words))

    # Minimum word lenght

    passum = ""
    passphrase = ""
    passw = ""
    passdash = ""
    altern = ""

    idx = 0

    print("Word List\n--------------")

    while idx < pass_len:

        # Mixing to make more random.
        N = random.randint(0, 600)

        for k in range(N):
            word = random.choice(words)

        if len(word) >= min_word_len:
            print(word)

            passphrase = "".join([passphrase, word, " "])
            passw = "".join([passw, word[0]])
            passum = "".join([passum, word])
            passdash = "".join([passdash,  word, "-"])
            _word = "".join( [word[0].upper(), word[1:].lower()])
            altern = "".join([ altern, _word ])

            idx = idx + 1

    passdash = passdash[:-1]

    enc = altern
    enc = altern.replace('a','@')
    enc = enc.replace('i','!')
    enc = enc.replace('b','8')
    enc = enc.replace('b','8')
    enc = enc.replace('o','0')
    enc = enc.replace('E','3')
    enc = enc.replace('s','5')
    enc = enc.replace('c','(')
    enc = enc.replace('I','&')
    enc = enc.replace('g','9')
    enc = enc.replace('v','\/')





    print("\nPassphrase all words")
    print("..........................")
    print(passphrase)

    print("\nPassphrase all words joined")
    print("..........................")
    print(passum)

    print("\nPassphrase separated by dash")
    print("..........................")
    print(passdash)

    print("\nUpper / Lower case alternate password")
    print("..........................")
    print(altern)

    print("\nPassphrase number encoded")
    print("..........................")
    print(enc)

    print("\nPassphrase initial of all words\t\t")
    print("..........................")
    print(passw)


import argparse
import sys

desc =\
"""
Interactive Password Creator\n
"""
parser = argparse.ArgumentParser(prog='passwordmaker', description=desc)
parser.add_argument("-l", "--lenght", help="Password Lenght")
parser.add_argument("-st", "--strong", action="store_true",
                    help="\tStrong Password - Numbers and Leters and characters")
parser.add_argument("-n", "--numeric", action="store_true", help="\tOpen in file manager after mounted")
parser.add_argument("-a", "--alpha", action="store_true", help="\tAlpha mixed case password")
parser.add_argument("-al", "--alpha-lowercase", action="store_true", help="\tLowercase only password")
parser.add_argument("-au", "--alpha-uppercarse", action="store_true", help="\tUppercase only password")
parser.add_argument("-an", "--alpha-numeric", action="store_true", help="\tAlpha numeric password")

parser.add_argument("-ps", "--passphrase", action="store_true", help="\tGenerates a passphrase from seed")

parser.add_argument("-e", "--edit", action="store_true", help="Edit configuration file")
parser.add_argument('--version', action='version', version='%(prog)s 1.0')

args = parser.parse_args()


if len(sys.argv) == 1:

    parser.print_help()

    print("""
    Check the password strenght in:
    1. http://password-checker.online-domain-tools.com/
    2. http://daleswanson.org/things/password.htm
    """)

    print("""

    Examples

    $ ./passgen.py -l 10 -st
    I1VosLgNWE

    $ ./passgen.py -l 10 -n
    7292365565

    $ ./passgen.py -l 6 -n
    98944

    $ ./passgen.py -l 10 -an
    h8Cj4TAUf7

    $ ./passgen.py -l 3 -ps
    51561
    Word List
    --------------
    powerful
    after
    although

    Passphrase all words
    powerful after although

    Passphrase all words joined
    powerfulafteralthough

    Passphrase separated by dash
    powerful-after-although

    Upper / Lower case alternate password
    PowerfulAfterAlthough

    Passphrase initial of all words
    paa

    """)

    sys.exit(1)

if args.lenght:

    N = int(args.lenght)
else:
    N = 6

if args.strong:
    print(strong_password(N))

if args.numeric:
    print(numeric_password(N))

if args.alpha:
    print(alpha_password(N))

if args.alpha_lowercase:
    print(alpha_lowercase(N))

if args.alpha_numeric:
    print(alpha_num_password(N))

if args.passphrase:
    passphrase(N, 5)


