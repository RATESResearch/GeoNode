2DLevel
======
2D-capable flood models like HEC-RAS 5.0 rely less on static modeling assumptions like pre-defined flow directions, which can
reduce model-building iterations and free up more time for model calibration, quality control and sensitivity analysis. Faster computing
times, widely-available digital elevation data, and a growing pool of knowledgeable 2D modelers are making these solutions more costeffective every year. In fact, for some applications a 2D solution will produce better results in less time compared to a “simpler” 1D model.

HEC-RAS can perform 1D, 2D only, or combined 1D and 2D modeling
 * Detailed 1D modeling
 * Detailed 2D modeling
 * 2D channel with floodplain modeling
 * 1D in a channel with 2D behind levees
 * 1D channels between 2D areas
 * Simplified to detailed levee and dam breach

2D uses complicated terrains of grid cells in a mesh
 * RAS Mapper reduces it into a grid with terrain data embedded
 * The grid cells are polygon shaped (3 to 8 sides) prisms with an irregular bottom
 * The volume of the prism is a function of water surface elevation
 * The area of each face is a function of water surface elevation
 * The Continuity Equation becomes a non linear equation with water surface elevation and velocity as unknowns
 * Cell Centers: The computational center of the cell. This is where the water surface elevation is computed for each cell
 * Cell Faces: Straight or multipoint line (usually at boundary of 2D flow area)
 * Cell Face Points: Ends of the cell faces
 * Channel can be smaller than the cell size
 * Water will move thru the channel portion of the cell because details of the channel cross section are contained in the cell faces
 * The elevation-volume relationship is in the cell hydraulic properties table
 * Is you want details of what is happening within the channel, (2-D flow velocities, varying water depth, etc) then use smaller cells
 
2D Hydro Assets 
=====
Reaches with significant and complex in-channel structures or Hydro Assets (weirs, culverts, and especially bridges - pressure flow is not handled in 2D) need to be done in HEC-RAS 1D

Terrain Hydro Assets in 2D need to be entered as Break Lines.
Needed for linear features such as levees, roads, steep banks, high ground barriers, etc
* Improves terrain model
* Forces the grid cell boundaries (grid face) to match the high point
* Hydraulics is defined at the grid face
* Break lines tell HECRAS that the water can not cross without exceeding an elevation

Workflow
=====
The following is a workflow to import terrains, set break lines, and boundaries

.. list-table:: Workflow

 * - Step 
   - Action
 * - 1
   - Download Elevation DEM into Level 0-4
 * - 2
   - Open HEC-RAS
 * - 3
   - Open RAS Mapper
 * - 4
   - Right Click on Map Lawers and Add WEB Imagery Layers
 * - 5
   - Select Tools New Terrain  Make Hill Shade and Contours; Close RAS Mapper
 * - 6
   - Open Geometric Dayta Schematic
 * - 7
   -  Make Grid Mesh Model
 * - 8
   -  Make Breaklines using 2DFlow Editor
 * - 9
   -  Set Boundary Conditions
 * - 10
   -  Run the Models with Unsteady Flow Analysis

