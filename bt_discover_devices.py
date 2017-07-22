#require to intall "pybluez" python package

import bluetooth

nearby_devices = bluetooth.discover_devices(lookup_names=True)

print "found %d devices" %len(nearby_devices)

for name,addr in nearby_devices:
	print "%s %s" %(name,addr)
