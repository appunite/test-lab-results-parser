from xml.dom import minidom
import os
# resultsDir = '/Users/piotrmadry/Desktop/work/reports/firebase-test-lab/hammerhead-21-en-portrait/test_result_3697305487943705087.xml'
# DOMTree = minidom.parse(resultsDir)
# print DOMTree.toxml()

def iterateThroughResults():
	resultsDir = '/Users/piotrmadry/Desktop/work/reports/firebase-test-lab/'
	for subdir, dirs, files in os.walk(resultsDir):
        	for file in files:
        		filePath = os.path.join(subdir, file)
        		if (filePath.endswith('.xml')):
        			DOMTree = minidom.parse(filePath)
        			print DOMTree.toxml()
	pass

iterateThroughResults()