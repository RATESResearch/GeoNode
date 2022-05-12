Geodetic Datums and Units
==========================

Please refer to the Geospatial Data Model for more details on submitted data format, units, and methods.  All points collected must be supplied in all units stated:

- Cartesian Coordinates
- Geodetic Coordinates
- Grid Projected State Plane Coordinates

Units
-----

.. list-table:: Supplied Coordinates
  :widths: 25 25 50
  :header-rows: 1
  
  * - Coordinate
    - Units
    - Format
  * - Cartesian Coordinate 
    - Meters (carried out to .001 meter)
    - X, Y, Z 
  * - Geodetic Coordintes
    - DMS Degrees, Minutes, and Seconds with 8 decimals, Ellispoidal Height US Survey Feet (carried out to .001 feet)
    - Latidue, (-)Longidude, Ellipsoidal Height 
  * - Grid Projected State Plane  Coordinates
    - Feet Horizontal coordinates and Orthometric Height (carried out to .001 feet)
    - Northing, Easting, Orthometeric Height
    
.. note::

Currently, U.S. Survey Feet is used in Texas. (Adoption of International Feet is expected.)

Horizontial Datum
-----------------
Unless otherwise expressed State Plane Coordinate System in NAD83 (2011) with GRS 1980 Ellipsoid is used for all RATES projects.

Vertical Datum
--------------
Unless otherwise expressed NAVD 1988 with the most current Geoid should.
