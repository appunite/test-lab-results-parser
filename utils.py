import os
import codecs, json
import time
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
			for testcase in root.findall('testcase'):
				name = testcase.attrib['name']
				uid = 0
				duration = testcase.attrib['time']

				failure = testcase.find('failure')
				if failure is None:
					test = Test(name, uid, duration, "")
					passedTestList.append(test)
				else:
					test = Test(name, uid, duration, failure.text[:200])
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


def getResults(resultsDir, build, version, pipeline, commiter):
	testResults = []
	date = time.strftime('%x')
	for subdir, dirs, files in os.walk(resultsDir, topdown=True):
			passedTestList, failedTestList = prepareTestLists(files, subdir)
			if passedTestList or failedTestList:
				deviceMeta = getDeviceMeta(subdir)
				tests = Tests(passedTestList, failedTestList)
				device = Device(deviceMeta[0], build, version, pipeline, deviceMeta[3], deviceMeta[2], "00:00", date, commiter, "Android, " + deviceMeta[1], tests)
				testResults.append(device)

	return testResults
