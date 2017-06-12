import os
import codecs, json
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

def getDeviceMeta(subdir):
	return os.path.basename(subdir).split('-')

def createJsonFile(destinationPath, json):
	if not os.path.exists(destinationPath):
		os.mkdir(destinationPath)
	filePath = os.path.join(destinationPath, 'results.json')
	file = open(filePath, 'w+')
	file.write(json)
	file.close()
	pass


def getResults(resultsDir):
	testResults = []
	for subdir, dirs, files in os.walk(resultsDir, topdown=True):
			passedTestList, failedTestList = prepareTestLists(files, subdir)
			if passedTestList or failedTestList:
				deviceMeta = getDeviceMeta(subdir)
				tests = Tests(passedTestList, failedTestList)
				device = Device(deviceMeta[0], "1000", "1.0", "1000", deviceMeta[3], deviceMeta[2], "10:30", "date", "Piotr Madry", "Android, " + deviceMeta[1], tests)
				testResults.append(device)

	return testResults