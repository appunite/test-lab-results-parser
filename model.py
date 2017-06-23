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

class Test(object):

	name = ""
	uid = 0
	duration = ""
	fail_reason = ""
	steps = []
	is_failed = False

	def __init__(self, name, uid, duration, fail_reason, steps, is_failed):
		self.name = name
		self.uid = uid
		self.duration = duration
		self.fail_reason = fail_reason
		self.steps = steps
		self.is_failed = is_failed
