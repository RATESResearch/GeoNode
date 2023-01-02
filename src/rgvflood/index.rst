Extending REONode for RGVFlood
==============================

:term:`REONode` is an implementation of :term:`GeoNodeGCP`, incorporating :term:`REON` extensions and applications. :term:`RGVFlood` is a production implementation of :term:`REONode` incorporating extensions and applications specified for the :term:`RGVFlood` deployment. :term:`RGVFlood` can be deployed as a :term:`Docker` stack, or as a :term:`k8s` app. The :term:`k8s` app is deployed on a :term:`GKE` autopilot cluster, available online at <http://rgvflood.com>. This section describes the process of constructing the base app.

To set up the environment for both options:

.. code::

    # Change directory to PROJECT_DIR
    # Complete project.env and save as .env
    # Export the Project Sensitive Data
    set -a; . .env; set +a
    # Edit the app :code:`.env` from :code:`template.env`
    envsubst < ${PROJECT_DIR}/.env > ${PROJECT_DIR}/src/${NAMESPACE}/.env
    envsubst < ${PROJECT_DIR}/src/templates/template.env >> ${PROJECT_DIR}/src/${NAMESPACE}/.env

.. toctree::
   :maxdepth: 2
   :caption: Deployment Options 

   compose/index 
   k8s/index