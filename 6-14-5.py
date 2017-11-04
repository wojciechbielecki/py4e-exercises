text = 'X-DSPAM-Confidence:0.8475'
colon_index = text.find(':')
number = text[colon_index+1:]
number = float(number)
print(type(number), number)
