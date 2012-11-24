#!/usr/bin/env python
# -*- coding: UTF8 -*-

# Do stuff!
table = {
    u'A':'A',
    u'Б':'B',
    u'В':'W',
    u'Г':'G',
    u'Д':'D',
    u'Е':'YE',
    u'Ё':'YO',
    u'Ж':'J',
    u'З':'Z',
    u'И':'I',
    u'Й':'I',
    u'К':'K',
    u'Л':'L',
    u'М':'M',
    u'Н':'N',
    u'О':'O',
    u'Ө':'O',
    u'П':'P',
    u'Р':'R',
    u'С':'S',
    u'Т':'T',
    u'У':'U',
    u'Ү':'U',
    u'Ф':'F',
    u'Х':'KH',
    u'Ц':'TS',
    u'Ч':'CH',
    u'Ш':'SH',
    u'Щ':'SHCH',
    u'ъ':'',
    u'ы':'IH',
    u'ь':'',
    u'Э':'E',
    u'Ю':'YU',
    u'Я':'YA',
    u'а':'a',
    u'б':'b',
    u'в':'w',
    u'г':'g',
    u'д':'d',
    u'е':'ye',
    u'ё':'yo',
    u'ж':'j',
    u'з':'z',
    u'и':'i',
    u'й':'i',
    u'к':'k',
    u'л':'l',
    u'м':'m',
    u'н':'n',
    u'о':'o',
    u'ө':'o',
    u'п':'p',
    u'р':'r',
    u'с':'s',
    u'т':'t',
    u'у':'u',
    u'ү':'u',
    u'ф':'f',
    u'х':'kh',
    u'ц':'ts',
    u'ч':'ch',
    u'ш':'sh',
    u'щ':'shch',
    u'э':'e',
    u'ю':'yu',
    u'я':'ya'
}

def lookup(char):
    if char in table:
        return table[char]
    return char

def transpose_string(input_string):
    return ''.join(map(lookup,list(input_string)))

print transpose_string(u'Википедиад тавтай морилно уу.')
