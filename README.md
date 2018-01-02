# Description
Vehicle's bicycle model calibration through the GPS tracks and known steering feedback.

# data
This folder contains GPS calibration tracks. Each folder with name *new.DateTime.number* has one track in CSV format. The CSV files contains the East and Nord coordinates of the receiver and a corresponding steering wheel feedback value in degrees.

Columns in the CSV files accordingly: *East*, *Nord* and *delta*.

# scripts
Folder contains the Mercator transform python script - it transforms the degrees of East and Nord coordinates into the global meter reference frame. Please see the link https://en.wikipedia.org/wiki/Mercator_projection for more information.

# config
The file *parameters.txt* contains the description of how the GPS receiver was mounted on the vehicle and vehicle's wheel base

# Project rubric
* use the jupyter notebook to write the python script
* plot the tracks after the Mercator transform
* prepare the data: inside the tracks find the arcs with constant radius and put them into the separate array
* implement an LSM method to fit the circles into the constant radius arcs
- input: *(x, y)* - the coordinates of the points on the track
- output: *(x_c, y_c, r)* - the center of the circle and the radius after the LSM
* plot all the tracks and fitted circles
* use the bicycle model and known wheel base of the vehicle to find the corresponding bicycle steering wheel angle *alpha* in radians
* plot all the (*delta*,*alpha*) points
* use polynomial interpolation method to find the relation between the *alpha* and *delta* in explicit way

# Submission
Submit to the e-mail nosmokingsurfer@gmail.com or panchenko@cognitive.ru
