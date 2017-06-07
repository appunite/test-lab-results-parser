import xml.etree.ElementTree as ET
from Test import Test
import os

def prepareListOfTestResults():
	resultsDir = '/Users/piotrmadry/Desktop/work/reports/firebase-test-lab/'
	testList = []
	for subdir, dirs, files in os.walk(resultsDir):
        	for file in files:
        		filePath = os.path.join(subdir, file)
        		if (filePath.endswith('.xml')):
        			document = ET.parse(filePath)
        			root = document.getroot()
        			print 'Passed: ' + str((root.attrib['failures'] == '0' and root.attrib['errors'] == '0'))
        			testcase = document.find('testcase')
        			print 'Name: ' + testcase.attrib['name'] 

	return testList

def main():
  testList = prepareListOfTestResults()

if __name__ == "__main__": 
  main()