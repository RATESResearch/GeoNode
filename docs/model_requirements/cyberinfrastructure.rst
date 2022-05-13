Cloud Services Cyberinfrastructure for the Tiered Modeling Framework
====================================================================

With the exception of the :term:`RTHS` in-ground and in-stream hardware, all the cyberinfrastructure utilized for the the production Tiered modeling framework is both deployed to and delivered from cloud infrastructure providers.

Computing hardware experiences rapid depreciation both in value and competitive performance, with an effective lifecycle of between 5 - 10 years. Further, for instantaneous use of hardware, where services are spun up and shut-down on demand, the cost of use is generally a fraction of the equivalent amortized cost of purchasing hardware.

High Performance Computing
--------------------------

:term:`HPC` capacity is required for the current incarnations of the :term:`Tier I` model, :term:`WRF-Hydro`, for continuous execution. All mainstream regional hydrologic and hydraulic models are developed as monlithic applications, although the most detailed and computationally intensive :term:`WRF-Hydro` included, are optimized for parallel execution on traditional :term:`HPC` s. Most :term:`HPC` s consist of a cluster of computing nodes connected via an ultra-high speed network where communication between processes is effected most often by the *Message Passing Interface* :term:`MPI`.

All three major cloud  providers offer :term:`HPC` services:

*   :term:`AWS`: Offers Amazon :term:`EC2` with computing capacity resizable to the applications needs.

*   :term:`GCP`: Offers :term:`HPC` ready :term:`VM` images allowing for the rapid formation of :term:`HPCC`.

*   :term:`Azure`: Microsoft offers :term:`HPC` services ranging from clustered :term:`VM` s as offered by Amazon and Google, to purpose build :term:`HPC` infrastructure and single-tenant Cray XC oe CS supercomputers.

Virtual Machines
----------------

For the current deployment schedule, :term:`Tier II` and :term:`Tier III` models are to expected to be run by the end-users, with :term:`RGVFlood` providing ready access to data to minimize data collection efforts needed. In order to provide functional demonstration of these facilities, 6 sub-regions and 20 urban areas within the :term:`LRGV` will be modeled by :term:`RATES`.

In order to facilitate the execution of these models by end-users who may not have the hardware, or indeed technical capacity, to run these models, procedures for spinning up  :term:`VM` s are being developed so that the currently selected :term:`Tier II` and :term:`Tier III` models, :term:`HEC-RAS` and :term:`SWMM` respectively, may be run. These :term:`VM` services are offered by most providers with the ability to spin up, provision, execute and shut down in order to limit the service costs.

As with :term:`HPC` services. :term:`VM` services are offered by a variety of providers, including the three major vendors: Amazon, Google and Microsoft.

Containerized Cloud Services
----------------------------

While :term:`RATES` is actively investigating the refactoring of traditionally monolithic :term:`H&H` models in coupled microservices, the user interface components of the :term:`RGVFlood` ecosystem are currently being deployed in containerized form. With an eye towards long term sustainability of :term:`RGVFlood` beyond the term of the :term:`TWDB/FIF` project, these services are all being migrated to cloud service providers.

*   :term:`RGVFlood.com`: is currently deployed as a stack of :term:`Docker` containers on the on-premise bare-metal server :term:`Tigger`. The process of migrating :term:`RGVFlood.com` to a :term:`Kubernetes` cluster on :term:`GCP` is currently underway. This will ensure scalability of the services as the data-intensive operations increase with increased end-user access. 
*   :term:`Wizard.RGVFlood.com`: is already deployed on the cloud as a :term:`PWA` with the provider Netlify.com. Migrating to Google's Firebase platform is currently being investigated.