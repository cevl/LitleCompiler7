import analizador_sintactico as sintac
import re
import json

operators = {'=' : 'Assignment op','+' : 'Addition op','-' : 'Subtraction op','/' : 'Division op','*' : 'Multiplication op','<' : 'Lessthan op','>' : 'Greaterthan op' }
identifier = sintac.identifier
symbol_table = sintac.symbol_table
# print(identifier)
# print(symbol_table)

# sp = []


with open('temp.json', 'r') as openfile:
    program = json.load(openfile)
    
    count = 0
    for line in program:
        # sp.append([])
        count += 1
        print('Line# ', count, '\n')
        
        left = ''
        right = ''
        operator = ''
        for token in line:
            if token in identifier.keys():
                # sp[count-1].append(token)
                if left == '':
                    left = symbol_table[token]
                else:
                    right = symbol_table[token]
                    if left == 'char' and symbol_table[token] != 'char':
                        if operator == '=':
                            print('No puedes asignar un valor numerico a un char')
                        else:
                            print('No puedes hacer una operacion entre un char un valor numerico')
                    elif left != 'char' and symbol_table[token] == 'char':
                        if operator == '=':
                            print('No puedes asignar caracteres a una variable numerica')
                        else:
                            print('No puedes hacer una operacion entre un valor numerico y un char')
            elif token in operators.keys():
                if operator != '':
                    left = right
                operator = token

