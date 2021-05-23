import config
import time
import requests
from datetime import date, timedelta
import smtplib

uname = config.uname
email = config.email
district_id = str(config.district_id)
vaccine_type = config.vaccine_type
fee_type =config.fee_type
age_limit = config.age_limit
if age_limit < 45:
    age_limit = 18
else:
    age_limit = 45

isUserNotified = config.isUserNotified
date_api = []
payload = []
available_flag_break = config.available_flag_break
attempt = config.attempt
wait_time = config.wait_time

def sendmail(payload, email):
    def smtp(email, body):
        print("Sending mail to " + email)
        SMTP_USER_NAME = config.SMTP_USER_NAME
        SMTP_PASSWORD = config.SMTP_PASSWORD
        SMTP_SERVER = config.SMTP_SERVER
        SMTP_PORT = config.SMTP_PORT
        TO = email
        TEXT = body
        SUBJECT = "Automation Message for the COWIN Vaccine Notifier"
    
        smtpserver = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        smtpserver.ehlo()
        smtpserver.starttls()
        smtpserver.ehlo
        smtpserver.login(SMTP_USER_NAME, SMTP_PASSWORD)
        header = 'To:' + TO + '\n' + 'From: ' + SMTP_USER_NAME
        header = header + '\n' + 'Subject:' + SUBJECT + '\n'
        msg = header + '\n' + TEXT + '\n\n'
        smtpserver.sendmail(SMTP_USER_NAME, TO, msg)
        smtpserver.close()
        print("Email sent successfully to " + email)

    def ulify(payload):
        string ="Hi "
        string += uname
        string += "\n\nThis is the automation mail send from COWIN Vaccine Notifier\n\n"
        string += "\n".join([str(s) for s in payload])
        string += "\n\nLink for COWIN Vacination Portal: https://www.cowin.gov.in \nPS: Since your automation was successfully completed, the script was terminated.\n\nThank you for using COWIN Vaccine Notifier."
        return string
    
    body = ulify(payload)
    smtp(email, body)

for ba in range(attempt):
    date_api.append( (date.today()+timedelta(days=ba)).strftime("%d-%m-%Y") ) 

def main():
    global isUserNotified
    global available_flag_break

    while (isUserNotified == 0):
        for b in range(attempt):
            if available_flag_break == 0 or isUserNotified == 0:
                exit

            if available_flag_break == 0 or isUserNotified == 0:
                curl = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id="+district_id+"&date="+str(date_api[b])
                user_agent = {'User-agent': 'Mozilla/5.0'}
                x = requests.get(curl, headers = user_agent)
                data = x.json()
                vax = data['centers']
                for i in vax:
                    for j in i['sessions']:
                        if j['vaccine'] == vaccine_type and i['fee_type'] == fee_type and j['available_capacity'] > 0 and j['min_age_limit'] == age_limit and j['date'] == date_api[b]:
                            count = j['available_capacity']
                            name = i['name']
                            date = j['date']
                            p = "There are ",count," ",vaccine_type," available in ",name," on ",date
                            pp = ''.join(str(p) for p in p)
                            print(p)
                            payload.append(pp)
                            isUserNotified = 1
                            available_flag_break = 1
                            break
                sendmail(payload, email)       
                print("going to sleep for {} minutes.".format(wait_time/60))
                time.sleep(wait_time)
