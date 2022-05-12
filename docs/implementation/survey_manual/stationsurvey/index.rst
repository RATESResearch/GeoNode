RATES Station Benchmark Site Surveying
=========================================

A 3D model of the RATES Station Benchmark Site Surveying shall be conducted with the requested two methods.

Method 1- Unmanned Aircraft System (UAS)
=========================================

A UAS utilizes hardward and software to generate a 3D point cloud Digital Surface Model (DSM) of the RATES Station Benchmark Site. Only 14 CFR FAA 107 Certified Remote Piolts for commericial operation shall have conduct UAS Surveys.  The Operations Over People rule became effective on April 21, 2021. Drone pilots operating under Part 107 may fly at night, over people and moving vehicles without a waiver as long as they meet the requirements defined in the rule. Airspace authorizations are still required for night operations in controlled airspace under 400 feet.  Certified Remote Pilots are full responsible for opperation of UAS for RATES Station Benchmark Site Surveying. Operators shall create their own safety standards to meet their professional and certification requirments. 

Equipment
------------

UAS 
 - All equipment and accessories will be modern, undamaged, and not reconditioned, remanufactured, nor recertified. All equipment software should be current to the manufactures releases.
 - UAS equipment used shall be capibile of working with Pix4Dcapture that can be found at `Suported Drones Pix4Dcapture <https://support.pix4d.com/hc/en-us/articles/203991609-Supported-drones-cameras-and-controllers-PIX4Dcapture>`_
 - Smartphone suport Pix4Dcapture

GNSS
 - GNSS equipment used for Ground Control Points (GCPs) shall be a Real Time Kinematic (RTK) GNSS rover equipment, operating at centimeter-level (i.e. survey-grade) 
accuracy.

Ground Targets
 - GCPs are a points with of known coordinates in the area of interest. Coordinates are measured with GNSS RTK surveying methods and used to georeference the generated point cloud.
 - 10 highly visible GCP targets shall be set at the RATES Station Benchmark Site to obtain the coordinates needed to georeference and check the generated point cloud.


Software
---------

Pix4Dcapture
 - RATE's Pix4D account or consultant Pix4D account should be used to login intitate Pix4Dcapture. Logging in requires Internet connection. It can be skipped up to five times so that the app can be temporarily used without login. The Login screen has several items.

Suncalc
 - `SunCalc <https://www.suncalc.org/>`_ should be used to determine the best sun angle to reduce the shadows that effect the 3D modeling

Workflow
-----------

The following is the general workflow.  Please refer to the Pix4Dcapture manual details.

.. code-block:: yaml
1. Optain 14 CFR FAA 107 Certified Remote Piolts
2. Complete the RATE's Tutorial on UAS Station Benchmark Surveying Training
3. Verify all equipment is charged and updated with current software.
4. Verify that a rights and premissions to opperate UAS at RATES Station Benchmark Site are secure.
5. Set GCPs 
 - Place in a geometeric distribution 
 - At least 6 targets should be placed per site to ensure the algorithm will run successfully.
 - Targets should be separated by at least 10 meters (~30 ft).
 - Targets should be placed on flat and static surfaces.
 - Targets should always be visible in the images that capture the location of the target.The mark must be durable, have a stable setting, and good satellite visibility.
 - Collect RTK solutions on each GCP
6. Configure Pix4Dcapture
.. figure:: pix4dcapture.PNG
 - Select Dobule Grid 3D Mission
 - Select safe flying heith that generates a minimal Ground Sample Distance (GSD) of 0.80 in/pixel
 - Select Angle Camera at 60%
 - Select Front and Side Overlap of 85% 
 - Select Drone Speed Normal
7. In the Map view move Area of Interest (AOI) mission area centered on RATES Station Benchmark Site and resize to capture topographic relief area needed for best surface model (For example 300' x 300'). 
8. Collect data following your safety standards.
9. Consider a second backup data collection, but rotate the AOI 45 degrees from first flight mission.
10. Additional images might be necssary to obtain under any structures using the Pix4Dcapture Circular for signle model.
11. Download to RATES shared drive
 - All images
 - GCP RTK solutions following Survey Data Model
 - Pix4D mission Project files
12. Consultant or RATES will process captured images and GCP using Pix4Dmapper
13. RATES will notify professional of the acceptance of tne RATES Station Benchmark Site survey

  
.. note::
 
Point cloud results will be tested in RATES mapping software against existing surface and surveying models.


Method 2- Conventional RTK GPS Topographic Survey
=========================================



Equipment
------------

GNSS
 - GNSS equipment used for Ground Control Points (GCPs) shall be a Real Time Kinematic (RTK) GNSS rover equipment, operating at centimeter-level (i.e. survey-grade) 
accuracy.



Sketches
---------

A survey sketch should be prepared at all hydraulic features; including cross sections. The sketch should include notations and measurements representing the structural 
geometry and the natural ground and show description codes and shot numbers from the field survey so that the sketch can be related to the field survey. Each sketch should include a planimetric and profile view (viewed looking downstream left to right, upstream face of structures) and show the following items: piers/piles, channel banks, channel, direction of flow, rails, deck, footings, abutments, culvert inverts, shape and size of opening, bench mark location, skew to flow, and north arrow

Data
-----

The L_Survey_Pt table is required for field survey data generated.

Workflow
-----------

The following is the general workflow.  Please refer to the Pix4Dcapture manual details.

.. code-block:: yaml
1. Blah
2. Blah
3. Blah
  - yes
  - no
  - Yes
Point cloud results will be tested in RATES mapping software against existing surface and surveying models.
