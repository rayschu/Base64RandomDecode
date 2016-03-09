#!/usr/bin/env python
import sys
import base64

def base64random(cipherfile):
	f = open(cipherfile, 'rb')
	cipher = f.read()
	f.close()

	i = 2
	while ( i > 1 ):
		try:
			decode = base64.b16decode(cipher)
		except TypeError:
			try:
				decode = base64.b32decode(cipher)
			except TypeError:
				try:
					decode = base64.b64decode(cipher)
				except TypeError:
					i = 0
		cipher = decode
	print(decode)

base64random(sys.argv[1])
