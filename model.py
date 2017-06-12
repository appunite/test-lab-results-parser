class Device(object):

	device = ""
	build = ""
	version = ""
	pipeline = ""
	orientation = ""
	lang = ""
	duration = ""
	start_date = ""
	commiter = ""
	device_meta = ""
	tests = []

	def __init__(self, device, build, version, pipeline, orientation, lang, duration, start_date, commiter, device_meta, tests):
		self.device = device
		self.build = build
		self.version = version
		self.pipeline = pipeline
		self.orientation = orientation
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
	duration = ""
	fail_reason = ""

	def __init__(self, name, uid, duration, fail_reason):
		self.name = name
		self.uid = uid
		self.duration = duration
		self.fail_reason = fail_reason
