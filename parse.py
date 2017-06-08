import json
from create_test_results import getResults

def toJson(object):
	return json.dumps(object, default=lambda o: o.__dict__, 
            sort_keys=True, indent = 4)

def main():
	resultsDir = '/Users/piotrmadry/Desktop/work/reports/firebase-test-lab'
	results = getResults(resultsDir)
	print toJson(results)

if __name__ == "__main__": 
  main()