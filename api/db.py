from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SQLITE = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

MySQL1 = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'sgpd',
        'USER': 'admin',
        'PASSWORD': 'admin123',
        'HOST': '192.168.10.109',
        'PORT': '3306',
    }
}

MySQL = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'SGPD',
        'USER': 'sgpdpnc',
        'PASSWORD': 'sgpdPnC$]',
        'HOST': 'localhost',
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
