#This program turns the given text into a text that Is emoji in discord
legal_characters = 'abcdefghijklmnopqrstuvwxyz'
text = input('Enter your text : ')
text = text.lower()
list_ = []

for i in text:
    if i not in legal_characters and i != ' ':
        list_.append(i)
    elif i == ' ':
        list_.append('  ')
    else:
        list_.append(f':regional_indicator_{i}: ')
list_ = ''.join(list_)
print(list_)