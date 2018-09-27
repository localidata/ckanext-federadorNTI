# -*- coding: utf-8 -*-
#
# @author	CEMI Malaga
# @email        datosabiertos@malaga.eu
#
#
import re
import ckan.plugins as p
from ckan.lib.base import BaseController

import federador as fed

# imports used on rdf render
#import ckan.lib.accept as accept
from ckan.lib.base import response
from ckan.lib.base import (request,
                           render,
                           BaseController,
                           model,
                           abort, h, c)


class GenerarRDF(BaseController):


	def generar(self,fname, template):

		import os
		import sys
		
			
		datardf = render(template)
		datardf = datardf.encode('utf-8')	
		patron = re.compile(" lang=\"..\" ")  
		datardf = patron.sub(" ",datardf)		
		
		try:
			with open(fname, 'w') as f:
				f.write(datardf)
				return p.toolkit.literal("proceso correcto")
		except IOError, ioe:
			sys.stderr.write( "Error !!!!! " + str(ioe) + "\n" )
			return p.toolkit.literal("error " + str(ioe))

