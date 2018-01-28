# -*- coding: utf-8 -*-
birthday = {
    'João':'04/08/1990',
    'Carlos':'12/11/1986',
    'Felipe':'21/06/1999',
    'Marcia':'09/02/1967',
    'Marcela':'10/10/1988',
    'Pedro':'29/02/1992'
}
print('Welcome to the birthday dictionary. We know the birthdays of:')
print('João')
print('Carlos')
print('Felipe')
print('Marcia')
print('Marcela')
print('Pedro')
name = raw_input("Who's birthday do you want to look up?")
if name in birthday:
    print'The birthday of '+name+' is '+birthday[name]
else:
    splash()
