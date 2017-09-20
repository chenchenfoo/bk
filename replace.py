import re
import json

#f = open("sessions.txt", "r")
#lines = json.load(f)

with open('filter.txt', 'w') as new_file:
    with open('sessions.txt') as old_file:
        for line in old_file:
            if '*' in line:
                continue
            else:
                new_file.write(line)
