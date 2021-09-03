import os

from runtime import *

RUNTIME = runtime_from_string (os.environ.get ("RUNTIME"))

PORT = int (os.environ.get ("PORT"))

CERVER_RECEIVE_BUFFER_SIZE = int (os.environ.get ("CERVER_RECEIVE_BUFFER_SIZE"))
CERVER_TH_THREADS = int (os.environ.get ("CERVER_TH_THREADS"))
CERVER_CONNECTION_QUEUE = int (os.environ.get ("CERVER_CONNECTION_QUEUE"))

def service_config ():
	print ("RUNTIME: ", runtime_to_string (RUNTIME))

	print ("PORT: ", PORT)

	print ("CERVER_RECEIVE_BUFFER_SIZE: ", CERVER_RECEIVE_BUFFER_SIZE)
	print ("CERVER_TH_THREADS: ", CERVER_TH_THREADS)
	print ("CERVER_CONNECTION_QUEUE: ", CERVER_CONNECTION_QUEUE)
