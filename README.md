# PHAsteroids

## About the package
A PHA (Potentially Hazardous Asteroid) is defined as an asteroid that has a probability of hitting the Earth of $\approx 10^{-6}$ (i.e. One in a million). `PHAsteroids` is a `Python3` package intended to predict the positions during time of the asteroids and to compare with NASA Jet Propulsion Laboratory data

The position of an asteroid can be modeled as an [Multivariate Normal Distribution](https://en.wikipedia.org/wiki/Multivariate_normal_distribution) of the orbital elements $(e,\space tp,\space\Omega,\space\omega,\space i)$ and their uncertainties (standard deviations). The purpose of the package is, given an asteroid (for example 2021EU as shown below) and a date, extract the distribution parameters $(\vec{\mu},\space\hat{\Sigma})$ predict the position of the asteroid at the given date, and compare with the data given by the NASA JPL (WIP).

### Graphing Positions
> **Note**: Earth and asteroids radius are not to scale yet.

This is a graph of the Earth and 1000 possible positions (surrogates) of 2021EU on its Ephemeris Time:
<p align="center">
<img src="https://github.com/Leonarda2g/PHAsteroids/blob/e9853a1c46805c7a992fd8e505134f0eddfe6ad4/gallery/EPHEMERIS%20TIME.png" width="800"/>
</p>

According to CNEOS Sentry: Earth Impact Monitoring, 2021EU has a impact probability of $2.9*10^{-5}$ on February 27, 2024. These are 1000 surrogates of 2021EU during its "Impact Date":
<p align="center">
<img src="https://github.com/Leonarda2g/PHAsteroids/blob/6006364e71b13f4c8ddaab8f37135778f7605aaa/gallery/ET.png" width="800"/>
</p>

As you can see, while higher is the quantity of surrogates, higher is the probability of having at least one surrogate crossing the Earth's orbit and (almost) impacting it.
