"""TestRail API binding for Python 3.x.

(API v2, available since TestRail 3.0)

Compatible with TestRail 3.0 and later.

Learn more:

http://docs.gurock.com/testrail-api2/start
http://docs.gurock.com/testrail-api2/accessing

Copyright Gurock Software GmbH. See license.md for details.
"""

import base64
import json

import requests

import logging
from Utilities.LogUtil import Logger
log = Logger(__name__, logging.INFO)

class APIClient:
    def __init__(self, base_url):
        self.user = ''
        self.password = ''
        if not base_url.endswith('/'):
            base_url += '/'
        self.__url = base_url + 'index.php?/api/v2/'

    def send_get(self, uri, filepath=None):
        """Issue a GET request (read) against the API.

        Args:
            uri: The API method to call including parameters, e.g. get_case/1.
            filepath: The path and file name for attachment download; used only
                for 'get_attachment/:attachment_id'.

        Returns:
            A dict containing the result of the request.
        """
        return self.__send_request('GET', uri, filepath)

    def send_post(self, uri, data):
        """Issue a POST request (write) against the API.

        Args:
            uri: The API method to call, including parameters, e.g. add_case/1.
            data: The data to submit as part of the request as a dict; strings
                must be UTF-8 encoded. If adding an attachment, must be the
                path to the file.

        Returns:
            A dict containing the result of the request.
        """
        return self.__send_request('POST', uri, data)

    def __send_request(self, method, uri, data):
        url = self.__url + uri

        auth = str(
            base64.b64encode(
                bytes('%s:%s' % (self.user, self.password), 'utf-8')
            ),
            'ascii'
        ).strip()
        headers = {'Authorization': 'Basic ' + auth}

        if method == 'POST':
            if uri[:14] == 'add_attachment':    # add_attachment API method
                files = {'attachment': (open(data, 'rb'))}
                response = requests.post(url, headers=headers, files=files)
                files['attachment'].close()
            else:
                headers['Content-Type'] = 'application/json'
                payload = bytes(json.dumps(data), 'utf-8')
                response = requests.post(url, headers=headers, data=payload)
        else:
            headers['Content-Type'] = 'application/json'
            response = requests.get(url, headers=headers)

        if response.status_code > 201:
            try:
                error = response.json()
            except:     # response.content not formatted as JSON
                error = str(response.content)
            raise APIError('TestRail API returned HTTP %s (%s)' % (response.status_code, error))
        else:
            if uri[:15] == 'get_attachment/':   # Expecting file, not JSON
                try:
                    open(data, 'wb').write(response.content)
                    return (data)
                except:
                    return ("Error saving attachment.")
            else:
                try:
                    return response.json()
                except: # Nothing to return
                    return {}



class APIError(Exception):
    pass


# customise--------------


client = APIClient('https://phdv.testrail.io/')
client.user = 'khanh.pham@yum.com'
client.password = 'phdvR@il123'
# https://www.gurock.com/testrail/docs/api/reference/results/
"""
Mobile: project_id = 1
"""
def create_test_run(name,testcases_id):
    print(type(testcases_id))
    arr_tc_id = list(testcases_id)
    client.send_post(
            'add_run/1',
            {
                'milestone_id': 16,
                'name': "[Automation] "+name,
                'assignedto_id': 4,
                'refs': "",
                'include_all': False,
                'case_ids': arr_tc_id
             }
        )
    log.logger.info("Testrail create test run: [Automation] "+str(name))

def get_latest_test_run_id():
    testruns_dict = client.send_get('get_runs/1') #base on project, 1 is mobile, dict
    testruns_list = testruns_dict.get("runs")  # list
    for testrun_info in testruns_list:
        for x, y in testrun_info.items():
            if (x == "id"):
                log.logger.info("Testrail latest test run id: " + str(y))
                return y


def post_result_baseon_testcase_id(testcase_id, PassedorFailed, comment):
    result_id = 5 # Failed
    if PassedorFailed == "Passed":
       result_id = 1
       comment = "[Automation] - Passed"


    client.send_post(
            'add_result/'+str(testcase_id),
            {'status_id': result_id,
             'comment': '[Automation] - '+comment}
        )
    log.logger.info("Testrail post result testcase id: " + str(testcase_id)+ ", result: "+PassedorFailed)
    """
    ID	Name
    1	Passed
    2	Blocked
    3	Untested
    4	Retest
    5	Failed
    """

def get_testcaseid_ontestrun(testrun_id,case_id): #(73,510)
    testrun_info = client.send_get('get_tests/'+ str(testrun_id))
    testcases_on_testrun = testrun_info.get("tests") # list
    for testcase_info in testcases_on_testrun:
        for x, y in testcase_info.items():
            if(x=="case_id" and y==case_id):
                id = testcase_info["id"]
                log.logger.info("Testrail case_id: "+str(case_id)+", testcase_id: "+str(id))
                return id




#create_test_run("khanh test thu",[510, 511, 512])
#print(get_testcaseid_ontestrun(73,513))
#print(get_newtestrun_baseon_project_mobile())
#create_test_run("moi add vao luon",[510,511])
#print(get_latest_test_run_id()) #76
#print(get_testcaseid_ontestrun(76,510)) # 3352
#post_result(3353,"Passed","Sai qua sai")