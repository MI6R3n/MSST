#/bin/python2
import smtplib
import time
import getpass
import os

os.system("clear")
print """\n
    To use this feature, you must activate the Google Account Limit to this section
		https://myaccount.google.com/data-and-personalization
		And tick the "Web & App Activity" option """

ti = input("\nEnter Time For Sleeping Script (Secound) >> ")


sender = raw_input("\nEnter Sender Gmail >> ")  

toaddrs = raw_input("\nEnter Target MAil >> ")

message = raw_input("""\nEnter Your Message >>  
 
 """)  

username = raw_input("\nEnter Your Username(Gmail) >> ")

password = getpass.getpass("\nEnter Your Password >> ") 

print ("\n\tWait until the mail arrives")
            
time.sleep(ti)

server = smtplib.SMTP("smtp.gmail.com:587") 
server.starttls() 
server.login( username , password ) 
server.sendmail(sender, toaddrs, message) 
server.quit() 

print "\n\nThe operation was carried out\n\n"
