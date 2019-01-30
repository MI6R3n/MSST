#/bin/python2
import smtplib
import time
import getpass
import os

os.system("clear")

try :
	print """\n
		To use this feature, you must activate the Google Account Limit to this section
			https://myaccount.google.com/data-and-personalization
			And tick the "Web & App Activity" option """

	ti = input("\n[*] Enter Time For Sleeping Script (Secound) >> ")


	sender = raw_input("\n[*] Enter Sender Gmail >> ")  

	toaddrs = raw_input("\n[*] Enter Target MAil >> ")

	message = raw_input("""\n[*] Enter Your Message >>  
	
	""")  

	username = raw_input("\n[*] Enter Your Username(Gmail) >> ")

	password = getpass.getpass("\n[*] Enter Your Password >> ") 

	os.system('clear')
	
	print ("\n\n\t[*] OK Now Please Wait Until The Mail Arrives ;)")
				
	time.sleep(ti)

	server = smtplib.SMTP("smtp.gmail.com:587") 
	server.starttls() 
	server.login( username , password ) 
	server.sendmail(sender, toaddrs, message) 
	server.quit() 

	print ("\n\n\t\t[*] The Operation Was Carried Out [*] \n\n")
except KeyboardInterrupt :
	print ("[!] You Typed Ctrl + X :(")

except smtplib.SMTPConnectError :

	print ('\n\n[!]Connecting Error Please Cheek Your Internet')
