#!/usr/bin/env python
# -*- coding: utf8 -*-
#
#    Copyright 2014,2018 Mario Gomez <mario.gomez@teubi.co>
#
#    This file is part of MFRC522-Python
#    MFRC522-Python is a simple Python implementation for
#    the MFRC522 NFC Card Reader for the Raspberry Pi.
#
#    MFRC522-Python is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    MFRC522-Python is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with MFRC522-Python.  If not, see <http://www.gnu.org/licenses/>.
#

import RPi.GPIO as GPIO
import MFRC522
import signal
import sys
from client import Spotify
import util as util
from scope_builder import ScopeBuilder
import pickle
from auth_values import CLIENT_ID
from auth_values import CLIENT_SECRET
from auth_values import REDIRECT_URL

store = {}
try:
    with open('store.pkl', 'rb') as f:
        store = pickle.load(f)
except:
    print("No existing store")

store['test_id'] = "spotify:user:andrew_walker2:playlist:6VXKlqxCX4ItIHWgFT9I6c"

scope = ScopeBuilder().library().spotify_connect().get_scopes()

if len(sys.argv) > 1:
	username = sys.argv[1]
else:
	print("Usage: %s username" % (sys.argv[0],))
	sys.exit()

token = util.prompt_for_user_token(username, scope, client_id=CLIENT_ID, client_secret=CLIENT_SECRET,
                                   redirect_uri=REDIRECT_URL)

device = None

if token:
	sp = Spotify(auth=token)
	devices = sp.devices()
	devices = devices['devices'][0]['id']
else:
    	print("Can't get token for", username)

continue_reading = True and devices != None

# Capture SIGINT for cleanup when the script is aborted
def end_read(signal,frame):
    	global continue_reading
    	print "Ctrl+C captured, ending read."
    	continue_reading = False
    	GPIO.cleanup()

# Hook the SIGINT
signal.signal(signal.SIGINT, end_read)

# Create an object of the class MFRC522
MIFAREReader = MFRC522.MFRC522()

# Welcome message
# print "Welcome to the MFRC522 data read example"
# print "Press Ctrl-C to stop."

# This loop keeps checking for chips. If one is near it will get the UID and authenticate
while continue_reading:
    
    	# Scan for cards    
    	(status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

    	# If a card is found
    	# if status == MIFAREReader.MI_OK:
        	# print "Card detected"
    
    	# Get the UID of the card
    	(status,uid) = MIFAREReader.MFRC522_Anticoll()

    	# If we have the UID, continue
    	if status == MIFAREReader.MI_OK:

        	# Print UID
        	print "Card read UID: %s,%s,%s,%s" % (uid[0], uid[1], uid[2], uid[3])
    
		uid = "%s%s%s%s" % (uid[0], uid[1], uid[2], uid[3])

		if store.__contains__(uid):
			sp.play_track(store[uid], device)
		else:
			url = raw_input("Please enter a Spotify URL: ")
			store[uid] = url
	
with open('store.pkl', 'wb') as f:
    pickle.dump(store, f, pickle.HIGHEST_PROTOCOL)
