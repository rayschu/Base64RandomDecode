#!/usr/bin/env python
import sys
import base64

def base64randomde(cipherfile):
	f = open(cipherfile, 'rb')
	cipher = f.read()
	f.close()
	while (True):
		try:
			decode = base64.b16decode(cipher)
		except TypeError:
			try:
				decode = base64.b32decode(cipher)
			except TypeError:
				try:
					decode = base64.b64decode(cipher)
				except TypeError:
					break
		cipher = decode
	print(decode)
base64randomde(sys.argv[1])
