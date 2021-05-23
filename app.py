from flask import Flask, redirect, current_app, jsonify, request, render_template
from multiprocessing import Process
from flask.helpers import url_for
import requests
import automate
import config

app = Flask(__name__)
process_flag = 0
data_set = None

@app.route('/', methods=['GET'])
def index():
    url = request.base_url+"user_details"
    data_set = requests.get(url).json()
    return render_template('index.html', data = data_set, process = process_flag)


@app.route('/id', methods=['GET'])
def id():
    return render_template('id.html')
  
@app.route('/user_details', methods=['GET'])
def user_detailss():
    global data_set
    data_set ={
        "uname": config.uname,
        "email": config.email,
        "district_id": config.district_id,
        "vaccine_type": config.vaccine_type,
        "fee_type": config.fee_type,
        "age_limit": config.age_limit,
        "wait_time": config.wait_time,
        "days_count": config.attempt,
        "isUserNotified": config.isUserNotified,
        "available_flag_break": config.available_flag_break
    }
    return jsonify(data_set)

@app.route('/start', methods=['GET'])
def automation():
    p = Process(target=automate.main)
    p.start()
    global process_flag
    process_flag += 1
    config_process = "Process-"+str(process_flag)
    current_app.config[config_process] = p
    return redirect(url_for('index')) 

@app.route('/kill', methods=['GET'])
def kill():
    global process_flag
    config_process = "Process-"+str(process_flag)
    if(process_flag != 0):
        p = current_app.config[config_process]
        p.kill()
        process_flag -= 1
        return redirect(url_for('index')) 
    else:
        return redirect(url_for('index')) 

if __name__ == '__main__':
    app.run(host='', debug=False, port=6060)