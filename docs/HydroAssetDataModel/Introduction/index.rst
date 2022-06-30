Introduction
=============

This research document summarizes the Hydrological Asset Data Model HEC-RAS (Hydrologic Engineering Center's (HEC) River Analysis System software (RAS) HEC-RAS:
 * one-dimensional (1D) Steady and Unsteady
 * two-dimensional (2D) Unsteady Flow.

Hydrological Asset Data Model includes the files to make a HEC-RAS 1D and 2D analysis that includes:
 * HEC-RAS project file (*.prj)
 * Geometry file (*.g01)
 * Unsteady flow file (*.u01)
 * Plan file (*.p01)
 * RAS Mapper file (*.rasmapper)
 
 
 Geometry files contain all the geometric data or Hydro Assets such as:
 * Cross section information; 
 * Hydraulic Structures; Bridges, Wiers, Culverts
 
 Users shall create proper data engineered file structuire to store imported and created files such as
 
 * Aerial photos
 * Hydrology
 * Land use
 * Projection
 * Results
 * Terrain
 * Shape files
 * DWG_DXF
  * Catchment delineations
  * Flow paths
  * Cross section and long section profile alignments
  * Roadway or levee centreline alignments
  * Building footprints
  * Structures

Elevations
=====
HECRAS uses a GeoTiff file format
 * Terrain needs to capture overbank and main river channel
 * LiDAR for overbank and shallow water
 * SONAR for deep water
 * TINS are used because they can be irregular. Lots of points in the channel and fewer in flat overbank
 * Good to have imagery with the elevation data to get a complete picture
 * Verify and proof data
 *  Imperfections in LiDAR data translate to model errors
 * Examine structures that cross rivers.
 * Screen vegetation
 * Over water returns need to be replaced with bathometric data

This document is not intended to replace the HEC-RAS documentation at the US Army Corps of Engineers at https://www.hec.usace.army.mil/software/hec-ras/documentation.aspx

 
