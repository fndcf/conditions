#!/usr/bin/env python3

### chmod +x 'arquivo.py'(chmod é um comando para alterar a permissão de arquivos )

password_input = str(input())
password = "Python is awesome"

if password_input == password:
    print("ACCESS GRANTED")
else:
    print("ACCESS DENIED.")