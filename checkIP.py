## importing socket module
import socket


## getting the hostname by socket.gethostname() method
def sendMail():
    import smtplib
    global emailList
    gmail_password = 'YOUR GMAIL PASSWORD'
    #sender mail ved høy eller lav temperatur
    gmail_user = 'YOUR EMAIL TO SEND FROM'
    sent_from = gmail_user
    to = emailList #sender email til alle i emaillisten
    subject = 'RASPBERRY PI IP DEVICE INFO'
    body = """
Hostname er : %s 
Ip adresse er er : %s 
    """ % (hostname, ipAdresse)

    email_text = """\
From: %s
To: %s
Subject: %s
%s
    """ % (sent_from, ", ".join(to), subject, body)
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, email_text)
        server.close()
        print('Email sent! Current email list is: ', emailList)
    except:
        print('Something went wrong...')



## Getting the hostname of the device using socket.gethostname() method # Test commit
hostname = socket.gethostname()

## getting the IP address using socket.gethostbyname() method
ip_address = socket.gethostbyname(hostname)
ipv4 = socket.gethostbyname(socket.gethostname())

## Gets ip address of raspberry pi device
ipAdresse = [l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1],
 [[(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close())
for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) if l][0][0]

## printing the hostname and ip_address
print(f"Hostname: {hostname}")
print(f"IP Address: {ip_address}")
print(ipAdresse)

emailList = [
    "EMAILS TO SEND TO",
]
sendMail()

