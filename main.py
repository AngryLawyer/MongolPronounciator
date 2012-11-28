#!/usr/bin/env python
# -*- coding: UTF8 -*-

# Do stuff!
import transposer

# NOTE: the API we're using will be like so: http://mn.wikipedia.org/w/api.php?format=xml&action=query&list=random&prop=revisions&rvprop=content then get the actual article by ID
# http://mn.wikipedia.org/w/api.php?action=query&prop=revisions&rvlimit=1&rvprop=content&format=xml&pageids=19494

trans = transposer.Transposer()
print trans.transpose_string(u'Википедиад тавтай морилно уу.')
