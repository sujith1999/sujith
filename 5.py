#!/usr/bin/python3
import smtplib
s = smtplib.SMTP('smtp.gmail.com',587)
s.starttls()
s.login("sujith1999.s1@gmail.com","sujith10")
message = "hi how r u"
s.sendmail("sujith1999.s1@gmail.com","sujith1999.s1@gmail.com",message)
s.quit()