#PHAsteroids

#This module contains the positions and velocities
#requests of -almost- any kind of celestial body 
#to the JPL Horizons Query


from phasteroids import *

#External dependencies
import numpy as np
from urllib import request
import json
from astropy.time import Time
from astroquery.jplhorizons import Horizons

class BodyJPL:
    
    """ Creates a celestial body as an object,
        using some methods from the Asteroid class"""
    
    def __init__(self, name, bodytype):
        
        """ Given a body name an a bodytype creates an object.
            Parameters:
                name (str): Name of the celestial body
                bodytype (int): Type of the body 
                                planet = 1
                                asteroid = 2
                                others = 3"""
        
        self.name = name
        self.bodytype = bodytype
        if type(bodytype) is not int:
            raise ValueError("Bodytype should be an integer. Planet = 1, Asteroid = 2, Others = 3")
        
    def get_jpl_positions(self,date):
        
        """ Given a date (in UTC format) it downloads from
            the Jet Propulsion Laboratory API the Orbital State
            Vector. 
            Parameter:
                date(str): Date in UTC format.
                
            Returns: 
                np.array([x, y, z, vx, vy, vz]): Orbital State Vector (units = AU, AU/d)"""
        
        if self.bodytype == 1:  
            JPL = Horizons(id=f'{self.ID} Barycenter', 
                           location='@sun', 
                           epochs=Time(self.date).jd).vectors()
    
            rt = np.array([JPL[c].value[0] for c in ["x", "y", "z", "vx", "vy", "vz"]])
           
        if self.bodytype == 2:
            html = request.urlopen(f"https://ssd-api.jpl.nasa.gov/sbdb.api?sstr={self.ID}&cov=mat")
            json_data = json.loads(html.read().decode())
            spkid = json_data['object']['spkid']
            JPL = Horizons(id=f'DES={spkid}', 
                           location='@sun', 
                           epochs=Time(self.date).jd).vectors()
    
            rt = np.array([JPL[c].value[0] for c in ["x", "y", "z", "vx", "vy", "vz"]])
     
        if self.bodytype == 3:
            JPL = Horizons(id=f'{self.ID}', 
                           location='@sun', 
                           epochs=Time(self.date).jd).vectors()
    
            rt = np.array([JPL[c].value[0] for c in ["x", "y", "z", "vx", "vy", "vz"]])
        
        return rt
    