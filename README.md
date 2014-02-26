password-generator
==================

A python CLI flexible and interactive password generator to crease easy to remember and hard to guess passwords.

Check the password strenght in:
http://password-checker.online-domain-tools.com/
http://daleswanson.org/things/password.htm


### Usage

~~~~

usage: passwordmaker [-h] [-l LENGHT] [-st] [-n] [-a] [-al] [-au] [-an] [-ps]
                     [-e] [--version]

Interactive Pssword Creator

optional arguments:
  -h, --help            show this help message and exit
  -l LENGHT, --lenght LENGHT
                        Password Lenght
  -st, --strong         Strong Password - Numbers and Leters and characters
  -n, --numeric         Open in file manager after mounted
  -a, --alpha           Alpha mixed case password
  -al, --alpha-lowercase
                        Lowercase only password
  -au, --alpha-uppercarse
                        Uppercase only password
  -an, --alpha-numeric  Alpha numeric password
  -ps, --passphrase     Generates a passphrase from seed
  -e, --edit            Edit configuration file
  --version             show program's version number and exit

 
~~~~

### Examples


1. Numeric Password 8 characters
~~~~
$ passgen -l 8 -n
82577207
~~~~

* Lower Case and Upper Case 
~~~~
$ passgen -a -l 10
eLCJomJOMe
~~~~

* Alpha numeric
~~~~
$ passgen -l 10 -an
qSjqtL3MkL
~~~~

* Lower Case Only
~~~~
$ passgen -al -l 10
qpnkmcrtpr

~~~~

* Generate a passphrase 4 words

~~~~

$ passgen -l 4 -ps
4
74454
Word List
--------------
portion
little
Realm
entire

Passphrase all words
..........................
portion little Realm entire 

Passphrase all words joined
..........................
portionlittleRealmentire

Passphrase separated by dash
..........................
portion-little-Realm-entire

Upper / Lower case alternate password
..........................
PortionLittleRealmEntire

Passphrase number encoded
..........................
P0rt!0nL!ttleRe@lm3nt!re

Passphrase initial of all words		
..........................
plRe


~~~~



