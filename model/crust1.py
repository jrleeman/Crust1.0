import numpy as np
from math import floor


class crustModel:
    """
    Top level model object to retreive information from the LLNL Crust 1.0
    model.

    Attributes
    ----------
    vp : ndarray
    P-wave velocity model

    vs : ndarray
    S-wave velocity model

    rho : ndarray
    Density model

    bnds : ndarray
    Elevation of the top of the given layer with respect to sea level model

    layer_names : list
    Names of the nine possible layers in the model
    """

    def __init__(self):
        # Read in data files
        self.vp = np.loadtxt('crust1.vp')
        self.vs = np.loadtxt('crust1.vs')
        self.rho = np.loadtxt('crust1.rho')
        self.bnds = np.loadtxt('crust1.bnds')

        # Reshape to a lon,lat,layer grid. The 0,0 index value
        # is at 90 south and 180 latitude.
        self.vp = self.vp.reshape((180, 360, 9))
        self.vs = self.vs.reshape((180, 360, 9))
        self.rho = self.rho.reshape((180, 360, 9))
        self.bnds = self.bnds.reshape((180, 360, 9))

        self.layer_names = ["water", "ice", "upper_sediments",
                            "middle_sediments", "lower_sediments",
                            "upper_crust", "middle_crust", "lower_crust",
                            "mantle"]

    def _get_index(self, lat, lon):
        """
        Returns in index values used to query the model for a given lat lon.

        Paramaters
        ----------
        lat : float
        Latitude of interest

        lat : flaot
        Longitude of interest

        Returns
        -------
        ilat : int
        Index for given latitude

        ilon : int
        Index for given longitude
        """

        # Make sure the longitude is between -180 and 180
        if lon > 180:
            lon -= 360
        if lon < -180:
            lon += 360

        # Find the index in the data for given lat and lon
        ilat = floor(90. - lat)
        ilon = floor(180 + lon)

        return int(ilat), int(ilon)

    def get_point(self, lat, lon):
        """
        Returns a model for a given latitude and longitude. Note that the model
        is only defined on a 1 degree grid starting at 89.5 and -179.5.

        Paramaters
        ----------
        lat : float
        Latitude of interest

        lat : flaot
        Longitude of interest

        Returns
        -------
        model_layers : dict
        Dictionary of layers with the keys as layer names and the values as
        a list of vp, vs, density, layer thickness, and the top of the layer
        with respect to sea level.
        """

        # Get index for arrays of data at this location
        ilat, ilon = self._get_index(lat, lon)

        # Calculate the thickness of the layers, add zero to the end
        # for the mantle since it's not defined
        thickness = np.abs(np.ediff1d(self.bnds[ilat, ilon], to_end=[0]))

        model_layers = dict()

        for i, layer in enumerate(self.layer_names):
            vp = self.vp[ilat, ilon][i]
            vs = self.vs[ilat, ilon][i]
            rho = self.rho[ilat, ilon][i]
            bnd = self.bnds[ilat, ilon][i]
            layer_thickness = thickness[i]

            # If the layer has thickness or is the mantle, write it
            if layer_thickness >= 0.01 or layer == "mantle":
                model_layers[layer] = [vp, vs, rho, layer_thickness, bnd]

        return model_layers
