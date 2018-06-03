#-*- coding: utf-8 -*-

from flask import Flask
from flask import redirect, request, render_template
from controllers import api
import os

flask_app = Flask(__name__)

@flask_app.route('/favicon.ico')
def favicon():
    return redirect(os.path.join(flask_app.root_path, 'templates'),'favicon.ico')

@flask_app.route('/<sht_url>', methods=['GET'])
def short_to_org(sht_url):
    #뒤에 url get parameter로 받기
    #db에서 실제 url 정보 가져오기
    #해당 url로 리다이렉트
    if request.method == 'GET':
        return api.get_org_url(sht_url)

@flask_app.route('/short', methods=['POST'])
def org_to_short():
    #util->shorturl생성
    if request.method == 'POST':
        org_url = request.form['org_url']
        return api.get_sht_url(org_url)


@flask_app.route('/')
def main_page():
    return render_template('home.html')



if __name__ == '__main__':
    flask_app.run(host='0.0.0.0', port=8080)