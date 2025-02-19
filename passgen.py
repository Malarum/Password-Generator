#!/usr/bin/python3
import string
import random
import argparse


parser=argparse.ArgumentParser(
	description = '''This is a very simple password generator. If you need a new password this is it''',
	epilog = """Good luck and don't get hacked""")

parser.add_argument('-l','--lowercase', action='store_true', help='Adds lowercase letters to your password')
parser.add_argument('-u','--uppercase', action='store_true', help='Adds uppercase letters to your password')
parser.add_argument('-n','--numbers', action='store_true', help='Adds numbers to your password')
parser.add_argument('-s','--special', action='store_true', help='Adds special characters to your password')
parser.add_argument('-a', '--all', action='store_true', help='Use all of the above')
args=parser.parse_args()


chars = ''

if args.all:
	chars = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

else:
    if args.lowercase:
	    chars += string.ascii_lowercase
    if args.uppercase:
	    chars += string.ascii_uppercase
    if args.numbers:
	    chars += string.digits
    if args.special:
	    chars += string.punctuation


def password_calculator():
	while True:
		pwdstr = ''
		try: 
			password = int(input("Enter the length of the password you would like, up to 50 characters: "))
			while password > 0 and password  < 50:

				for i in range(password):
					pwdstr += random.choice(chars)
				return pwdstr
			
				break
			if password > 50:
				print("Please select a number between 0-50")
				continue
			elif password <= 0: 
				print("Please select a number between 1 and 50")
				continue
			print(pwdstr)
		except ValueError:
			print("that is not a number. please try again.")
		else:
			break

password = password_calculator()
print(password)