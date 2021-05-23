#Configuration details of user 
uname = "Guru HariHaraun"
email = "guru@gmail.com"
district_id = 560 # The 506 is the district code for trichy.
vaccine_type = "COVAXIN" # Either user COVISHIED or COVAXIN All should be in UPPERCASE
fee_type ="Free" # The fee type should be Paid or Free All should be in UPPERCASE
age_limit = 45 # Enter Your Age Here
attempt = 1 # Number of days the application should periodically check
wait_time = 300 # 5 minutes in seconds

#SMTP Email Configuration
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
SMTP_USER_NAME = 'test@gmail.com'
SMTP_PASSWORD = 'qwerty@1234'

#Should Not Modify The variables below
isUserNotified = 0  # Setting up a flag to say that the user has been notified
available_flag_break = 0 # To break the process after notified to user