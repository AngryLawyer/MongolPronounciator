#!/usr/bin/env python
# -*- coding: UTF8 -*-

# Do stuff!
import transposer

# NOTE: the API we're using will be like so: http://mn.wikipedia.org/w/api.php?format=xml&action=query&list=random&prop=revisions&rvprop=content then get the actual article by ID

trans = transposer.Transposer()
print trans.transpose_string(u'Википедиад тавтай морилно уу.')

class Pronounciator(object):
    _transposer = transposer.Transposer()

    def go(self):
        print 'MongolPronounciator'
        print '-------------------'
        print '1: Practice individual characters'
        print '2: Practice words'
        print '3: Practice blocks of text'

        while True:
            user_input = raw_input('? ')
            if user_input == '1':
                pass
            else:
                break



engine = Pronounciator()
engine.go()
