import numpy as np
import zipfile
import crust1
from os import remove
from simplekml import Kml, Style

# Create an instance of Kml
kml = Kml(open=1)
fol = kml.newfolder(name="Crust 1.0")


def convert_to_html(model):
    """
    Takes a model instance and produces an HTML table that represents the
    results in a nice way for us to look at.

    Parameters
    ----------
    model : dict
    Dictionary of layers and their properties as a list in the form of
    [Vp, Vs, rho, thickness, top]

    Returns
    -------
    html_str : str
    Nicely formatted HTML table of the model results.
    """

    layer_labels = ["Water", "Ice", "Upper_Seds.", "Middle_Seds.",
                    "Lower_Seds.", "Upper_Crust", "Middle_Crust",
                    "Lower_Crust", "Mantle"]
    header = ["Type", "Vp", "Vs", "Density", "Thickness", "Top"]

    layer_names = ["water", "ice", "upper_sediments",
                   "middle_sediments", "lower_sediments",
                   "upper_crust", "middle_crust", "lower_crust", "mantle"]

    # Make the table with HTML
    html_str = "<table width=\"350\" border=\"1\">\n"
    html_str += "\t<tr>"

    # Header row
    for h in header:
        html_str += "\t\t<td>%s</td>\n" % h
    html_str += "\t</tr>\n"

    # Row for each layer (if it exists)
    for i, layer in enumerate(layer_names):
        if layer in model:
            # Layer label in first column
            html_str += "\t<tr>\n"
            html_str += "\t\t<td>%s</td>\n" % layer_labels[i]

            # Get and write layer data
            row = model[layer]
            for item in row:
                html_str += "\t\t<td>%s</td>\n" % item

            html_str += "\t</tr>\n"

    # Close table
    html_str += "</table>\n"

    return html_str

# The model is defined from 89.5 to -89.5 latitude and -179.5 to 179.5
# longitude in 1 degree increments, we'll work with each cell
lats = np.arange(89.5, -90, -1)
lons = np.arange(-179.5, 180, 1)

# Make model instance
model = crust1.crustModel()

# Use a style for the points, this will save space in the kml file
style = Style()
style.iconstyle.icon.href = 'http://maps.google.com/mapfiles/kml/pal4/icon49.png'
style.labelstyle.scale = 0

# Run the model for each lat and lon pair
print "Running model worldwide..."
for lon in lons:
    for lat in lats:
        model_results = model.get_point(lat, lon)
        result_html = convert_to_html(model_results)

        pnt = fol.newpoint()
        pnt.name = "CRUST 1.0 (%.1f,%.1f)" % (lat, lon)
        pnt.description = result_html
        pnt.coords = [(lon, lat)]
        pnt.style = style


# Save the KML
print "Writing KML file..."
outfile = 'CRUST_1.0'
kml.save('../%s.kml' % outfile)

# Try to compress it to KMZ, if we can, the delete the kml, otherwise
# we're done and we'll show a message indicating the outcome. zlib is
# required for this, otherwise the file size won't be reduced
try:
    import zlib
    compression = zipfile.ZIP_DEFLATED
    print "zlib present: will be stored in compressed format"
except:
    compression = zipfile.ZIP_STORED
    print "zlib not present: will be stored in uncompressed format"

with zipfile.ZipFile('../%s.kmz' % outfile, 'w') as zf:
    print "Zipping KML file to KMZ..."
    zf.write('../%s.kml' % outfile, compress_type=compression)
    remove('../%s.kml' % outfile)
