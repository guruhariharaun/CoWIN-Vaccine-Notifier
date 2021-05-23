<h1 align="center">
  <img src="https://ik.imagekit.io/guruhariharaun/github/CoWIN_Vaccine_Notifier/header.png" alt="CoWIN Vaccine Notifier" width ="500"/><br>
CoWIN Vaccine Notifier
</h1>

CoWIN Vaccine Notifier is a python based alert bot that checks the https://www.cowin.gov.in/ periodically and if the vaccination slot was available it may send the email alert.

**NOTE:** This application is only for educational purpose. Should not use it for any Illegal trades, denial of service and I&apos;m not responsible for the future consequences, all the risk should be taken by yourself. Also please consider the current situation happening in the country. People who first and seriously needed are finding it difficult to get a vaccine so please feel curtesy before using this application.

## Deployment
**Note:** The application is hosted on heroku's free tier so you can't perform any process. The main aim for the deployment is to show how would the frontend looks like. If you need so then clone the repository from **[here](https://github.com/guruhariharaun/CoWIN-Vaccine-Notifier/ "here")**

This Project is [**Live**](https://cowinvaccinenotifierdemo.herokuapp.com/ "**Live**") on: 🌍 **https://cowinvaccinenotifierdemo.herokuapp.com/**

## Getting Started
## API Used In This Application
- The application uses the [Co-WIN Public APIs.](https://apisetu.gov.in/public/api/cowin "Co-WIN Public APIs.") These APIs are subject to a rate limit of 100 API calls per 5 minutes per IP. Also, the available data is cached and may be up to 30 minutes old.

- To automate the bot we need the state id and districts ID 

1. API to get vaccination sessions on a specific date in a given district by district.
2. API to get all the states in India.
3. API to get all the districts.

## Prerequisites
Tools that needed to run 
- [**Python 3.8+**](https://www.python.org/downloads/ "**Python 3.8+**") Installed.
- SMTP Server if you are going to host it on a server.

## Installation
- Git clone the code from this repository.

- Check whether the python 3.8+ Installed on your computer using `python3 --version` 

- Install the modules which are required to run the application on requirements.txt using the command `pip3 install requirement.txt`

- To modify the user details open up the `config.py` file on any IDE or Text Editor and change the prefilled template according to your settings.

- Deploy the application using  `python3 app.py` or `flask run`

- The server will start running on http://127.0.0.1:6060 or http://127.0.0.1:5000

## Modifying Configuration
- Before you start to run the application you should need to update the configuration file which is on the `config.py` file.

### User Details File Modification
| Variables | User Details | Instructions |
| ------------ |---------------|-----|
| uname      | Guru HariHaraun | Enter Your **Name** Here |
| email      | guruhari@abcd.com |Enter Your **Email** Here |
| district_id | 560 |The **506** is the district code for trichy. You can fetch your district id from http://127.0.0.1:6060/id page |
| vaccine_type | COVISHIELD | Either user **COVISHIED**  or **COVAXIN** All should be in **UPPERCASE** |
| fee_type | Free | The fee type should be **Paid** or **Free** All should be in **UPPERCASE** |
| age_limit | 21 | Enter Your **Age** Here |
| atempt    | 3   | Number of days the application should periodically check |
| wait_time | 300 |The number of seconds the bot needs to check. ***Note: **The APIs are subject to a **rate limit** of **100 API calls per 5 minutes per IP*** |

### Setting Up a SMTP User Configuration 
- In this application the SMTP server was Gmail&apos;s SMPT Server. Can be changed according to your prefered SMTP Server and port number.

	**Note for Gmail User:** If you are using Gmail&apos;s SMTP Server you should **Turn Off** Less Secure App. [Click Here](https://support.google.com/accounts/answer/6010255#zippy=%2Cif-less-secure-app-access-is-on-for-your-account "Click Here") to learn how to turn off the less secure application.

| Variables | User Details | Instructions |
| ------------ |---------------|-----|
| SMTP_SERVER | smtp.gmail.com  |Enter Your SMTP Server API&apos;s Endpoint |
| SMTP_PORT | 587  |Enter Your SMTP Server Port Number |
| SMTP_USER_NAME | hariguru@abcd.com | Enter Your SMTP Server&apos;s User Name |
| SMTP_PASSWORD | QWERTY@1234 | Enter Your SMTP Server&apos;s Password |

## TODO
- [x] ~~Setting up a **Flask Application** for presentation purpose.~~
- [x] ~~Setting up an **Emali Alert **using python SMTP module.~~
- [ ] To add up the **Dose 1** or** Dose 2** parameter in the user details.
- [ ] Sending an an **SMS (short message service)** Alert to the users.
- [ ] Scheming up a database to hold user details and data.
- [ ] Handling multiple users in the application.

## License
The **COWIN Vaccine Notifier** is licensed under the terms of the [MIT license](https://github.com/guruhariharaun/CoWIN-Vaccine-Notifier/blob/main/LICENSE "MIT license") and is available for free.

## Acknowledgement
- Appreciating Indian Govt for providing Open APIs via [APISetu.](https://apisetu.gov.in/ "APISetu")
- Hat tip to anyone who&apos;s code was used ✌
- Hands down to my Stackoverflow Bros 🙆🏻‍♂️

<p align="center">
  Made with ❤️ by <a href="https://github.com/guruhariharaun">Guru HariHaraun</a>
</p>
<img align="center" src="https://ik.imagekit.io/guruhariharaun/github/CoWIN_Vaccine_Notifier/footer.png" alt="footer" />
