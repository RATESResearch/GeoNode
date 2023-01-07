Component Integrations 
======================

:term:`RGVFlood` serves as the core platform into which value-added component services are plugged-in and provided for use by the end-user.

RTHS Data API
-------------

Originally packaged with the beta release of :term:`RGVFlood`, the RTHS Data :term:`API` ingests RTHS time-series data on-demand for use by the end-user. :term:`RGVFlood` is also able to serve the data to other component services such as Flood Wizard, WRF-Hydro and the RAS Data Provider. The  RTHS Data API wil be included in the next release of :term:`RGVFlood.com`.

Flood Wizard 
------------

Flood Wizard is a Javascript Progressive Web Application developed using the Ionic framework. It was packaged with the last beta release of :term:`RGVFlood`, with the folliowing features:

* Ability to view and inspect the :term:`RGVFlood` delineated sub-basins and RTHS stations
* Ability to view and download the input data and modeling results from the Tier II modeling effots
* Overlay and compare stage height data from multiple RTHS stations

Flood Wizard was deployed to seed end-user discussion on the type of applications deemed most useful by end-users. Flood Wizard will be  included in the next release of :term:`RGVFlood.com`, incorporating user-recommended modifications and additions.

RAS Data Provider 
-----------------

The goal of this component is to generate :term:`HEC RAS` input data for selected domains from :term:`RGVFlood.com` availalble data on demand.  At the very minimum, this will include discharge data extracted from hydrologic model outputs, along with pertinent RTHS data. Other data, such as topographic and hydraulic asset surveys will also be provided. The development of this component is currently on-going.

WRF-Hydro 
----------

Although not a direct integration, the outputs of the Tier I modeling effort will be ingested into :term:`RGVFlood.com` for visualization and decision support application.  Development of this component is pending prototype deployment of the Tier I model.


