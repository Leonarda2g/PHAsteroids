#PHAsteroids

#__INIT__ MODULE

import os

#Support class to import external files
class Files(object):
    def get_data(path):
        """
        Given a filename returns the path where is located.
        
        Parameter:
            File (str): Filename
            
        Returns:
           Path (str): Location of the file
            
        """
        
        try:
            FILE=__file__
            ROOTDIR=os.path.abspath(os.path.dirname(FILE))
        except:
            import IPython
            FILE=""
            ROOTDIR=os.path.abspath('')
    
        return os.path.join(ROOTDIR,'data',path);

from phasteroids.bodyjpl import *
from phasteroids.asteroid import *