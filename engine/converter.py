import json
from watson_developer_cloud import DocumentConversionV1
import datetime


class ConvertDoc():
		document_conversion = DocumentConversionV1(
		  username='https://gateway.watsonplatform.net/document-conversion/api',
		  password='6898f353-4f93-4a45-ab5f-7e0c73dd252d',
		  version='2015-12-15'
		)

		config = {
		  'conversion_target': 'ANSWER_UNITS',
		  # Use a custom configuration.
		  #Configur
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

		with open(('sample-docx.docx'), 'r') as document:
		  response = document_conversion.convert_document(document=document, config=config)
		  print(json.dumps(response, indent=2))

		  #finding the time and parsing with chrono time/date parser needs to be done