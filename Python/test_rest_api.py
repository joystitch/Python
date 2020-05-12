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
        if a.headers['Content-Type'] == 'application/json':
            return a.status_code, a.json()
        return a.status_code, a

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

    def get_report(self, resource=None, all_info="false", path='/file/report'):
        if all_info is not 'false':
            all_info = 'all_info={}'.format(all_info)
        if not resource:
            raise Exception('resource is required')
        else:
            resource = 'resource={}'.format(resource)
        path += '?' + resource + '&' + all_info
        status_code, data = self._send_request(method='GET', request_path=path)
        return status_code, data

    def get_artifact(self, sha256=None, path='/file/artifact'):
        if sha256 is None:
            raise Exception("sha256 is required")
        else:
            sha256 = "sha256={}".format(sha256)

        path += '?' + sha256
        status_code, data = self._send_request(method='GET', request_path=path)
        return status_code, data

    def download_detail_report(self, sha256=None, engine=None, env=None, type=None, path='/file/download'):
        download_list = list()
        if sha256 is None:
            raise Exception("sha256 is required")
        else:
            download_list.append("sha256={}".format(sha256))
        if engine is None:
            raise Exception("engine is required")
        else:
            download_list.append("engine={}".format(engine))
        if env is None:
            raise Exception("env is required")
        else:
            download_list.append("env={}".format(env))
        if type is None:
            raise Exception("type is required")
        else:
            download_list.append("type={}".format(type))

        path += '?' + '&'.join(download_list)
        status_code, response = self._send_request(method="GET", request_path=path, stream=True)
        print(status_code)
        print(response)




#test1 = TestCaptureATP('https://10.103.64.233', 'CC5BF0659516', '12199BE87101C49BED0DA3CB16976A49')
test2 = TestCaptureATP('https://10.103.64.202', '123456789ABC', '2813babc6ed843c1a496349f2a53d8db')
#print(test1.scan_file('/home/joy/test.docx'))
#print(test1.get_list(before='1688811393', page_size=10, page_index=0))
#print(test1.get_report(resource='8e8f73493c25d71190bb86ff078062bf', all_info="true"))
#print((test1.get_artifact(sha256='f35fbecb6c6a3bb31eed097365b04877a8ef85e85abdd762327daa0a827ce1fb')))
test2.download_detail_report(sha256='91f335e048e4bcaaea4b4723054a1baad6e43e0321354c20e02e5198dc6f05cd', engine='s', env='win7_amd64', type='pcap')
















