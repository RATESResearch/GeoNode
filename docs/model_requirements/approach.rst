Approach to Deployment
======================

The prcess of deployment accross all three Tiers falls into 3 iterative and cross-tier integrated steps:

*  Requirements Determination: This is an iterative process by which the target functionality of the application is determined. Two factors influence the iterative nature of the development and deployment cycle. The first is the end-user expectations. In scenarios where the end-user is integrally involved in a feed-back cycle, end-user expectations will evolve as thier familiarity increases with the application both during development and post deployment. The second is driven by the structure of the modeling framework, including the upstream and downstream modeling Tiers and the data availability.
*  Implementation: This too is an iterative proces, evolving as the Requirements Determination process evolves.
*  Deployment: The deployment process is continuous, with the :term:`RGVFlood` user interface application being delivered as service (:term:`SaaS`).

.. uml:: 
   :align: center
   :caption: Model Tier Integration Approach (x-axis is % complete)

   robust  "Tier I" as tier1
   robust  "Tier II" as tier2
   robust  "Tier III" as tier3

   @0
   tier1 is Requirements

   @25
   tier1 is Implementation
   tier2 is Requirements

   @50
   tier1 is Deployment
   tier2 is Implementation
   tier3 is Requirements

   @75
   tier2 is Deployment
   tier3 is Implementation

   @100
   tier3 is Deployment


