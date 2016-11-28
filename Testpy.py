from .watson_developer_cloud_service import WatsonDeveloperCloudService
import os
import json


class DocumentConversionV1(WatsonDeveloperCloudService):
    DEFAULT_URL = 'https://gateway.watsonplatform.net/document-conversion/api'
    ANSWER_UNITS = 'answer_units'
    NORMALIZED_HTML = 'normalized_html'
    NORMALIZED_TEXT = 'normalized_text'
    latest_version = '2016-02-10'

    def __init__(self, version, url=DEFAULT_URL, **kwargs):
        WatsonDeveloperCloudService.__init__(self, 'document_conversion', url, **kwargs)
        self.version = version

        def convert_document(self, document, config, media_type=None):
            params = {'version': self.version}
            filename = os.path.basename(document.name)
            file_tuple = (filename, document, media_type) if media_type else (filename, document)
            files = [('file', file_tuple),
            ('config', ('config.json', json.dumps(config), 'application/json'))]
            accept_json = config['conversion_target'] == DocumentConversionV1.ANSWER_UNITS
            return self.request(method='POST', url='/v1/convert_document', files=files, params=params,
                accept_json=accept_json)

            def index_document(self, config, document=None, metadata=None, media_type=None):
                if document is None and metadata is None:
                    raise AssertionError('Missing required parameters: document or metadata. At least one is'
                       'required.')
                    params = {'version': self.version}
                    files = [('config', ('config.json', json.dumps(config), 'application/json'))]
                    if document is not None:
                        filename = os.path.basename(document.name)
                        file_tuple = (filename, document, media_type) if media_type else (filename, document)
                        files.append(('file', file_tuple))
                        if metadata is not None:
                            files.append(('metadata', ('metadata.json', json.dumps(metadata), 'application/json')))
                            return self.request(method='POST', url='/v1/index_document', files=files, params=params, accept_json=True)
