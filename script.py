import os

API_KEY = os.environ['AK']

print('python app/joincliSetup.py -ak ' + API_KEY)

os.system('python app/joincliSetup.py -ak {}'.format(API_KEY))
os.system('python app/joincliSetup.py -re')
os.system('python app/joincliServer.py')
