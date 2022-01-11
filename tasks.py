from invoke import task
import os
from os import system, getenv
import sys, shutil
from dotenv import load_dotenv
from invoke import Responder

IS_ANDROID: bool = hasattr(sys, 'getandroidapilevel')

if IS_ANDROID:
    IN_STREAM_ARG = False
    shutil.copy("/storage/emulated/0/.ssh/.env", ".env")
else:
    IN_STREAM_ARG = None
    shutil.copy(getenv("HOME")+"/.ssh/.env", ".env")

sudopass = Responder(
     pattern=r'\[sudo\] password:',
     response=str(getenv('PASSWORD'))+'\n'
     )

load_dotenv()

if not os.path.exists("src/docker/.env"):
    shutil.copy("src/docker/template.env", "src/docker/.env")

@task
def install(c):
    """
    Install the package
    """
    c.sudo("apt-get -y update", watchers=[sudopass])
    c.sudo("apt-get -y upgrade", watchers=[sudopass])
    c.sudo("apt-get -y install texlive-latex-recommended texlive-latex-extra texlive-fonts-recommended latexmk", watchers=[sudopass])
    c.run("pip install --upgrade -e .", in_stream = IN_STREAM_ARG)

@task
def clean(c):
    """
    Clean the docs _build directory
    """
    c.run("make clean", in_stream = IN_STREAM_ARG)

@task
def html(c):
    """
    Make html documents
    """
    c.run("make html --debug", in_stream = IN_STREAM_ARG)

@task
def slides(c):
    """
    Make slides
    """
    c.run("make slides --debug", in_stream = IN_STREAM_ARG)

@task
def single(c):
    """
    Make slides
    """
    c.run("make singlefile-slides --debug", in_stream = IN_STREAM_ARG)

@task
def pdf(c):
    """
    Make pdf
    """
    c.run("make latexpdf --debug", in_stream = IN_STREAM_ARG)

@task
def up(c):
    """
    Run docker-compose
    """
    html(c)
    c.run("cd src/docker; docker-compose up -d", in_stream = IN_STREAM_ARG)

@task
def down(c):
    """
    Bring down docker images
    """
    c.run("cd src/docker; docker-compose down", in_stream = IN_STREAM_ARG)

@task
def dall(c):
    """
    Do it all with docker
    """
    c.run("cd src/docker; docker-compose down -v --rmi local", in_stream = IN_STREAM_ARG)
    clean(c)
    html(c)
    single(c)
    pdf(c)
    up(c)

@task
def all(c):
    """
    Do it all
    """
    clean(c)
    html(c)
    #pdf(c)
    single(c)



if __name__ == "__main__":

    system("inv all")
    #system("inv html")
    #system("inv slides")
    exit()

    ans=True
    while ans:
    	system("inv --list")
    	ans=input("What would you like to do? ")
    	system("inv "+ans)
