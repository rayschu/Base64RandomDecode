#!/usr/bin/env python
import sys
import base64

def base64random(cipherfile, de_times):
	f = open(cipherfile, 'rb')
	cipher = f.read()
	f.close()

	n = int(de_times)
	i = 0
	while ( i < n ):
		try:
			decode = base64.b16decode(cipher)
		except TypeError:
			try:
				decode = base64.b32decode(cipher)
			except TypeError:
				try:
					decode = base64.b64decode(cipher)
				except TypeError:
					pass
		i += 1
		cipher = decode
	print(decode)
base64random(sys.argv[1], sys.argv[2])
