import os
print('Quer desligar o pc em:')
print('[1] Segundos')
print('[2] Minutos')
print('[3] Horas')
print('[4] cancelar o desligamento')
print('[0] Agora')


x = int(input('Digite um numero para continuar: '))

match x:
    case 1:
        n = int(input('em quantos segundos? '))
        print (os.system(f'shutdown -s -f -t {n}'))
        print(f'o pc vai desligar em {n} segundos')

    case 2:
        n = int(input('em quantos minutos? '))
        m = n * 60
        print (os.system(f'shutdown -s -f -t {m}'))
        print(f'o pc vai desligar em {n} minutos')

    case 3:
        n = int(input('em quantas horas? '))
        h = n * 3600
        print (os.system(f'shutdown -s -f -t {h}'))
        print(f'o pc vai desligar em {n} horas')
    case 0:
        print ('tem certeza que deseja desligar nesse exato momento? ')
        es = str (input ('S/N: ')).upper()
        if es == 'S': 
            print (os.system('shutdown -s -f -t 0'))
    case 4:

        print (os.system('shutdown -a'))

