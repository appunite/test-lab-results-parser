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
	parser.add_argument('--build', dest='build', required=True, nargs='?', type=str, help='build')
	parser.add_argument('--version', dest='version', required=True, nargs='?', type=str, help='version')
	parser.add_argument('--pipeline', dest='pipeline', required=True, nargs='?', type=str, help='pipeline')
	parser.add_argument('--commiter', dest='commiter', required=True, nargs='?', type=str, help='commiter')
    	args = parser.parse_args()

	results = getResults(args.source, args.build, args.version, args.pipeline, args.commiter)
	createJsonFile(args.destination, toJson(results))

if __name__ == "__main__":
  main()
