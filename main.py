#!/usr/bin/env python
# -*- coding: UTF8 -*-

# Do stuff!
import transposer

# NOTE: the API we're using will be like so: http://mn.wikipedia.org/w/api.php?format=xml&action=query&list=random&prop=revisions&rvprop=content then get the actual article by ID

trans = transposer.Transposer()
print trans.transpose_string(u'Википедиад тавтай морилно уу.')
