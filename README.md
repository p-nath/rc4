# RC4 Stream Cipher using Python 2.7

Run RC4 encryption using the default plaintext and key by running ` pyhton rc4.py`


The keystream generated by the RC4 is distinguishable from perfectly random stream as it is biased in certain sequences.

To see that the second byte is biased towards 0 run ` python rc4.py c -o <output_filename> `

It was later shown that the first byte was also biased.

[Wiki](https://en.wikipedia.org/wiki/RC4#Biased_outputs_of_the_RC4)

