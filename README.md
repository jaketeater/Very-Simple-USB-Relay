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

For example, edit /etc/udev/rules.d/99-usbrelay.rules and add this line: (Information available: Linux command `lsusb`, MacOs command: `ioreg -p IOUSB -l -w 0`)
	
	SUBSYSTEM=="usb", ATTR{idVendor}=="16c0", ATTR{idProduct}=="05df", MODE="777"

Then restart your computer or run this command:
	
	sudo udevadm control --reload-rule

# Usage
Then save the relay.py in your projects folder and:

    run command:
    - Turn On/Off all port in relay 
    python relay.py --port 0 --switch True/False
    - Turn On/Off 1-8 port in relay 
    python relay.py --port 1-8 --switch True/False
    - Show status relay
    python relay.py --port 0-8 (0 - all status, 1-8 - port status)
