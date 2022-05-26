#! pyhton3
# mclip.py - a multiline clipboard program

import sys , pyperclip

text = {'agree' : '''yes, I agree. That sounds fine to me''',
            'busy' : '''Sorry I am busy. Can we do this later this week or next?''',
            'upsell' : '''Would you consider making this a monthly donation?'''}

if len(sys.argv) < 2:
    print("no keyword entered")
    sys.exit()

print("only the text associated with first keyword is copied if multiple arguments are provided.")

if sys.argv[1] in text.keys():
    pyperclip.copy(text[sys.argv[1]])
    print('text associated with', sys.argv[1] ,'is successfully copied!!')
else:
    print("there is no text for" , sys.argv[1])
