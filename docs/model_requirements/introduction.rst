Introduction to the Tiered Regional H&H Modeling Framework
==========================================================

The Tiered Regional Hydrologic and Hydraulic Modeling Framework consists of 3 coupled computational tiers: 

*   **Tier I** Real-Time Regional Hydrologic Model: Currently being instatiated using the :term:`WRF-Hydro` to provide forecast discharges across the :term:`LRGV`. This is a computationally intensive application run continuously in order to produce forecasts of discharges up to 5 days in advance in the major classified streams.
*   **Tier II** On-Demand Sub-Regional Hydraulic Model: Currently being developed and implemented using the :term:`HEC-RAS` hydraulic model. :term:`HEC-RAS` is being applied to 6 selected sub-basins within the :term:`LRGV` to demonstrate the coupling of the :term:`Tier I` and :term:`Tier II` modeling frameworks within the :term:`RGVFlood` platform.
*   **Tier III** Urban Stormwater Model: Off-line Urban Stormwater model targeted for integration within the 4th quarter of 2022. The model intended for integration is :term:`SWMM`.

The structure of the Tiered approach allows or *mix-and-match* applications, where the configuration of Tiers applied to a specific problem can be tuned to the locations specific needs and hydrography. Further, the approach promotes the potential of expansion to incorporate ensemble forecasts by incorporating additional models and data within and across individual Tiers.

The Tiered modeling components are integrated into the :term:`RGVFlood` user interface components to provide a seamless user experience to maximize focus on analysis and decision making rather than data collection and model development:

.. uml::
   :align: center
   :caption: :term:`RGVFlood` User Interface Components

   package Models {
    [Tier I] as tier1
    [Tier II] as tier2
    [Tier III] as tier3
   }

   tier1 --> tier2
   tier2 --> tier3

   package UserInterface {
    [RGVFlood.com] as rgvflood
    [Wizard.RGVFlood.com] as wizard
    [RTHS.us] as rths
   }
   
   rths --> rgvflood
   rths --> wizard
   rgvflood --> wizard

   rths --> tier1
   rgvflood --> tier2

   Models --> UserInterface
   UserInterface --> Models