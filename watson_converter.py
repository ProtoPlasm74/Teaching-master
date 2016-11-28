import json
from watson_developer_cloud import DocumentConversionV1

document_conversion = DocumentConversionV1(
  url = "https://gateway.watsonplatform.net/document-conversion/api",
  password='3QKUJFXDg1GK',
  username='6898f353-4f93-4a45-ab5f-7e0c73dd252d',
  version='2015-12-15'
)
  # Catch any issues with the file here
try:
  # Your code goes here
except WatsonException as e:
  print e
  
config = {
  'conversion_target': 'ANSWER_UNITS',
  # Use a custom configuration.
  'word': {
    'heading': {
      'fonts': [
        {'level': 1, 'min_size': 24},
        {'level': 2, 'min_size': 16, 'max_size': 24}
      ]
    }
  }
}

with open(('/Users/zacmorgan/Downloads/Managing for Success.pdf'), 'r') as document:
  response = document_conversion.convert_document(document=document, config=config)
  print(json.dumps(response, indent=2))