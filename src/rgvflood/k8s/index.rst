RGVFlood Kubernetes
------------------

The :term:`k8s` deployment is adapted from the Docker Compose stack to fully utilize the replication, redundancy and stability features of a :term:`k8s` cluster.


.. code:: 
    
    # Delete database secrets
    kubectl delete secret ${NAMESPACE}-secrets --namespace ${NAMESPACE}    
    # Create database secrets
    kubectl create secret generic ${NAMESPACE}-secrets --from-env-file ${PROJECT_DIR}/src/${NAMESPACE}/.env  --namespace ${NAMESPACE}
    # Re-apply
    kubectl rollout restart deployment/rgvflood-app -n rgvflood