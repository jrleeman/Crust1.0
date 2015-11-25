# Crust 1.0 and Google Earth
![](docs/header_image.png)

This project is a python adaptation of the Crust 1.0 model that also makes a kmz
file to view the model with Google Earth. The Crust 1.0 model is a product of
Gabi Laske, Zhitu Ma, Guy Masters ([UCSD](http://ucsd.edu)) and Michael
Pasyanos([LLNL](https://www.llnl.gov)). More information about the model and the
original FORTRAN routines can be found on the [Crust 1.0
webpage](http://igppweb.ucsd.edu/~gabi/crust1.html).

In this repository there is a pythonic way to access the model as well as a tool
to produce a KMZ file to allow exploration of the model through the intuitive
interface of [Google Earth](https://www.google.com/earth/). The final KMZ is
also included so you don't have to use the Python scripts unless you want to
modify anything or access it from your own program.

## How do I use it?
If you just want to use the [Google Earth](https://www.google.com/earth/) file,
simply download the repository by clicking the "Download Zip" button above.
Unzip the file and find the KMZ file. Open it in [Google
Earth](https://www.google.com/earth/) and explore by clicking on a red point.
The pop-up box will show you the latitude and longitude of that point and the
information for each layer of the model. Information includes the
[P-wave](https://en.wikipedia.org/wiki/P-wave) speed [km/s],
[S-wave](https://en.wikipedia.org/wiki/S-wave) speed [km/s],
[density](https://en.wikipedia.org/wiki/Density) [g/cc], layer thickness [km],
and elevation of the top of the layer with respect to sea level [km]. If you're
not familiar with the structure of the Earth, explore some
[activities](activities/) and read about the [structure of the
Earth](https://en.wikipedia.org/wiki/Structure_of_the_Earth). You can copy and
paste information out of the pop-up box as plain-text. Try exploring the
different types of crust (continental and oceanic), noting differences between
them.

## Where are things?
* The final KMZ file for [Google Earth](https://www.google.com/earth/) is in the main directory.
* Activities for students are collected into subfolders in [activities](activities/).
* Images and other things used for the documentation are in [docs](docs/).
* The Python files and model data in all in [model](model/).

## Contributing
We always welcome new ideas and improvements. Feel free to fork the repository
and make modifications, file issues, etc. You can always email the authors for
more information.

John Leeman : jleeman@psu.edu
<br>Charles Ammon : charlesammon@psu.edu
