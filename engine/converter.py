import json
from os.path import join, dirname
from os import environ
from watson_developer_cloud import DocumentConversionV1
import datetime
#import chrono


class ConvertDoc():
		document_conversion = DocumentConversionV1(
		  url= 'https://gateway.watsonplatform.net/document-conversion/api',
		  username='dc03be7f-6189-4dbf-aa20-c96eadf2af62',
		  password='AXrXfupGzIpH',
		  version='2016-02-10'
		)

		config = {
		  'conversion_target': 'NORMALIZED_TEXT',
		  # Use a custom configuration.
		  #http://www.ibm.com/watson/developercloud/doc/document-conversion/customizing.shtml
		  'word': {
		    'heading': {
		      'fonts': [
		        {'level': 1, 'min_size': 24},
		        {'level': 2, 'min_size': 16, 'max_size': 24}
		      ]
		    }
		  }
		}

		with open('uploads/guide.pdf', 'r') as document:
		  response = document_conversion.convert_document(document=document, config=config)
		  print response.text
	    
	    #To pass to next page?
		#def convert_doc()
		#	return response.text


		  #finding the time and parsing with chrono time/date parser needs to be done
		  #https://github.com/wanasit/chrono-python