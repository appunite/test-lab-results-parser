import xml.etree.ElementTree as ET
from test import Test
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
        			testcase = document.find('testcase')
        			name = testcase.attrib['name']
        			passed = str((root.attrib['failures'] == '0' and root.attrib['errors'] == '0'))
        			uid = 0

        			testList.append(Test(name, uid, passed))

	return testList

def main():
  testList = prepareListOfTestResults()
  print len(testList)

if __name__ == "__main__": 
  main()