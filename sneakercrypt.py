""" sneakercrypt.py: Unbreakable encryption for the masses. """
__author = "Ken Newcomb"
import sys
from modules import pads, gen, crypto

def usage():
	logo()
	print("Usage: python3 sneakercrypt.py <command>")
	print("Available commands:")
	print("\t1.) pads     - View your stored pads")
	print("\t2.) generate - Generate one-time-pad (outpad)")
	print("\t3.) encrypt  - Encrypt message with outpad")
	print("\t4.) decrypt  - Decrypt message with inpad\n")
	print("OTP Cryptography requires two pads:")
	print("\tinpads  - Used to decrypt incoming messages. Place your friend's generated pads in your ./inpads/ folder.")
	print("\toutpads - Used to encrypt outgoing messages. Generate one to give to a friend with the \"generate\" command.")
	exit()

def logo():
	print("""                         _                                      
   ()                   | |                                     
   /\  _  _    _   __,  | |   _   ,_    __   ,_           _ _|_ 
  /  \/ |/ |  |/  /  |  |/_) |/  /  |  /    /  |  |   | |/ \_|  
 /(__/  |  |_/|__/\_/|_/| \_/|__/   |_/\___/   |_/ \_/|/|__/ |_/
                                                     /|/|       
                                                     \|\|   
             Unbreakable Encryption for the Masses.\n """)
# Sanitize input
if len(sys.argv) != 2:
	usage()

# Get mode, take appropriate action
mode = sys.argv[1]
if mode == 'pads' or mode == '1':
	pads.printPads()
elif mode == 'generate' or mode == '2':
	gen.genPad()
elif mode == 'encrypt' or mode == '3':
	pad_exists = pads.printPads('outpad')
	if pad_exists:
		name = input("Please choose an outpad to encrypt your message: ")
		crypto.encrypt(pads.getPad(name, 'outpad'))
		pads.chop(name, 'outpad')
	else:
		print("There are no outpads. Generate one.")
elif mode == 'decrypt' or mode == '4':
	pad_exists = pads.printPads('inpad')
	if pad_exists:
		name = input("Please choose an inpad to decrypt your message: ")
		crypto.decrypt(pads.getPad(name, 'inpad'))
		pads.chop(name, 'inpad')
	else:
		print("There are no inpads. Obtain one from a friend.")
else:
	usage()
