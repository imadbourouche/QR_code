
# Python code to illustrate Sending mail with qr code as attachment
# from your Gmail account 
  
# libraries to be imported
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import qrcode
import pandas as pd

#Open the excel file that contains the contacts
#You can find an exmeple here : https://docs.google.com/spreadsheets/d/1Ec8IBmBUPR23h5oXaETNc-onEYatP0DY2bewq86mxVo/edit?usp=sharing
data=pd.read_excel('contact.xlsx')

for f in data.values:
    
    fromaddr = "Your email goes here"
    toaddr = f[1]
       
    # instance of MIMEMultipart
    msg = MIMEMultipart()
      
    # storing the senders email address  
    msg['From'] = fromaddr
      
    # storing the receivers email address 
    msg['To'] = toaddr
      
    # storing the subject 
    msg['Subject'] = "your email's subject goes here"
      
    # string to store the body of the mail
    body = "Your body goes here"
      
    # attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))
      
    
    
    # example data
    data = f[0]
    # output file name
    filename = f[2]+".png"
    # generate qr code
    img = qrcode.make(data)
    # save img to a file
    img.save("images/"+filename)
    
    # open the file to be sent 
    filename = filename
    attachment = open("images/"+filename, "rb")
      
    # instance of MIMEBase and named as p
    p = MIMEBase('application', 'octet-stream')
      
    # To change the payload into encoded form
    p.set_payload((attachment).read())
      
    # encode into base64
    encoders.encode_base64(p)
       
    p.add_header('Content-Disposition', "attachment; filename= %s" %filename)
      
    # attach the instance 'p' to instance 'msg'
    msg.attach(p)
      
    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)
      
    # start TLS for security
    s.starttls()
      
    # Authentication
    s.login(fromaddr, "Your password goes here")
      
    # Converts the Multipart msg into a string
    text = msg.as_string()
      
    # sending the mail
    s.sendmail(fromaddr, toaddr, text)
    print(f)
    # terminating the session
    s.quit()
    


    
