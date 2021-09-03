import os

RUNTIME_TYPE_NONE			= 0
RUNTIME_TYPE_DEVELOPMENT	= 1
RUNTIME_TYPE_LOCAL			= 2
RUNTIME_TYPE_TEST			= 3
RUNTIME_TYPE_PRODUCTION		= 4

def runtime_to_string (runtype):
	if (RUNTIME_TYPE_DEVELOPMENT == runtype):
		return "Development"
	if (RUNTIME_TYPE_LOCAL == runtype):
		return "Local"
	if (RUNTIME_TYPE_TEST == runtype):
		return "Test"
	if (RUNTIME_TYPE_PRODUCTION == runtype):
		return "Production"

	return "None"

def runtime_from_string (value):
	if ("development" == value):
		return RUNTIME_TYPE_DEVELOPMENT
	if ("local" == value):
		return RUNTIME_TYPE_LOCAL
	if ("test" == value):
		return RUNTIME_TYPE_TEST
	if ("production" == value):
		return RUNTIME_TYPE_PRODUCTION

	return RUNTIME_TYPE_NONE
