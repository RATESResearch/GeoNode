Extending REONode for RGVFlood
==============================

:term:`REONode` is an implementation of :term:`GeoNodeGCP`, incorporating :term:`REON` extensions and applications. :term:`RGVFlood` is a production implementation of :term:`REONode` incorporating extensions and applications specified for the :term:`RGVFlood` deployment. :term:`RGVFlood` is available online at <http://rgvflood.com>. This section describes the process of constructing the base app for :t
    # Edit the app :code:`.env` from :code:`template.env`
    envsubst < ${PROJECT_DIR}/.env > ${PROJECT_DIR}/src/${NAMESPACE}/.env
    envsubst < ${PROJECT_DIR}/src/templates/template.env >> ${PROJECT_DIR}/src/${NAMESPACE}/.env
    # Delete database secrets
    kubectl delete secret ${NAMESPACE}-secrets --namespace ${NAMESPACE}    
    # Create database secrets
    kubectl create secret generic ${NAMESPACE}-secrets --from-env-file ${PROJECT_DIR}/src/${NAMESPACE}/.env  --namespace ${NAMESPACE}
    # Re-apply
    kubectl rollout restart deployment/rgvflood-app