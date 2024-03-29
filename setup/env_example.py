import os, json, socket

def get_ip_address():
    '''Return IP adress'''
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address

def get_allowed_hosts():
    '''Create a list of aloowed hosts'''
    hosts = ['127.0.0.1', 'localhost', get_ip_address()]
    return hosts


os.environ['SECRET_KEY'] = 'your key'
os.environ['DEBUG'] = 'true' # '' is False
os.environ['ALLOWED_HOSTS'] = json.dumps(get_allowed_hosts())
os.environ['LANGUAGE_CODE'] = 'pt-br'
os.environ['TIME_ZONE'] = 'America/Sao_Paulo'
os.environ['AUTHOR'] = 'your-name'
os.environ['USE_SQLITE'] = 'True' # if '' is False, else is True

os.environ['EMAIL_HOST'] = 'EMAIL_HOST'
os.environ['EMAIL_HOST_USER'] = 'EMAIL_HOST_USER'
os.environ['EMAIL_HOST_PASSWORD'] = 'EMAIL_HOST_PASSWORD'
os.environ['EMAIL_PORT'] = 'EMAIL_PORT'

os.environ['EMAIL_BACKEND'] = 'EMAIL_BACKEND'
os.environ['GMAIL_HOST'] = 'GMAIL_HOST'
os.environ['GMAIL_HOST_USER'] = 'GMAIL_HOST_USER'
os.environ['GMAIL_HOST_PASSWORD'] = 'GMAIL_HOST_PASSWORD'