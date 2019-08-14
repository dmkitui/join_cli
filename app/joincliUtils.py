import re, argparse, json, os
import pymongo

MONGO_URI = os.environ['MONGO_URI']
DB_NAME = os.environ['DB_NAME']

def api_regex(s, pat=re.compile(r"\w{32}")):
    if not pat.match(s):
        raise argparse.ArgumentTypeError
    return s

def str2bool(arg):
    if arg.lower() in ('yes','true','t','y','1'):
        return True
    if arg.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected!')

def open_local_devices():
    print('Did we get here?')
    try:
        client = pymongo.MongoClient(MONGO_URI)
        db = client[DB_NAME]
        print('XXXXX: ', db.devices.find_one())

        return db.devices.find_one()
        # with open("devices.json", "r") as deviceJSON:
        #     device_data_old = json.loads(deviceJSON.read())
        #     return device_data_old
    except:
        return None


def  save_devices(data, operation):
    try:
        client = pymongo.MongoClient(MONGO_URI)
        db = client[DB_NAME]
        print('DATA TO BE SAVED: ', data)
        if operation == 'setup':
            db.devices.save(data)
        elif operation == 'register':
            db.devices.update({}, data)

    except Exception as e:
        print('Error on saving: ', e)


def decode_UTF8(data):
    try:
        return data.decode("utf-8")
    except UnicodeDecodeError:
        return False
    except Exception as e:
        raise(e)
