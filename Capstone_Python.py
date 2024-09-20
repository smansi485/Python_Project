import random
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
#generating a random 6-digit OTP
def generate_otp():
    return str(random.randint(100000,999999))
#sending otp
def send_otp_email(recipient_email, otp):
    smtp_server="smtp.gmail.com"
    smtp_port=587
    sender_email=""
    sender_password=""
    message= MIMEMultipart("alternative")
    subject="The OTP is"
    body= f"Your OTP code is {otp}."
    message= MIMEText(body)
    message['subject']= "The OTP is"
    message['From']= sender_email
    message['To']= recipient_email
    try:
        server =smtplib.SMTP(smtp_server,smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, message.as_string())
        server.quit()
        print("The otp has been sent to given email")
        return True
    except Exception as e:
        print(f"Invalid,Retry: {e}")
        return False
def get_user_input():
    user_otp= input("Enter the OTP you have received:")
    return user_otp
#Verification of OTP
def verify_otp(generate_otp,user_otp):
    return int(generate_otp) == user_otp
def otp_verification_system():
    print("here")
    otp = generate_otp()
    recipient_email= input("Enter your email:")
    send_otp_email(recipient_email, otp)


    max_attempts = 6
    attempts=0

    while attempts<max_attempts:
       user_otp = int(get_user_input())
       if verify_otp(otp,user_otp):
           print("Access Granted!")
           break
       else:
           attempts= attempts+1
           print(f"Incorrect OTP. You have {max_attempts-attempts} attempts left.")
    if attempts== max_attempts: 
       print("Access Denied. no attempts left")

if __name__=="__main__":
    otp_verification_system()

