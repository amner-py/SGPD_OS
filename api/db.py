from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SQLITE = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

MySQL = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'sgpd_db',
        'USER': 'devopy',
        'PASSWORD': 'amnerpy1',
        'HOST': '192.168.8.146',
        'PORT': '3306',
    }
}

"""
Para usar BD Oracle colocar la siguiente libreria: cx_Oracle
pip install cx_Oracle
"""
Oracle = {
    'default':{
        'ENGINE':'django.db.backends.oracle',
        'NAME':'BD_NOMBRE',
        'USER':'BD_USUARIO',
        'PASSWORD':'CONTRASEÑA',
        'HOST':'IP_HOST_DOMINIO',
        'PORT':'PUERTO',
    }
}