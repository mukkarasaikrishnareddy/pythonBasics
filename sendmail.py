import smtplib
# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)
# start TLS for security
s.starttls()
# Authentication
s.login("rockstarkid2006@gmail.com","nvlz kzta oirj imrx" )
# message to be sent
message = "subject : rey nene ra puka\n\n This is the end hold ur heart breath nowwww"
# sending the mail
s.sendmail("rockstarkid2006@gmail.com", "sairockstar2006@gmail.com", message)
# terminating the session
s.quit()