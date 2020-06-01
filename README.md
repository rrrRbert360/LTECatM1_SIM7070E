#Piece-of-Cake Modem debug tooling v1.0

##About
This tool-kit enables you easily to create a LTE-M Internet Of Things Proof-Of-Concept with a Raspberry PI and a SIMCom SIM7070E  which is based on the multi-band multi-mode modem Qualcomm9205.
You can use the preconfigured SD-Card image to test LTE-M connectivity or simply use this SD-image to easilyy add LTE-M connectivity to your own proof of concepts.
A short explanation is shown on: https://youtu.be/YQDOI8ArKjU
More experienced users can use the provided patch-file to create their own kernel.

##Obtain required hardware to get this working
1. Get a evaluation daughter board for the SIMCom SIM7070E and ensure to have the correct firmware for SIM7070E:  firmware 3B05 with USB VID:PID "1e0e:9206 Qualcomm" (Note: check with lsusb)
2. Get a SIMCom EVB V1.02 mother board which you can use in combination with the SIMCom SIM7070E evaluation daughter board
3. Get a RasberryPI zero, 3B+ or 4, an appropriate monitor, adapters, keyboard, mouse and power adapter
4. Ensure to have a RaspberryPI approved 32GB SD card
5. Get a SIMCard from your mobile network operator supporting LTE-CatM1

##Prepare the PoC-setup
1. Download on a computer the zip file https://drive.google.com/file/d/1mbNeSmJKFiF3XHhSEe2lUzAExyxdfzKx
2. Unzip the SD-image file and flash the SD card with the image (follow instructions on https://www.raspberrypi.org)
3. Place the SD-Card in the RasberryPI
4. Connect RaspberryPI pin GPIO21(PIN#40) connected to SIMCom EVB V1.02 pin(A)PWRKEY
5. Connect RaspberryPI GND  (PIN#39) connected to SIMCom EVB V1.02 pin(C)GND
6. Disable a PIN if it is present on the SIMCard (e.g. with a mobile phone)

##How to get this working:
Connect the antenna
Power the modem and Raspberry and give them a minute to boot.
The following steps only need to be done for the first time.
Open Terminal to open the linux prompt and enter 'modem help' to look at the available commands.
Enter the command on the linux prompt: modem at
If the driver is loaded properly, the the programme minicom will start and after you type at the modem must respond with OK.
The modem needs to be set properly for the first time.
The settings are stored in the modems flash memory and used after powering up.
Therefore ensure to set the correct APN to the modem by using the AT-command:
at+cgdcont=1,"IP","[APN]",
(Replace [APN] with the operator provided APN)
Exit minicom by entering: CTRL-A Z and Q
Reboot the RaspberryPI.

##Explanation
After booting the modem is automatically switched on.
This is followed by automaticaly setting up the ppp and
changing the default gateway.
This results in a ppp0 (wwan) connection which you can verify with ifconfig.
Follow the instructions mentioned above for more information.

##Pre-installed tooling for your convenience
tcpdump
ppp
minicom
iperf3
mc

##Enabled services
SSH
VNC
SPI

##Background
Files which might be relevant during debugging:

Booting:
/etc/rc.local
/etc/init.d/modem
/etc/rc2.d/S01modem

Modem_ON toggle used by scripts above:
/usr/local/bin/modem
/home/pi/MODEM_ON_pulse.py

ppp settings:
/etc/ppp/net-chat
/etc/ppp/net-connect
/etc/ppp/options

##Credentials
user:pi
pwd:iotc360

##Notes
Check any updates on the repository LTE-CatM1 SIM7070E at: https://github.com/rrrRbert360/LTECatM1_SIM7070E
Save your data-bundle! Before your install/update any software/firmware ensure to disable the ppp0 interface by performing a modem stop from the terminal.


Robert J. Heerekop
IOTC360   May 2020

-.-
