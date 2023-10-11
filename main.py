import os
try:
    from flask import Flask, jsonify, request
    import requests, json
except:
    os.system('pip install flask')
    os.system('pip install requests')
app = Flask(__name__)
list_key = ['khoihuynh1109', 'huynhminhkhoi', 'svduyanhoccho', 'duyanhisoccho']
@app.route('/')
def index():
    return "Hello, you are using KhoiHuynh1109's API"

def check_key(key):
    if key in list_key:
        return True
    return False
@app.route('/bugdilink', methods = ['GET'])
def buglink():
    key = request.args.get('key')
    link = request.args.get('link')
    if key == None or key == '':
        data = {
        'api': 'KhoiHuynh1109',
        'status': 'error',
        'message': 'Please Check The Key On The Url'
        }
    else:
        if check_key(key):
            if link == None or link == '':
                data = {
                'api': 'KhoiHuynh1109',
                'status': 'error',
                'message': 'Please Check The Link On The Url'
                }
            else:
                if 'dilink' in link:
                    try:
                        bug = requests.get(link).text
                        url_bug = bug.split("url: '")[1].split("',")[0]
                        data = {
                        'api': 'KhoiHuynh1109',
                        'status': 'success',
                        'url': url_bug
                        }
                    except Exception as e:
                        data = {
                        'api': 'KhoiHuynh1109',
                        'status': 'error',
                        'message': str(e)
                        }
                else:
                    data = {
                    'api': 'KhoiHuynh1109',
                    'status': 'error',
                    'message': 'Please Check The Link Again, I Can Only Bug Dilink.com'
                    }
        else:
            data = {
            'api': 'KhoiHuynh1109',
            'status': 'error',
            'message': 'Invalid Key!!!'
            }
    return json.dumps(data)
if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 8080)
