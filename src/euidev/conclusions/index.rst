Conclusions
============

:term:`RGVFlood.com` has been successfully taken out of beta and deployed in production mode.

#. The single-stack :term:`Docker` container deployment used in the beta deployment has been coverted to a scalable :term:`Kubernetes` cluster.
#. The production system now relies on a shared inter-pod, cloud-based :term:`NFS` volume service, ensuring expansion and accomodation of the large volumes of geospatial data being stored, and produced by the :term:`H&H` and visualization tools to be integrated.
#. Database services are now provided by a Google's CloudSQL, a managed cloud-served database service, resulting in minimal data access bottle-necks.
#. The core :term:`GeoNode` application has been upgraded to v4.0 maximizing the potential for future growth and seamless conntinuous deployment.
#. A step-wise development process has been implemented, allowing both for the continuous integration of changes in third-party applications (e.g. :term:`GeoNode`), incorporation of new :term:`RGVFlood` apps, rigorous testing and continuous deployment.