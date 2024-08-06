#!/usr/bin/env python3

### chmod +x 'arquivo.py' (chmod é um comando para alterar a permissão de arquivos )

numero = int(input("Type a number: "))
if numero == 0:
    print("This number is both positive and negative.")
elif numero < 0:
    print("This number is negative.")
else:
    print("This number is positive.")