pip install --upgrade watson-developer-cloud

import json
from watson_developer_cloud import DocumentConversionV1

document_conversion = DocumentConversionV1(
  username='{username}',
  password='{password}',
  version='2015-12-15'
)

Catching an error
from watson_developer_cloud import DocumentConversionV1

document_conversion = DocumentConversionV1(
  username='{username}',
  password='{password}',
  version='2015-12-15'
)

try:
  # Your code goes here
except WatsonException as e:
  print e

  convert_document(document, config, media_type=None)

  Example request
import json
from watson_developer_cloud import DocumentConversionV1

document_conversion = DocumentConversionV1(
  username='{username}',
  password='{password}',
  version='2015-12-15'
)

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

with open(('sample-docx.docx'), 'r') as document:
  response = document_conversion.convert_document(document=document, config=config)
  print(json.dumps(response, indent=2))

  Example response
{
  "source_document_id": "",
  "timestamp": "2015-10-12T20:16:15.535Z",
  "media_type_detected": "application/pdf",
  "metadata": [{
    "name": "publicationdate",
    "content": "2015-07-18"
  }],
  "answer_units": [{
    "id": "de93c979-414b-4967-afd5-21eafeaedf69",
    "type": "regular",
    "title": "Title from your document 1",
    "content": [{
      "media_type": "text/plain",
      "text": "Text from your document 2"
    }]
  }, {
    "id": "f3702667-9133-4e9d-a639-fbfc70822b9c",
    "type": "regular",
    "title": "Title from your document 3",
    "content" :[{
      "media_type": "text/plain",
      "text": ""
    }]
  }],
  "warnings": []
}