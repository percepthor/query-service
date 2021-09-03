import ctypes

from cerver.http import HTTP_STATUS_OK
from cerver.http import http_response_json_msg_send
from cerver.http import http_response_json_key_value_send

import version

# GET /api/service
@ctypes.CFUNCTYPE (None, ctypes.c_void_p, ctypes.c_void_p)
def main_handler (http_receive, request):
	http_response_json_msg_send (
		http_receive,
		HTTP_STATUS_OK,
		b"Query Service Works!"
	)

# GET /api/service/version
@ctypes.CFUNCTYPE (None, ctypes.c_void_p, ctypes.c_void_p)
def version_handler (http_receive, request):
	v = '%s - %s' % (version.SERVICE_VERSION_NAME, version.SERVICE_VERSION_DATE)

	http_response_json_key_value_send (
		http_receive,
		HTTP_STATUS_OK,
		b"version", v.encode ('utf-8')
	)

# GET *
@ctypes.CFUNCTYPE (None, ctypes.c_void_p, ctypes.c_void_p)
def service_catch_all_handler (http_receive, request):
	http_response_json_msg_send (
		http_receive,
		HTTP_STATUS_OK,
		b"Query Service!"
	)
