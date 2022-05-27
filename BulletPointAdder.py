#! python3
#BulletPointAdder - adds bullet points to the start


import pyperclip

test = pyperclip.paste()
lines = test.split('\n')
for i in range(len(lines)):
    lines[i] = '*' + lines[i]
    print(lines[i])




