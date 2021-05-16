# Simple Flask App

Aplikacja Dydaktyczna wyświetlająca imię i wiadomość w różnych formatach dla zajęć
o Continuous Integration, Continuous Delivery i Continuous Deployment.

- W projekcie wykorzystamy virtual environment, dla utworzenia hermetycznego środowisko dla aplikacji:

  ```
  ## upewniamy sie czy mamy polskie litery

  # tworzymy hermetyczne środowisko dla bibliotek aplikacji:
  # upewnij sie, ze we wlasciwym katalogu(projekcie)
  ## to srodowisko tworzymy raz, cokolwiek instalujemy w nim - jest zachowane
  $ python3 -m venv .venv

  # za pomocą Makefile
  $ make deps

  # !!!!! aktywowanie hermetycznego środowiska !!!!!
  ## source nadpisuje zmienne srodowiskowe
  $ source .venv/bin/activate
  $ pip install -r requirements.txt
  $ pip install -r test_requirements.txt

  # zobacz
  $ pip list
  ```

  Sprawdź: [tutorial venv](https://docs.python.org/3/tutorial/venv.html) oraz [biblioteki flask](http://flask.pocoo.org).

- Uruchamianie applikacji:

  ```
  # w trybie deweloperskim
  $ make run

  # jako zwykły program
  $ python main.py

  # albo:
  $ PYTHONPATH=. FLASK_APP=hello_world flask run
  ```

- Uruchamianie testów (see: http://doc.pytest.org/en/latest/capture.html):

  ```
  $ make test

  # bez Makefile
  #albo
  $ PYTHONPATH=. py.test
  $ PYTHONPATH=. py.test --verbose -s
  ```

- Kontynuując pracę z projektem, aktywowanie hermetycznego środowiska dla aplikacji py:

  ```
  # deaktywacja
  $ deactivate
  ```

  ```
  ...

  # aktywacja
  $ source .venv/bin/activate
  ```

- Integracja z TravisCI:

  ```
  # miejsce na twoje notatki
  ```

- Deployment do Heroku z TravisCI
  ```
  # miejsce na twoje notatki
  ```

- Dodanie monitoringu Statuscake
  ```
  # miejsce na twoje notatki
  ```

# Pomocnicze

## Ubuntu

- Instalacja dockera: [dockerce howto](https://docs.docker.com/install/linux/docker-ce/ubuntu/)

## Centos

- Instalacja docker-a:

  ```
  $ yum remove docker \
        docker-common \
        container-selinux \
        docker-selinux \
        docker-engine

  $ yum install -y yum-utils

  $ yum-config-manager \
      --add-repo \
      https://download.docker.com/linux/centos/docker-ce.repo

  $ yum makecache fast
  $ yum install -y docker-ce
  $ systemctl start docker
  ```

## Dodanie Badge z TraviCI

[![Build Status](https://travis-ci.org/primeira-iza/se_hello_printer_app.svg?branch=master)](https://travis-ci.org/primeira-iza/se_hello_printer_app)

## Dodanie Badge z StatusCake

![StatusCake](https://app.statuscake.com/button/index.php?Track=5961429&Days=1&Design=2)
