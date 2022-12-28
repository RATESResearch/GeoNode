Theming RGVFlood
================

Fortunately, GeoNode's built-in theming capabilities are sufficient for initial deployment of production instances. The current way of creating and deploying themes involves:

1. Initial theme relies on the stock GeoNode Themes Library. An RGVFlood theme has been created:

    1. A jumbotron slide show is used as the Welcome theme.

    #. The RGVFlood logo is uploaded.

    #. Images depicting various flooding events are used a slide show content.



Archive 
=======

1. Log into a django container in one of the apps pods:

.. code::

    docker compose --env-file .env -f docker-compose-geonode-original.yml exec -it django /bin/bash

#. Download the themes fixture:

.. code::

    python manage.py dumpdata geonode_themes --indent 4 > geonode_themes.json    
