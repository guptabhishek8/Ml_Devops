import smtplib 
  
# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587) 
  
# start TLS for security 
s.starttls() 
  
# Authentication 
s.login("email", "password") 
  
# message to be sent 
message = '''Hello, 
				Developer this is an email regarding your last commit. Your last commit was taken into consideration and based on that the trained model has given best accuracy .
				Congratulations on your success.
			THANK YOU ...'''
  
# sending the mail 
s.sendmail("senderemail", "receivemail", message) 
  
# terminating the session 
s.quit() 