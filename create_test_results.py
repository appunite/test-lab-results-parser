import os
import xml.etree.ElementTree as ET
from model import Device, Tests, Test

	
def prepareTestLists(files, subdir):
	passedTestList = []
	failedTestList = []
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

	
def getResults(resultsDir):
	testResults = []
	for subdir, dirs, files in os.walk(resultsDir, topdown=True):
			passedTestList, failedTestList = prepareTestLists(files, subdir)
			tests = Tests(passedTestList, failedTestList)
			device = Device("Nexus5", "1000", "1.0", "1000", "en", "10:30", "date", "Piotr Madry", "Android, 7.1", tests)
			if passedTestList or failedTestList:
				testResults.append(device)
        	
	return testResults	

	