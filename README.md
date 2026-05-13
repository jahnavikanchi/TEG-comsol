# TEG-comsol
Thermoelectric Generators - A COMSOL Study of the Geometry

## What This Project Is About
In this project, we focused on the geometric optimisation of a thermoelectric generator while keeping Ag₂Se as the n-type thermoelectric material.

Using Python, we generated around 5000 unique geometry combinations by varying important design parameters such as thermoelectric leg dimensions, interconnect dimensions, filling factor, material widths, contact resistivity, input heat flux density, and hot-side temperature.

These generated cases were then simulated in COMSOL Multiphysics using a parametric study. The simulation results were collected into a dataset and later used for machine learning-based geometric optimisation.

