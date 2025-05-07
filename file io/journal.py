# This opens example file for writing
file = open('journal.txt', 'w')




with open('journal.txt', 'w') as file:
    entries = ['entry 1\n', 'entry 2\n','entry 3\n','entry 4\n','entry 5\n']
    for i in range(1, 6):
        file.write(f'{entries[i - 1]}\n')
    file.writelines(entries)

    file = open('journal.txt', 'r')

    content = file.read()

    print('Using read():')
    print(content)
file.close()
