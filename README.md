# SGPD

Este proyecto es un sistema para optimización de procesos para agentes de la Subdirección General de Prevensión del Delito de la PNC de Guatemala.

Está realizado con:

Python 3.9.2

y las siguientes librerias:

asgiref==3.5.2
Django==4.1.2
mysqlclient==2.1.1
pkg_resources==0.0.0
PyMySQL==1.0.2
sqlparse==0.4.3

El desarrollo es elaborado en WSL Debian para Docker.

Para poder seguir mejorando el proyecto es necesario que clone el repositorio bajo un FORK.

Si se trabaja bajo el mismo WSL es necesario realizar lo siguiente:

## WSL DEBIAN

```bash
apt-get update && apt-get upgrade
apt-get install libmariadbclient-dev
apt-get install python3-pip
apt-get install python3-venv
apt-get install python3-dev
```

## CLONAR EL REPOSITORIO

Clonando el repositorio 

```bash
git clone https://github.com/amner-py/SGPD_OS.git SGPD
```

## CLONAR TU PROPIO FORK

Clonando el repositorio 

```bash
git clone [acá tu link para el repositorio fork] SGPD
```

##  CREAR ENTORNO VIRTUAL PARA USAR EL PROYECTO

Abrir la consola de preferencia en la carpeta SGPD que se creó y luego en consola ingresar lo siguiente:

### LINUX
```bash
python3 -m venv .
```

### WINDOWS
```bash
py -m venv .
```
ó

```bash
py -m virtualenv .
```

### ENTRAR AL ENTORNO VIRTUAL LINUX

```bash
source bin/activate
```

### ENTRAR AL ENTORNO VIRTUAL WINDOWS

```bash
cd Scripts
activate
```

### INSTALAR REQUERIMIENTOS PARA EL PROYECTO 

```bash
pip install -r requirements.txt
```