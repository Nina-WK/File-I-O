f = open('newfile.txt', 'w')
lines = ['Hello', 'World', 'Welcome','To', 'File IO']
text = '\n'.join(lines)
f.writelines(text)
f.close()