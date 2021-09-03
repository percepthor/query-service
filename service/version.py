from cerver.utils import LOG_TYPE_NONE, cerver_log_both

SERVICE_VERSION = "0.1"
SERVICE_VERSION_NAME = "Version 0.1"
SERVICE_VERSION_DATE = "01/09/2021"
SERVICE_VERSION_TIME = "23:57 CST"
SERVICE_VERSION_AUTHOR = "Erick Salas"

def service_version_print_full ():
	cerver_log_both (
		LOG_TYPE_NONE, LOG_TYPE_NONE,
		"\nService Version: %s".encode ('utf-8'),
		SERVICE_VERSION_NAME.encode ('utf-8')
	)

	cerver_log_both (
		LOG_TYPE_NONE, LOG_TYPE_NONE,
		"Release Date & time: %s - %s".encode ('utf-8'),
		SERVICE_VERSION_DATE.encode ('utf-8'),
		SERVICE_VERSION_TIME.encode ('utf-8')
	)

	cerver_log_both (
		LOG_TYPE_NONE, LOG_TYPE_NONE,
		"Author: %s\n".encode ('utf-8'),
		SERVICE_VERSION_AUTHOR.encode ('utf-8')
	)

def service_version_print_version_id ():
	cerver_log_both (
		LOG_TYPE_NONE, LOG_TYPE_NONE,
		"\nService Version ID: %s\n".encode ('utf-8'),
		SERVICE_VERSION.encode ('utf-8')
	)

def service_version_print_version_name ():
	cerver_log_both (
		LOG_TYPE_NONE, LOG_TYPE_NONE,
		"\nService Version: %s\n".encode ('utf-8'),
		SERVICE_VERSION_NAME.encode ('utf-8')
	)
