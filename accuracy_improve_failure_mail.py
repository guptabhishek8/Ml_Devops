import smtplib 
  
# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587) 
  
# start TLS for security 
s.starttls() 
  
# Authentication 
s.login("email", "password")
  
# message to be sent 
message = '''Hello, 
				Developer this is an email regarding your last commit. It seems that your accuracy_improve.py is not working properly please check it once and recommit.
			THANK YOU'''
  
# sending the mail 
s.sendmail("Sender Email", "Receiver Email", message) 
  
# terminating the session 
s.quit() 