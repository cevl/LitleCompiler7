import json
import re
import os

file = open("codigo_fuente.txt")

operators = {'=' : 'Assignment op','+' : 'Addition op','-' : 'Subtraction op',
             '/' : 'Division op','*' : 'Multiplication op','<' : 'Lessthan op','>' : 'Greaterthan op' }
operators_key = operators.keys()

data_type = {'ent' : 'integer type', 'flot': 'Floating point' , 'car' : 'Character type', 'grande' : 'long int' }
data_type_key = data_type.keys()

punctuation_symbol = { ':' : 'colon', ';' : 'semi-colon', '.' : 'dot' , ',' : 'comma',
                      '(' : 'Open round bracket', ')' : 'Close round bracket', 
                      '[' : 'Open square bracket', ']' : 'Close square bracket',
                      '{' : 'Open curly bracket', '}' : 'Close curly bracket'}
punctuation_symbol_key = punctuation_symbol.keys()

identifier = {}
identifier_key = identifier.keys()

reserved = ['mientras', 'para', 'romper', 'continuar', 'retornar', 'si',
            'funcion', 'imprimir']

translate = {'mientras' : 'while', 'para' : 'for', 'romper' : 'break', 'continuar' : 'continue',
             'retornar' : 'return', 'si' : 'if', 'funcion' : 'function',
             'imprimir': 'console.log', 'ent' : 'let', 'flot' : 'let', 'car' : 'let',
             'grande' : 'let', '=' : '=', '+' : '+', '-' : '-', '/' : '/', '*' : '*',
             '<' : '<', '>' : '>', ';' : ';', '(' : '(', ')' : ')', '[' : '[',
             '{' : '{', '}' : '}'}

a=file.read()

tokend = []
count=0
program = a.split("\n")
jprogram = []
for line in program:
    count = count + 1
    # print("line#" , count, "\n" , line)
                
    tokens=line.split(' ')
    
    if tokens[0] in data_type_key:
            if tokens[1] not in identifier:
                identifier[tokens[1]] = 'id'
                identifier_key = identifier.keys()
                
    jtokens = []
    for token in tokens:
        if token in operators_key:
            jtokens.append(translate[token])
        elif token in data_type_key:
            jtokens.append(translate[token])
        elif token in punctuation_symbol_key:
            jtokens.append(translate[token])
        elif token in identifier_key:
            jtokens.append(token)
        elif token in reserved:
            jtokens.append(translate[token])
        elif re.match('^[0-9]*$', token):
            jtokens.append(token)
        elif re.match('^"[0-9 a-z A-Z \s]*"$', token):
            jtokens.append(token)
            
            
        if token in operators_key:
            tokend.append({'Tipo': operators[token], 'Valor' : translate[token]})
        elif token in data_type_key:
            tokend.append({'Tipo': data_type[token], 'Valor' : translate[token]})
        elif token in punctuation_symbol_key:
            tokend.append({'Tipo': punctuation_symbol[token], 'Valor' : translate[token]})
        elif token in identifier_key:
            tokend.append({'Tipo': 'id', 'Valor' : token})
        elif re.match('^[0-9]+$', token):
            tokend.append({'Tipo': 'entero', 'Valor' : token})
        elif re.match('^"[0-9 a-z A-Z]*"$', token):
            tokend.append({'Tipo': 'caracteres', 'Valor' : token})
        elif re.match('^[0-9]+.[0-9]+$', token):
            tokend.append({'Tipo': 'flotante', 'Valor' : token})
        elif token in punctuation_symbol_key:
            tokend.append({'Tipo': punctuation_symbol[token], 'Valor': token})
        elif token in reserved:
            tokend.append({'Tipo': 'reserved', 'Valor': translate[token]})
    
    jprogram.append(jtokens);
   
    
with open('Generated_code.js', 'w') as js:
    for line in jprogram:
        for token in line:
            js.write(token)
            js.write(' ')
        js.write('\n')

json_object = json.dumps(tokend, indent = 4)
with open("Transformed.json", "w") as outfile:
    outfile.write(json_object)

try: os.remove('temp.json')
except: print('...')
def translate(token):
    jtoken = translate[token]
    return jtoken
