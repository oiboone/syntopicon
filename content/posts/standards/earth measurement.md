---
title: Earth Measurement Standards
date: 2021-01-02
author: Jeffrey A. Jalkio
---

#System of Units

SI (International System of Units) as promulgated by the BIPM (International Bureau of Weights and Measures), a technical committee, which reports to the CIPM (International committee for weights and measures) that makes recommendations to the CGPM (General Conference on Weights and Measures) that consists of representatives from all countries that are signatories of the meter convention of 1875. 

IEEE-1541 defines binary prefixes for powers of 1048 rather than powers of 1000.

#International Earth Rotation Service

Responsible for maintaining global time and reference frame standards. Since there is slow movement of plates relative to the earth, the reference meridian is determined via satellites, lunar ranging, and very long baseline interferometry.

# International Terrestrial Reference System an Frame

Specifies prime meridian and location of pole for standardized latitude and longitude.

# World Geodetic System (WGS 84)

Coordinate origin at Earth's center of mass (believed accurate to less than 2 cm) North through axis of rotation. Zero longitude in direction of IERS reference meridian.

Datum surface is an oblate spheroid with a specified equatorial radius and a specified flattening at the poles.
Defining constants are equatoriall radius, flattening, and gravitational constant (GM)

The Earth Gravitational Model EGM96 geoid defines a nominal sea level by means of a set of spherical harmonics up to 360th order, while the EGM2008 uses at least 2159 spherical harmonics.

The World Magnetic Model (WMM) is realeased at 5 year intervals to model the magnetic potential (hence magnetic declination)

# Reporting Geographic Coordinates

## Standard Representation of geographic point location by latitude, longitude and altitude coordinates - ISO 6709

<https://en.wikipedia.org/wiki/ISO_6709#General_rules> 

## Universal Transverse Mercator and Polar Mercator Systems (UTM)

Collection of 60 Transverse Mercator projections (cylindircal projections with cylinder axis on equator rather than through the poles). By limiting each zone to 6 degrees, the system reduces the distortion of projection in each zone. The Universal Polar System allows a single projection at each pole. <https://www.movable-type.co.uk/scripts/latlong-utm-mgrs.html>

## Military Grid reference system

MGRS is used by NATO militaries and uses the Universal Transverse Mercator (UTM) grid system and universal polar stereographic (UPS) system at the poles to provide map coordinates for the entire Earth.

Between 80 degrees South and 84 degrees North longitude, the first digit or pair of digits specifies 1 of 60 longitude zones. With zone 1 starting at 180 degrees west and progressing eastward.

This is followed by a single character specifying one of 20 8 degree wide latitude bands starting with C at 80 degrees south and progressing to X (skipping I and O). The X band extends to 84 degrees North to cover all land mass.

In the polar regions, there is no leading number. A specifies the west half of the south pole and B the east half, while Y specifies the west half of the north pole and Z the east half. 

Together, this leading number letter pair specifies a grid zone.

The next two letters specify a 100 Km square with the first character providing the column and the second character the row within the grid zone. The column letter starts at A in grid 1, J in grid 2, and S in grid 3, progressing eastward. The row letter starts at A in odd numbered zones and F in even numbered zones and increases north.

The remaining digits specify an X,Y coordinate within that square. The first half of the remaining digits specify easting, the second half northing.

<https://www.movable-type.co.uk/scripts/latlong-utm-mgrs.html>

## NAD-83, ETRS89, GDA94

Local geodetic datums that allow coordinates within a continent to remain unaffected by tectonic shifts.

# Time

#### Time systems

Nice reference here <http://irtfweb.ifa.hawaii.edu/~tcs3/tcs3/Misc/about/time.pdf>

Barycentric coordinate time - based on SI second at center of mass of solar system

Terrestrial Time (aka terrestrial dynamical time (TDT))- at surface of the earth (same rate as TIA but wiht offset of 32.184 s)

Geocentric coordinate time - at center of mass of earth

TIA - International Atomic Time. Based on the SI second, with constant incrementing from a fixed start point.

UT - Mean solar time at the prime meridian. 

UT1 - Mean solar time at prime meridian as determined by long baseline interferometry of distant quasars, laser ranging of the moon, and GPS orbits. UT1 is related to the earth's rotation angle (ERA) by :

ERA = 2π(0.7790572732640 + 1.00273781191135448Tu) radians
where Tu = (Julian UT1 date - 2451545.0)[13]

UTC - atomic timescale based on TIA with leap seconds added to keep within 0.9 s of UT1

#### Reporting Times, dates, intervals - ISO 8601

An international standard for representing dates, times, periods of times, and recurring periods of time.

Date and time : 2007-04-05T14:30Z or 2007-04-05T12:30-02:00

Durations : PnYnMnDTnHnMnS

Time Interval : <start>/<end> | <start>/<duration> | <duration>/<end> | <duration>

Repeating Intervals : Rn/<interval> | R/<intrval> for unbounded repetitions

