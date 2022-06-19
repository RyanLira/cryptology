# how to use
The idea here is that you get the encryption and decryption scripts on your desktop.
you can compile them with pyinstaller if you like, or just run in terminal

if you do use pyinstaller open terminal and run theses commands

pyinstaller --onefile encryption.py

pyinstaller --onefile decryption.py

that should convert the python scripts into executible files, 
which you can then drag onto your desktop, or wherever.
then to use them, just click on them like you would click on anything else.

get your ally to do the same on their computer.
agree on a keyword in person.

open the encryption executible

enter the keyword and type the message to be encrypted
it will return an encrypted message

copy and past the encrypted message into snapchat or insta or text or email or whatever, then send it like normal.

your ally can then copy and paste your encrypted message from their email, into the decryption executible
using the key he can decrypt it and read your message.

then he can respond using the encryption executible

this way you can keep using normal social media like messenger and instagram,
but you have the option of security, from people who might otherwise read your messages



!!!!IMPORTANT!!!!

This code uses the vigenere cipher, which is only moderatly secure.
Far more secure than a caeser cipher, but it doesn't take longer than the lifetime of the universe to crack like RSA.
Relativly secure, but not uncrackable.

suitible for privacy from parents, spouses, teachers, uneducated authority figures, maybe underfunded police officers.
Not suitible for privacy from skilled cryptographers, the state, educated authority figures, or people who can afford to hire skilled cryptographers

NOTE:

longer keywords are harder to crack

a 1-charecter keyword could be brute forced in 26 tries

a 4-charecter keyword could be brute forced in 456976 tries

a 10-charecter keyword could be brute forced in 1.4 X 10^14 tries

