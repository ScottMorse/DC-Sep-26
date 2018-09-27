import re

with open('extra/emails.txt') as f:
    read = f.read()

addresses = set(re.findall(r'[\w]+@[\w]+\.[\w]+',read))
print(addresses)

new_file = 'duplicate-free-emails.txt'
open(new_file,'w').close()

working_file = open(new_file,'a')
for address in addresses:
    working_file.write(address.strip() + '\n')
