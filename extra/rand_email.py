from random import randint
import re

total = randint(20,40)

open('rand-emails.txt','w').close()
file = open('rand-emails.txt','a+')
for i in range(total):

    name_len = randint(4,8)
    digit_len = randint(1,4)
    domain_len = randint(4,8)

    name = ""
    for i in range(name_len):
        rand_char = chr(randint(97,122))
        name += rand_char
    
    for i in range(digit_len):
        rand_dig = str(randint(0,9))
        name += rand_dig
    
    name += "@"

    for i in range(domain_len):
        rand_char = chr(randint(97,122))
        name += rand_char
    

    name += (".com",".net")[randint(0,1)]

    file.write(name + '\n')
    if not randint(0,9):
        file.write(name + '\n')

file.close()

with open('rand-emails.txt') as f:
    addresses = set(re.findall(r'[\w]+@[\w]+\.[\w]+',f.read()))

open('rand-duplicate-free-emails.txt','w').close()
new_file = open('rand-duplicate-free-emails.txt','a')
for address in addresses:
    new_file.write(address + '\n')

new_file.close()
    