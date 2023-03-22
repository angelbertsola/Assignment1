import random
import string
import hashlib
import os

#filename = '/serverdata/output_filename.txt'
#data = ''.join(random.choices(string.ascii_uppercase + string.digits, k=1024))

# write random data to file
#     with open(filename, 'w') as f:
#         f.write(data)



# Open a file for writing
with open("output_filename.txt", "w") as file:
    # Write 10 lines of random data
    for i in range(10):
        # Generate a random string of 10 characters
        random_string = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=10))
        # Write the string to the file
        file.write(random_string + "\n")

# calculate checksum
checksum = hashlib.md5(data.encode('utf-8')).hexdigest()

# send file and checksum to client
with open(filename, 'rb') as w:
    file_data = w.read()
    client_data = file_data + b'\n' + checksum.encode('utf-8')
    # send client_data to client here
