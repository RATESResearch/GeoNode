Background 
----------

A beta version :term:`RGVFlood.com` was released in the Fall of 2021 to demonstrate the proposed functionality of the system. This version of :term:`RGVFlood.com` was based on :term:`GeoNode` v3.3.2, with additional enhancements, including integration of an :term:`API` for ingestion of timeseries :term:`RTHS` data, a 'Flood Wizard' app for visualizing data and :term:`H&H` model availability. After operating for 6 months, it was determined that installation on a single bare-metal server was insufficient for the anticipated  demand, and the base software suite upon which :term:`RGVFlood.com` was constructed, limited the implementation of Continuous Integration/Continuous Delivery pathways for the already integrated extension and planned extensions - specifically those associated with :term:`H&H` model execution.

In the Spring of 2022, the beta site was decommissioned to allow for spin-up of a re-incarnation of :term:`RGVFlood.com` addressing the key issues identified during beta deployment:

#. Migration from a single-stack :term:`Docker` container deployment, to a scalable :term:`Kubernetes` cluster.
#. Reliance on an inter-pod shared, cloud-based :term:`NFS` volume service to ensure expansion and accomodation of the large volumes of geospatial data to be stored, as well as data produced by the integrated :term:`H&H` and visualization tools.
#. Reliance on a managed cloud-served database service, to ensure minimal data access bottle-necks.
#. Integration of :term:`GeoNode` v4.0 to promote future growth and seamless conntinuous deployment.
