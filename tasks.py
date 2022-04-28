#!/usr/bin/env python3

from invoke import task
import os, socket, datetime
from os import system, getenv
import sys, shutil
from dotenv import load_dotenv
from invoke import Responder

IS_ANDROID: bool = hasattr(sys, 'getandroidapilevel')

if IS_ANDROID:
    IN_STREAM_ARG = False
else:
    IN_STREAM_ARG = None

sudopass = Responder(
     pattern=r'\[sudo\] password:',
     response=str(getenv('PASSWORD'))+'\n'
     )

load_dotenv()

if not os.path.exists("src/docker/.env"):
    shutil.copy("src/docker/template.env", "src/docker/.env")

@task
def deploy_docs(c):
    """
    Build, compose & deploy docs
    """
    c.run("make html")
    c.run("docker-compose up -d  --build docs")

@task
def restore_volumes(c):
    """ Retore the Docker Volumes
    """
    c.sudo("rsync -avzh --progress --delete tigger.water-wizard.org:/var/lib/docker/volumes/rgvflood* /var/lib/docker/volumes/")
    c.sudo("( cd /home/anernest/RGVFlood; sudo -u anernest docker exec django4rgvflood sh -c 'python manage.py migrate_baseurl -f --source-address=rgvflood.com --target-address=rgvflood.water-wizard.org")

@task
def install_latex(c):
    """
    Install the package
    """
    c.sudo("apt-get -y update", watchers=[sudopass])
    c.sudo("apt-get -y upgrade", watchers=[sudopass])
    c.sudo("apt-get -y install texlive-latex-recommended texlive-latex-extra texlive-fonts-recommended latexmk", watchers=[sudopass])
    c.run("pip install --upgrade -e .", in_stream = IN_STREAM_ARG)

@task
def rebuild_django(c):
    """ Rebuild the django container
    """
    c.run("docker-compose build --no-cache django", in_stream = IN_STREAM_ARG)
    c.run("docker-compose down", in_stream = IN_STREAM_ARG)
    c.run("docker-compose up -d", in_stream = IN_STREAM_ARG)
    #c.run("inv install-reondj", in_stream = IN_STREAM_ARG)
    #c.run("inv add-reondj", in_stream = IN_STREAM_ARG)

@task
def install_reondj(c):
    """ Install the REONdj app in the docker container
    """
    c.run('docker exec django4rgvflood sh -c "mkdir -p -m 0600 ~/.ssh"', in_stream = IN_STREAM_ARG)
    c.run('docker exec django4rgvflood sh -c "ssh-keyscan -H github.com bitbucket.org >> ~/.ssh/known_hosts"', in_stream = IN_STREAM_ARG)
    c.run('docker cp ~/.ssh/id_rsa django4rgvflood:/root/.ssh/', in_stream = IN_STREAM_ARG)
    c.run('docker exec django4rgvflood sh -c "pip install --no-cache-dir --upgrade git+ssh://git@github.com/RATESResearch/REONapp.git"', in_stream = IN_STREAM_ARG)

@task
def add_reondj(c):
    """ Add the REONdj appd to GeoNode
    """
    c.run('docker cp base.html django4rgvflood:/usr/src/geonode/geonode/templates/', in_stream = IN_STREAM_ARG)
    c.run('docker cp urls.py django4rgvflood:/usr/src/geonode/geonode/', in_stream = IN_STREAM_ARG)
    c.run('docker cp settings.py django4rgvflood:/usr/src/geonode/geonode/', in_stream = IN_STREAM_ARG)
    c.run('docker exec django4rgvflood sh -c "python manage.py makemigrations --noinput"', in_stream = IN_STREAM_ARG)
    c.run('docker exec django4rgvflood sh -c "python manage.py migrate --noinput"', in_stream = IN_STREAM_ARG)
    c.run('docker exec django4rgvflood sh -c "python manage.py collectstatic --noinput"', in_stream = IN_STREAM_ARG)
    c.run('docker exec django4rgvflood sh -c "touch /usr/src/geonode/geonode/wsgi.py"', in_stream = IN_STREAM_ARG)

@task
def provision_reondj(c):
    """ Provision REONdj
    """
    c.run('docker cp theme.json django4rgvflood:/usr/src/geonode', in_stream = IN_STREAM_ARG)
    c.run('docker exec django4rgvflood sh -c "mkdir -p /mnt/volumes/statics/uploaded/img/2021/12/"', in_stream = IN_STREAM_ARG)
    c.run('docker cp background.jpg django4rgvflood:/mnt/volumes/statics/uploaded/img/2021/12/', in_stream = IN_STREAM_ARG)
    c.run('docker cp logo.png django4rgvflood:/mnt/volumes/statics/uploaded/img/2021/12/', in_stream = IN_STREAM_ARG)
    c.run('docker exec django4rgvflood sh -c "python manage.py loaddata /usr/src/geonode/theme.json"', in_stream = IN_STREAM_ARG)
    c.run('docker exec django4rgvflood sh -c "python manage.py provision 144 145 146 147 148"', in_stream = IN_STREAM_ARG)

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
def latexpdf(c):
    """
    Make pdf
    """
    c.run("make latexpdf --debug", in_stream = IN_STREAM_ARG)

@task
def pdf(c):
    """
    Make pdf
    """
    c.run("make pdf --debug", in_stream = IN_STREAM_ARG)

@task
def build_no_cache(c):
    """
    Run docker-compose build --no-cache
    """
    html(c)
    c.run("docker; docker-compose build --no-cache", in_stream = IN_STREAM_ARG)

@task
def up(c):
    """
    Run docker-compose
    """
    html(c)
    c.run("docker; docker-compose up -d", in_stream = IN_STREAM_ARG)

@task
def down(c):
    """
    Bring down docker images
    """
    c.run("docker-compose down", in_stream = IN_STREAM_ARG)

@task
def delete(c):
    """
    Bring down docker images and delete the volume
    """
    c.run("docker-compose down -v --rmi local", in_stream = IN_STREAM_ARG)

@task
def docs_for_docker(c):
    """
    Build docs for docker
    """
    clean(c)
    html(c)
    single(c)

@task
def backup(c):
    """ Backup 
    """
    c.run("docker cp br/settings.ini django4rgvflood:/backup_restore/", in_stream = IN_STREAM_ARG)
    c.run("docker exec django4rgvflood python manage.py backup -f --backup-dir=/backup_restore --config=/backup_restore/settings.ini", in_stream = IN_STREAM_ARG)
    target = os.path.join("/srv/REON/backup", socket.gethostname(), "RGVFlood")
    c.run("docker cp -a django4rgvflood:/backup_restore br/", in_stream = IN_STREAM_ARG)
    c.run("rsync -avzh --progress  br/backup_restore tigger.water-wizard.org:"+target)
    c.run("docker exec django4rgvflood sh -c 'rm /backup_restore/*.*'", in_stream = IN_STREAM_ARG)

@task
def recreate(c):
    """ Recreate from backup 
    """
    clean(c)
    delete(c)
    docs_for_docker(c)
    # #build_no_cache(c)
    up(c)

@task
def reondj(c):
    install_reondj(c)
    add_reondj(c)
    provision_reondj(c)

@task
def restore(c):
    nameroot = datetime.datetime.utcnow().strftime("%Y-%m-%d_%H*.*")
    source = os.path.join("/srv/REON/backup/tigger/RGVFlood/backup_restore/", nameroot)
    c.run("rsync -avzh --progress  tigger.water-wizard.org:"+source+" br/backup_restore/")
    c.run("docker cp -a br/backup_restore django4rgvflood:/", in_stream = IN_STREAM_ARG)
    c.run("docker exec django4rgvflood sh -c 'python manage.py restore -f --soft-reset --backup-files-dir=/backup_restore/ --config=/backup_restore/settings.ini'", in_stream = IN_STREAM_ARG)
    c.run("docker exec django4rgvflood sh -c 'rm /backup_restore/*.*'", in_stream = IN_STREAM_ARG)
    c.run("docker exec django4rgvflood sh -c 'python manage.py migrate_baseurl -f --source-address=rgvflood.com --target-address=rgvflood.water-wizard.org'", in_stream = IN_STREAM_ARG)

@task
def host(c):
    print(socket.gethostname())
    name = datetime.datetime.utcnow().strftime("%Y-%m-%d_%H*")
    print(name)

@task
def all(c):
    """
    Do it all
    """
    clean(c)
    delete(c)
    docs_for_docker(c)
    build_no_cache(c)
    up(c)
    install_reondj(c)
    add_reondj(c)
    provision_reondj(c)

if __name__ == "__main__":

    #system("inv install_reondj")
    #system("inv html")
    #system("inv slides")
    #exit()

    ans=True
    while ans:
        system("inv --list")
        ans=input("What would you like to do? ")
        system("inv "+ans)
