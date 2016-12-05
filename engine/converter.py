import json
from watson_developer_cloud import DocumentConversionV1


class ConvertDoc():
		document_conversion = DocumentConversionV1(
		  username='{username}',
		  password='{password}',
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