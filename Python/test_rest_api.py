import requests
import os
from urllib.parse import urljoin


class TestCaptureATP(object):
    def __init__(self, server, sn, api_key, base_url='/external/v1'):
        self.server = server
        self.base_url = base_url
        self.session = requests.session()
        self.session.auth = (sn, api_key)
        self.session.verify = False

    def _send_request(self, request_path, method, files=None, stream=False, timeout=10):
        url = urljoin(self.server, self.base_url + request_path)
        a = self.session.request(method=method, url=url, files=files, timeout=timeout, stream=stream)
        return a.status_code, a.text

    def scan_file(self, file_path, path='/file/scan'):
        if not os.path.isfile(file_path):
            raise Exception('invalid file path')
        with open(file_path, 'rb') as files:
            status_code, data = self._send_request(method="POST", request_path=path,
                                                   files={"filestream": files})
        return status_code, data

    def get_list(self, after=None, before=None, page_size=None, page_index=None, path='/file/list'):
        query_list = list()
        if page_size is not None:
            query_list.append('page_size={}'.format(page_size))
        if page_index is not None:
            query_list.append('page_index={}'.format(page_index))
        if after is not None:
            query_list.append('after={}'.format(after))
        if before is not None:
            query_list.append('before={}'.format(before))
        if query_list:
            path += '?' + '&'.join(query_list)
        status_code, data = self._send_request(method="GET", request_path=path)
        return status_code, data



test1 = TestCaptureATP('https://10.103.64.239', 'CC253095D93E', '1434577867A553A91CDA23AD755AF528')
#test1.scan_file('/home/joy/test.docx')
print(test1.get_list(before='1688811393', page_size=10, page_index=0))
















