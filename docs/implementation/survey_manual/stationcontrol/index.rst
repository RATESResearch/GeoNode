RATES Station Control Benchmark Surveying
=========================================

To ensure that the best horizontial and vertical coordinates to determine the elevation of the RATES Station NOAA NGS Online Processing User Service (OPUS) Shared Static Solutions will be used.

Monuments:
-----------

Monument locations shall be installed in a stable surface that is not subject to effects of geologic and soil activity in the region, in accordance with Geospatial Data Model. 

Monuments must be highly visible away from vegetation, moving structures, or high traffic areas subject to movements. Descriptions of monuments should be added to the NOAA NGS OPUS Shared Solutions.

Monuments shall be navigated to using the record coordinates  obtained from OPUS. 

NOAA NGS OPUS Shared Soluions. 
--------------------

NOAA NGS OPUS Shared solutions shall be used to process and publish the location of the RATES Station Control Benchmark.  When possible, Static observations shall be collected on the GNSS Reference Station  simultaneous to all reference monuments being observed, to ensure  simultaneous data is collected on both the reference station and all 
reference monuments for final evaluation and approval of adjusted coordinates.

The residual error shall be noted shall  be within tolerances set forth. 
Your shared solution must be a high-quality solution:
 - ≥ 70% observations used and ambiguities fixed
 - ≤ 3 cm RMS
 - ≤ 4 cm peak-to-peak error ranges for latitude and longitude
 - ≤ 8 cm peak-to-peak error range for ellipsoid height

Workflow
-----------

The following is the general workflow.  Please refer to the NGS OPUS Shared Static Solutions for more details.

.. code-block:: yaml
1. Complete the NGS and RATE Tutorial on How to Submit an OPUS Share Observatoin
2. Refer to the referenced Documents for setting NGS Monuments and Submit an OPUS Share Observatoin
3. Utilize Multi Frequency GNSS Receiver
4. Utilize a Fixed Height Pole with proper tripod legs
5. Scout the location and set a Station Mark
 - Marks are defined IN USGS TM3A19 or `NGS Special Application Mark Description <https://geodesy.noaa.gov/marks/descriptors.shtml#setting>`_
 - The mark must be durable, have a stable setting, and good satellite visibility.
 - Follow safety procedures and sign notification when occupying location.
 - Obtain pictures of mark for OPUS Shared Observer Field Log
6. Place GNSS level on RATES Station Benchmark Contorl Point
7. Start Survey: Collect RINEX 3 data (Conversion from Vendor format to Rinx may occur in office download) for 4 hours and 15 minutes.
8. Occationally check level of instrument and note time checked.  If off more then half bubble stop measuring.  Level and restart 4 hours and 15 minutes.
9. Complete `Observer Field Log for GNSS Surveys <https://geodesy.noaa.gov/surveys/forms/obslog-OPUS.pdf?>`_
  - Obtain pictures of setup
  - Obtain measurments and description to find RATES Station Control
10. Optional: `Complete Visibility Obstruction Diagram <https://geodesy.noaa.gov/surveys/forms/#visibility>`_
11. End Survey: Stop Collecting after 4 hours and 15 minutes
12. Occupy RATES Station Benchmark Control Point with your RTK GPS twice with a complete loss of lock between occupations
13. Download to RATE Shared Site under \Station\01_BM\RINEX
  - If collected in Vendor format please place Vendor format file in RATE Shared Site under \Station\01_BM\RINEX
13. DO NOT UPLOAD to OPUS Shared Solutions
14. Upload to regular OPUS and submit PDF of email results to \Station\01_BM\OPUS_RESULTS
15. Place all Images and Observation Feild Logs in \Station\01_BM\FIELD_NOTES
16. Place the two (2) RATES Station Benchmark Control Point RTK GPS Solutions:
  - In X,Y, Z (m); Lat, Lon, ellipsoidal height (ftus); Northing, Easting, Orthometric Height (ftus) with RMS in File format outlined in Geospatial Data Model document in the \Station\01_BM\RTK directory 
  - In any raw vendor data format \Station\01_BM\RTK directory 
  
.. note::
 
Your shared solution must be a high-quality solution:
≥ 70% observations used and ambiguities fixed
≤ 3 cm RMS
≤ 4 cm peak-to-peak error ranges for latitude and longitude
≤ 8 cm peak-to-peak error range for ellipsoid height
