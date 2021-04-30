<div align="center" id="top"> 
  <img src="./.github/GithubIcon.png" alt="Foot Salary" width=150/>

  &#xa0;
</div>

<h1 align="center">Foot Salary</h1>

<p align="center">
  <img alt="Github Lenguaje mas utilizado" src="https://img.shields.io/github/languages/top/feliamunda/foot-salary?color=56BEB8">

  <img alt="Github numero de lenguajes utilizados" src="https://img.shields.io/github/languages/count/feliamunda/foot-salary?color=56BEB8">

  <img alt="Tamano del repo" src="https://img.shields.io/github/repo-size/feliamunda/foot-salary?color=56BEB8">

  <img alt="Licencia" src="https://img.shields.io/github/license/feliamunda/foot-salary?color=56BEB8">
</p>

<p align="center">
  <a href="#dart-about">Acerca de</a> &#xa0; | &#xa0; 
  <a href="#sparkles-features">Características</a> &#xa0; | &#xa0;
  <a href="#rocket-technologies">Tecnologias</a> &#xa0; | &#xa0;
  <a href="#white_check_mark-requirements">Requerimientos</a> &#xa0; | &#xa0;
  <a href="#checkered_flag-starting">Empezar</a> &#xa0; | &#xa0;
  <a href="#memo-license">Licencia</a> &#xa0; | &#xa0;
  <a href="https://github.com/feliamunda" target="_blank">Autor</a>
</p>

<br>

## :dart: Acerca de ##

Este Projecto es acerca de una API REST que procesa un Objeto JSON con la información de los jugadores de un equipo a la vez y calcula el total de su sueldo completo

Para mas información acerca de su uso leer la [DOCUMENTACIÓN](https://documenter.getpostman.com/view/7918914/TzK2bEeV)

## :sparkles: Caracteristicas ##

:heavy_check_mark: RESTfull\
:heavy_check_mark: JWT Authorization\
:heavy_check_mark: Contenerizada\
:heavy_check_mark: Potencial de Expansión y guardado de registros en BD

## :rocket: Tecnologías ##

Las siguientes tecnologias fueron usadas en este proyecto:

- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Django Rest Framework](https://www.django-rest-framework.org/)

## :white_check_mark: Requerimientos ##

Antes de empezar :checkered_flag:, necesitas tener [Git](https://git-scm.com) y [Python](https://www.python.org/) instalados o [Docker](https://www.docker.com/).

## :checkered_flag: Empezar ##

```bash
# Clona el projecto
$ git clone https://github.com/feliamunda/foot-salary

# Accede
$ cd foot-salary

## CON PYTHON ##
# Instalar pipenv
$ pip install pipenv

# Crear ambiente virtual 
$ pipenv install

# Correr Migraciones 
$ pipenv run python manage.py migrate

# Si es la primera vez o no tiene un usuario ejecutar reemplazando admin y admin@test.com por los de su preferencia, luego desplegará un prompt para crear su contraseña
$ pipenv run python manage.py createsuperuser --username admin --email admin@test.com

# Ejecutar Servidor 
$ pipenv run python manage.py runserver
# El servidor se inicializará en <http://localhost:8000>

## CON DOCKER ##

#Ejecutar Docker Compose
$ docker-compose up -d
# El servidor se inicializará en <http://localhost:8000>

# Detiene los contenedores y sus servicios
$ docker-compose down 

#Con Docker se crea un usuario por defecto admin con password 12345#
```

## :memo: Licencia ##

Este Proyecto esta bajo la licencia [GPL](LICENSE.md).


Hecho con el :heart: por <a href="https://github.com/feliamunda" target="_blank">Felicie Amundaray</a>

&#xa0;

<a href="#top">Volver arriba</a>
