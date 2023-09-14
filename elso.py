
'''print('üdv \na \nfedélzeten', end='')
print('Szia', 'Józsi')
'''

nev = input("Mi a neved: ")
print(f'Szia {nev}')
print('Szia {0}'.format(nev))
print('''Ez
több
sorba kerül''')
print('Jobbra'.rjust(50,' '))
print('Balra'.ljust(50,'-'))
print('Közép'.center(50,' '))