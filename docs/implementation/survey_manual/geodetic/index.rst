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
  * - Geodetic Coordinates
    - DMS Degrees, Minutes, and Seconds with 8 decimals, Ellipsoidal Height US Survey Feet (carried out to .001 feet)
    - Latitude, (-)Longitude, Ellipsoidal Height 
  * - Grid Projected State Plane  Coordinates
    - Feet Horizontal coordinates and Orthometric Height (carried out to .001 feet)
    - Northing, Easting, Orthometric Height
    
.. note::

Currently, U.S. Survey Feet is used in Texas. (Adoption of International Feet is expected.)

Horizontal Datum
-----------------
Unless otherwise expressed State Plane Coordinate System in NAD83 (2011) with GRS 1980 Ellipsoid is used for all RATES projects for final products.

Vertical Datum
--------------
Unless otherwise expressed NAVD 1988 with the most current Geoid should.

Conversions
--------------
Conversions between Geodetic and Grid coordinates shall be consistent with published standards and methods uses shall be documented with all deliverables.

Transformation
---------------
Transformations between datums shall be consistent with published standards and methods uses shall be documented with all deliverables.
