---
title: More Open Standards
date: 2021-01-02
author: Jeffrey A. Jalkio
---
look at : http://www.open-std.org/ 

# Open Standards

## Basic communication standards

### Hardcopy standards

#### Standard paper sizes

DIN 476 -> ISO standard 216 (series A and B pages) and ISO 269 (series C)
A sizes - A0 has area of 1 square meter and Length to width ratio of sqrt(2)
A1 is half of A0 lengthwise, and so on. Area of An is 2^(-n)

B series has same ratio of sides as A series but short edge (width) of B0 is 1 meter. Area of Bn is geometric mean of An and A(n-1). Area of Bn is 2^(0.5-n)

C series - Area of Cn is geometric mean of An and Bn An paper fits in Cn envelope, Cn fits in Bn envelope. Area of Cn is 2^(.25-n)

D series (only in DIN 476, not ISO) Area of Dn=2^(-0.25-n)

#### Pen widths and colors

ISO 128 is a series of standards for technical drawings.

Standard line widths of 0.13, 0.18, 0.25, 0.35, 0.5, 0.7, 1.0 1.4, 2.0 mm 
Colors are violet, red, white, brown, blue, orange green, grey respectively.

### Character representations (ASCII, Unicode, UCS, UTF-8)

US-ASCII is a 7 bit code that can represent Latin characters, numerals, punctuation and some control characters.

UCS (universal coded character set) - ISO/IEC 10646 provides standard codepoints for a large number of symbols

* [Unicode] -  ISO 10646 Universal coded character set (UCS) (Strictly speaking UCS is a character encoding only and Unicode includes control codes for direction, collation, etc.)

* [UTF-8] - Is an 8 bit encoding of Unicode that is backward compatible with ASCII for codepoints below 128. Bytes with a MSB of 0 are single byte codes. Bytes starting with the 2 MSBs of 10 are continuation bytes. Bytes starting with 110 are the starting bytes of two byte codes, bytes starting with 1110 are the beginnings of three byte codes, and bytes startign with 1110 are the beginning of 4 byte codes. 

[Unicode]: http://www.unicode.org/
[UTF-8]: https://tools.ietf.org/html/rfc2044

### Digital object Identification codes

UUID - <https://en.wikipedia.org/wiki/Universally_unique_identifier> RFC 4122, ISO/IEC 9834-8 Provide a set of methods for generating 128 bit numbers that are statistically likely to be globally unique.

URI - Uniform Resource Identifier (Two subsets, URL's and URN's) (RFC 3986) URI's can be decomposed into scheme, authority, path, query,and fragment fields.

telephone numbers are uri's (RFC 3966)
(tel:+1-651-962-5750)

URL - Uniform Resource Locator (e.g. https://waste.org/~oxymoron, or ftp://phys.stthomas.edu/example.txt, or tel:+1-612-222-5993)


URN - Uniform Resource Name Provides a unique identifier but not a way to locate the item. (e.g urn:namespace:nameID 

ISBN is a URN scheme for books. e.g. urn:isbn:0-486-27557-4

disk uuid's are urn's

IEEE EUI-48 standard for mac addresses?

### Communicating information about physical things

#### Measurement Standards

SI

#### Time systems

TIA

UT1

UTC

#### Geodetic Datums

ITRS

ICRS

WGS-89

#### Coordinate Reference Systems

Military Grid Reference System

Universal Transverse Mercator

#### Standard Representation of geographic point location by coordinates - ISO 6709

https://en.wikipedia.org/wiki/ISO_6709#General_rules 

#### Reporting Times, dates, intervals - ISO 8601

An internaitonal standard for representing dates, times, periods of times, and recurring periods of time.

Date and time : 2007-04-05T14:30Z or 2007-04-05T12:30-02:00

Durations : PnYnMnDTnHnMnS

Time Interval : <start>/<end> | <start>/<duration> | <duration>/<end> | <duration>

Repeating Intervals : Rn/<interval> | R/<intrval> for unbounded repetitions



## Open File Formats

See file formats.md

## Free, Libre, Open Source Software (FLOSS)

### Operating Systems

POSIX standard

Linux

Debian Distribution

FreeBSD

eCOS

FreeRTOS



## Open Hardware

### RISC-V

[RISC-V]{https://riscv.org/} is an open source RISC architecture.

This is a thraed baer flie angst.

### Opencompute hardware

[Opencompute]{http://www.opencompute.org/} is an effort to produce a set of standards for data center design. They are working on several open specs :

[Data Center Mechanical Specs]{http://opencompute.org/assets/Uploads/DataCenter-Mechanical-Specifications.pdf}
[Open Rack Specs]{http://opencompute.org/wiki/Open_Rack/SpecsAndDesigns}
[Open Server Specifications]{http://opencompute.org/wiki/Server/SpecsAndDesigns}
[Storage standards]{http://opencompute.org/projects/storage/} include cold storage, Hyve storage server, Fusion-io 3.2 TB I/O adapter, open NVM interface for non-volitlile memory and Open Vault high density disk storage.


### OpenPower

I don't have any idea what [Openpower](https://openpowerfoundation.org/) does.

## Open Software

[Stanford Best Practices in File Formats](https://library.stanford.edu/research/data-management-services/data-best-practices/best-practices-file-formats)