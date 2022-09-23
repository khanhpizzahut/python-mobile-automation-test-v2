from Utilities.configReader import readConfig
from Utilities.testrail import *

testRunid = readConfig("config", "latest_test_run_id")
case_id = "2136"
print(testRunid)
print(get_testcaseid_ontestrun(testRunid,case_id))
#post_result_baseon_testcase_id(get_testcaseid_ontestrun(testRunid,case_id),"Passed","")