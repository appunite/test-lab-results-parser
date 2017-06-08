import xml.etree.ElementTree as ET
from test import Test
from tests import Tests
from device import Device
from test_results import TestResults
import json
import os

def prepareListOfTestResults():
	resultsDir = '/Users/piotrmadry/Desktop/work/reports/firebase-test-lab/'
	passedTestList = []
	failedTestList = []
	for subdir, dirs, files in os.walk(resultsDir):
        	for file in files:
        		filePath = os.path.join(subdir, file)
        		if (filePath.endswith('.xml')):
        			document = ET.parse(filePath)
        			root = document.getroot()
        			testcase = document.find('testcase')
        			name = testcase.attrib['name']
        			uid = 0

        			test = Test(name, uid)
        			if ((root.attrib['failures'] == '0' and root.attrib['errors'] == '0')):
        				passedTestList.append(test)
        			else:
        				failedTestList.append(test)

	return passedTestList, failedTestList

def parseToJson(passedTestList, failedTestList):
	tests = Tests(passedTestList, failedTestList)
	device = Device("Nexus5", "1000", "1.0", "1000", "en", "10:30", "date", "Piotr Madry", "Android, 7.1", tests)
	testResultsList = []
	testResultsList.append(device)
	testResults = TestResults(testResultsList)
	return json.dumps(testResultsList, default=lambda o: o.__dict__, 
            sort_keys=True, indent = 4)

def main():
  passedTestList, failedTestList = prepareListOfTestResults()
  print len('PASSED: ' + str(len(passedTestList)))
  print len('FAILED: ' + str(len(failedTestList)))
  print parseToJson(passedTestList, failedTestList)

if __name__ == "__main__": 
  main()