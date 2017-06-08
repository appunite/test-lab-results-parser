class Device(object):

	device = ""
	build = ""
	version = ""
	pipeline = ""
	lang = ""
	duration = ""
	start_date = ""
	commiter = ""
	device_meta = ""
	tests = []

	def __init__(self, device, build, version, pipeline, lang, duration, start_date, commiter, device_meta, tests):
		self.device = device
		self.build = build
		self.version = version
		self.pipeline = pipeline
		self.lang = lang
		self.duration = duration
		self.start_date = start_date
		self.commiter = commiter
		self.device_meta = device_meta
		self.tests = tests

class Tests(object):

	passed = []
	failed = []

	def __init__(self, passed, failed):
		self.passed = passed
		self.failed = failed

class Test(object):

	name = ""
	uid = 0

	def __init__(self, name, uid):
		self.name = name
		self.uid = uid
