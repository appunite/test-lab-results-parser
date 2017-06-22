import os
import re
import codecs, json
import time
import xml.etree.ElementTree as ET
from model import Device, Test


def prepareTestList(files, subdir):
	testList = []
	for file in files:
	        filePath = os.path.join(subdir, file)
	        if (filePath.endswith('.xml')):
	        	document = ET.parse(filePath)
	        	root = document.getroot()
			for testcase in root.findall('testcase'):
				name = testcase.attrib['name']
				duration = testcase.attrib['time']
				failure = testcase.find('failure')

				regex = re.compile("([a-zA-Z]+)_([a-zA-Z]+)_([0-9]+)")
				match = regex.match(str(name))
				testId = "_".join(match.groups())
				uid = match.group(3)
				steps = getStepsForTest(testId, subdir)

				if failure is None:
					test = Test(name, uid, duration, "", steps, False)
					testList.append(test)
				else:
					test = Test(name, uid, duration, failure.text[:200], steps, True)
					testList.append(test)

	return testList

def getDeviceMeta(subdir):
	return os.path.basename(subdir).split('-')

def getStepsForTest(testId, subdir):
	steps = []
	file = open(os.path.join(subdir, 'logcat'))
	for line in file:
		if 'I/' + testId in line:
			steps.append(line.split("): ", 1)[1])
	file.close()
	return steps

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
			testList = prepareTestList(files, subdir)
			if testList:
				deviceMeta = getDeviceMeta(subdir)
				device = Device(deviceMeta[0], build, version, pipeline, deviceMeta[3], deviceMeta[2], "00:00", date, commiter, "Android, " + deviceMeta[1], testList)
				testResults.append(device)

	return testResults
