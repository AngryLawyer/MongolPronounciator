#!/usr/bin/env python
# -*- coding: UTF8 -*-

import transposer

# NOTE: the API we're using will be like so: http://mn.wikipedia.org/w/api.php?format=xml&action=query&list=random&prop=revisions&rvprop=content then get the actual article by ID

class Pronounciator(object):
    _max = 10
    _transposer = transposer.Transposer()

    def individual_characters(self):
        wins = 0
        print 'Individual characters'
        print '---------------------'
        for i in range(0, self._max):
            (key, value) = self._transposer.random_pair()
            print u'What is '+ key
            user_input = raw_input()
            if user_input == value:
                print 'CORRECT!'
                wins += 1
            else:
                print "WRONG! It's "+value
        print 'You got %(wins)d out of %(max)d' % {'wins': wins, 'max': self._max}


    def go(self):
        print 'MongolPronounciator'

        while True:
            print '-------------------'
            print '1: Practice individual characters'
            print '2: Practice words'
            print '3: Practice blocks of text'
            user_input = raw_input('? ')
            if user_input == '1':
                self.individual_characters()
            else:
                break

Pronounciator().go()
