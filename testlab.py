import json
import argparse
from utils import getResults, createJsonFile

def toJson(object):
	return json.dumps(object, default=lambda o: o.__dict__, 
            sort_keys=True, indent = 4)

def main():
	parser = argparse.ArgumentParser(description='Process files paths')
    	parser.add_argument('--source', dest='source', required=True, nargs='?', type=str, help='source')
    	parser.add_argument('--destination', dest='destination', required=True, nargs='?', type=str, help='destination')
    	args = parser.parse_args()

	resultsDir = '/Users/piotrmadry/Desktop/work/reports/firebase-test-lab/'
	destinationPath = '/Users/piotrmadry/Desktop/'

	results = getResults(args.source)
	createJsonFile(args.destination, toJson(results))

if __name__ == "__main__": 
  main()