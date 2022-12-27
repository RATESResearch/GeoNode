Extending REONode for RGVFlood
==============================

:term:`REONode` is an implementation of :term:`GeoNodeGCP`, incorporating :term:`REON` extensions and applications. :term:`RGVFlood` is a production implementation of :term:`REONode` incorporating extensions and applications specified for the :term:`RGVFlood` deployment. :term:`RGVFlood` is available online at <http://rgvflood.com>. This section describes the process of constructing the base app for :term:`RGVFlood.com`.

1. The environment variables file from :term:`REONode` is adapted to reflect the specifics of :term:`RGVFlood`.

#. Create the namespace, context, static IP, app :code:`.env` file and secrets:

.. code::

    # Export the variables from .env 
    set -a; . .env; set + 
    # Create namespace 
    kubectl create namespace ${NAMESPACE} 
    # Verify creation of namespace:
    kubectl describe namespace ${NAMESPACE}
    # Add the cluster and context to the local kube.config. We
    gcloud container clusters get-credentials ${CLUSTER} --region ${REGION}
    # List the contexts:
    kubectl config get-contexts
    # Rename the new context:
    kubectl config rename-context gke_${PROJECT_ID}_${REGION}_${CLUSTER} ${NAMESPACE}
    # Add namespace to the new context
    kubectl config set-context ${NAMESPACE} --namespace ${NAMESPACE}
    # List the contexts to verify addition of the namespace:
    kubectl config get-contexts
    # Use the desired context
    kubectl config use-context ${NAMESPACE}
    # Create a static IP 
    gcloud compute addresses create ${NAMESPACE}-ip --project=${PROJECT_ID} --global
    # Check the IP value
    gcloud compute addresses describe ${NAMESPACE}-ip --project=${PROJECT_ID} --global
    # Create the app :code:`.env` from :code:`template.env`
    envsubst < ${PROJECT_DIR}/.env > ${PROJECT_DIR}/src/${NAMESPACE}/.env
    envsubst < ${PROJECT_DIR}/src/templates/template.env >> ${PROJECT_DIR}/src/${NAMESPACE}/.env
    # Create cloudsql-oauth-credentials
    kubectl create secret generic cloudsql-oauth-credentials --from-file=credentials.json=$HOME/.ssh/waterwizard-cloudsql.json --namespace ${NAMESPACE}
    # Create database secrets
    kubectl create secret generic ${NAMESPACE}-secrets --from-env-file ${PROJECT_DIR}/src/${NAMESPACE}/.env  --namespace ${NAMESPACE}

#. Create the manifests from the templates:

.. code::

    # envsubst < ${PROJECT_DIR}/src/templates/namespace.template.yaml > ${PROJECT_DIR}/src/${NAMESPACE}/namespace.yaml
    envsubst < ${PROJECT_DIR}/src/templates/mc.template.yaml > ${PROJECT_DIR}/src/${NAMESPACE}/mc.yaml    
    envsubst < ${PROJECT_DIR}/src/templates/pv.template.yaml > ${PROJECT_DIR}/src/${NAMESPACE}/pv.yaml
    envsubst < ${PROJECT_DIR}/src/templates/pvc.template.yaml > ${PROJECT_DIR}/src/${NAMESPACE}/pvc.yaml
    envsubst < ${PROJECT_DIR}/src/templates/deployment.template.yaml > ${PROJECT_DIR}/src/${NAMESPACE}/deployment.yaml
    envsubst < ${PROJECT_DIR}/src/templates/backendconfig.template.yaml > ${PROJECT_DIR}/src/${NAMESPACE}/backendconfig.yaml
    envsubst < ${PROJECT_DIR}/src/templates/service.template.yaml > ${PROJECT_DIR}/src/${NAMESPACE}/service.yaml
    envsubst < ${PROJECT_DIR}/src/templates/ingress.template.yaml > ${PROJECT_DIR}/src/${NAMESPACE}/ingress.yaml
    # envsubst < ${PROJECT_DIR}/src/templates/clouddeploy.template.yaml > ${PROJECT_DIR}/src/${NAMESPACE}/clouddeploy.yaml

#. Deploy the RGVFlood app:

.. code::
    # Create the Google managed SSL certificate:
    kubectl apply -f /data/${NAME}/src/${NAMESPACE}/mc.yaml

    # Create the Kubernetes Persistent Volume for /data 
    kubectl apply -f /data/${NAME}/src/${NAMESPACE}/pv.yaml

    # Create the Kubernetes Persistent Volume Claim for /data 
    kubectl apply -f /data/${NAME}/src/${NAMESPACE}/pvc.yaml

    # Deploy the containers:
    kubectl apply -f /data/${NAME}/src/${NAMESPACE}/deployment.yaml

    # Configure the Backend:
    kubectl apply -f /data/${NAME}/src/${NAMESPACE}/backendconfig.yaml

    # Expose the app:
    kubectl apply -f /data/${NAME}/src/${NAMESPACE}/service.yaml

    # Enable external access:
    kubectl apply -f /data/${NAME}/src/${NAMESPACE}/ingress.yaml