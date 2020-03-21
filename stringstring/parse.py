mp = [{} for i in range(6)]

with open('ascii_letters.txt', 'r') as fin:
    while (fin.readline()):
        letter = fin.readline()[:-1]
        for j in range(6):
            mp[j][letter] = fin.readline()[:-1].replace('.', ' ').replace('#', '~')
    fin.close()

with open('ascii_letters.py', 'w') as fout:
    fout.write('ascii_letters = ')
    fout.write(str(mp))
    fout.close()
