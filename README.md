# Very-Simple-USB-Relay
A Python 3 module for getting/setting the state of USB Relays. 
![Image of USB Relay](asset.jpg?raw=true)
Specifically, these relays are purchased usually from EBay and come from a Chinese manufacturer. They have Songle relays, or look alikes (ex: CNTENGFEI).

These relays use the USB-HID specification (Human interface device) for communication. 

There are other python modules out there for controlling these relays, however, I needed to be able to get the state as well as set the state, something the other modules didn't offer.

Also, I am not familiar with communicating with HIDs, and found the other modules confusing and wanted to create something easier to understand.

This does NOT work on Windows 7 (and likely other versions of Windows).  It appears that the OS does not allow the get_feature_report() and send_feature_report() methods.  If you are able to get this working on Windows, please let me know.

# Dependencies
This module depends on the [hidapi module](https://github.com/trezor/cython-hidapi), which can be installed with the following:

    sudo apt-get install python-dev libusb-1.0-0-dev libudev-dev
    pip install --upgrade setuptools
    pip install hidapi

# udev rule
In linux you may need to create a udev rule in order to use this without sudo privileges.

For example, edit /etc/udev/rules.d/99-usbrelay.rules and add this line:
	
	SUBSYSTEM=="usb", ATTR{idVendor}=="16c0", ATTR{idProduct}=="05df", MODE="777"

Then restart your computer or run this command:
	
	sudo udevadm control --reload-rule

# Usage
Then save the relay.py in your projects folder and:

	from relay import Relay
	from time import sleep

	# Create a relay object, using the vendor/product, which you can find with `lsusb`,
	# then just add the 0x prefix. The id/vendor pair below are the default parameters,
	# so you can try to instantiate with Relay() and hope you are lucky.
	relay = Relay(idVendor=0x16c0, idProduct=0x05df)

	# (Setter) Turn switch 1 on
	relay.state(1, on=True)

	# (Getter) Print the status of switch 1 (returns True/False)
	print(relay.state(1))

	# This is just here so you hear a audible 'click' when the relay trips
	sleep(1)

	# Turn all switches off
	relay.state(0, on=False)

	# Print the state of all switches (returns a list of True/False 
	# per relay)
	print(relay.state(0))
