########################
# P H A s t e r o i d s
########################

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
    
setuptools.setup(
    # ######################################################################
    # DESCRIPTION
    # ######################################################################
    name='phasteroids',
    author="Leonard Gómez García",
    author_email="leonard.gomez@udea.edu.co",
    description="Potentially Hazardous Asteroids: Predicting positions.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    
    # ######################################################################
    # PACKAGE
    # ######################################################################
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    
    # ######################################################################
    # REQUIRED LIBRARIES
    # ######################################################################
    install_requires=[
        'astroquery', 'ipython', 'matplotlib', 'numpy', 'astropy', 'spiceypy',
    ],

)
