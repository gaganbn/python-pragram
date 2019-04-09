#sending mail using python



import smtplib

s=smtplib.SMTP('smtp.gamil.com','587')
s.starttls()
sender='gagangana9739@gmail.com'
receiver='gchaturyar@gamil.com'
msg="hii"
s.login(sender,'gagangana007')
s.sendmail(sender,receiver,msg)
print("msg sent successfully")
s.quit()