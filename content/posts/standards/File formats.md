---
title: "Preferred File Formats"
author: Jeff
date: 2019-09-18
---

## Open Formats

* Published Specification
* Maintained by a standards organization
* Usable by anyone at no monetary cost
* <https://en.wikipedia.org/wiki/Open_format>
* <https://library.stanford.edu/research/data-management-services/data-best-practices/best-practices-file-formats>

## Documents

Recomendations:

i) Pdf/a for distribution of documents
ii) Ooxml for Microsoft office documents
iii) Open document format for open office documents
iv) Html in utf-8 for web pages
v) Latex in utf-8 for technical article source
vi) Plain text in utf-8

### Portable Document Format - PDF - ISO 32000-1:2008 

Started as proprietary Adobe format. Standardized by ISO but stilll contains references to proprietary Adobe components.

PDF/A is the standardized subset of PDF features intended for archived documents to permit easy reading long into the future. Requires that fonts and graphics are embedded into file. PDF/A-2u or PDF/A-2a (for accessible files)

#### Alternatives

DjVu - for scanned documents???

### Open document format - ODF - ISO/IEC 26300 

Open format for word processor, spreadsheet, presentations, graphics, and formulas. Used by libre-office. Standard itself is open and freely available. 

#### Alternatives

docx - opn office XML format from Microsoft

### Rich Text formats 

Text file formats for describing formatting as well as text. 

* LaTeX - LaTeX was developed for publishing and is fairly complex. 
* HTML - Hypertext Markup Language was designed for web page description
* CSS - style sheet format to be used with HTML
* Markdown - Markdown can be processed into formatting for webpages, paper, or other forms but is not well standardized.

## Data serialization and configuration data formats

### Text formats

* [XML] - Extensible Markup Language - High overhead due to multicharacter tags and closing tags for each data element. A pain to read or write by hand but easy for machine parsing. Each field has a start and end tag "<name> value </name>" which makes it verbose but unambiguous. Commonly used for descriptions of objects. Metadata can be assigned to data by inserting name=data pairs inside the name tag. XML schema can be created to specify the format of data structures and validate data sets. The XPath query system can be used to query data in XML format. XSL can be used to transform one XML document into another. Many specific data format standards are based on XML.

* [JSON] - JavaScript Object Notation - Simpler encoding for XML type structures. Uses Name/value pairs separated by colons and surrounded by curly brackets. Also allows arrays and objects.Uses curly braces to delimit start and end of structures, square brackets to indicate start and end of arrays, and name:value pairs to indicate name and value of fields. Items within structures and arrays are separated by commas. Commonly used for data transfer. Strings (including names of variables) are enclosed in double quotes. JSON is intended for data transfer and is widely supported in programming libraries.

* [YAML] - YAML ain't Markup Language - Simpler than JSON. Uses vertical alignment to indicate structure. Can use curly brackets for lists and square brackets for arrays so JSON is a valid subset of YAML. Widely used as a language for configuration fields or document metadata headers. Unfortunately, slower to serialize than json. Mostly a superset of JSON (but duplicate keys can be valid JSON but not valid in YAML). name:value pairs need not be quoted. Arrays are structures with numeric keys, but can also be indicated with square brackets or dashes before elements. References are allowed in YAML data structures, for example a: &b indicates that a is a pointer to b. YAML uses whitespace indentation to indicate levels in structure. Might be preferred for human maintained files.

* TOML - Another human readable format similar to the old .ini files for configuration data.

* CSV - comma separated variables

[YAML]: http://yaml.org/
[XML]: http://www.w3schools.com/xml/ 
[JSON]: http://www.json.org/


### Scientific data exchange formats

* SDXF standardized in RFC 3072, general purpose <https://en.wikipedia.org/wiki/SDXF>
* FITS (Flexible Image Transport System) - used for astronomical images
* ASDF proposed modern replacement for FITS
* NetCDF
* HDF (Hierarchical Data Format)
* Simple Data Format (This webpage has a nice summary of pros and cons of various scientific data formats : <http://solarmuri.ssl.berkeley.edu/~fisher/public/software/SDF/SDF-intro-2007.pdf)

## Fonts

* SNFT (Spline font) Basis of opentype, truetype, postscript, graphite, and WOFF fonts
* Opentype - Open standard
* WOFF - SFNT font compressed to be more easily embedded.
* Graphite - Might allow faster rendering of non-western scripts.

## Graphics

Graphics formats can be divided into three categories - raster graphics, vector graphics and containers. Raster graphics are appropriate for the output of cameras and other imaging systems and data sets being presented in pseudocolor or greyscale. Vector graphics is appropriate for line drawings, graphs, icons, and similar illustrations. Containers are formats that allow different graphic formats to be transpoted in the same file type.

### Raster Graphics Formats

Within the category of raster graphics, formats are categorized by the type of compression used - uncompressed, lossless, and lossy. These formats can be compared based on file size relative to image size, limits the format enforces on image size and quality, Image quality at a given file size, availability of metadata, and openness of format. GIMP can be used to convert between formats.

Preferred formats:

* PNG for lossless compression 
* jpeg for lossy compression
* JITS or TIFF for uncompressed images (JITS allows for more metadata and larger numbers of bits per channels, TIFF is more widely used)
* GIF for small palette animations needing good maximum compression and protability

#### Lossy Compression

* JPEG - Bitmap images with lossy compression. Suffers degradation with each generation of editing. Can store metadata in EXIF format. (ISO/IEC 10918)
* JPEG 2000 - Update of JPEG standard. Not yet widely supported in open source although the GROK library is available. Format also allows for lossless compression. Unclear whether actual performance of compression matches claims. (ISO/IEC 15444)
* webp - from google, derivative of VP8 video format , can be lossy or lossless. Still an emerging format in 2019

#### Lossless Compression

* Portable Network Graphics (PNG) - Bitmap images with lossless compression and optional transparency. Supports palette based or direct mapped full color and grayscale images at 1 to 16 bit resolution. An open standard that uses the deflate compression algorithm. (ISO/IEC 15948 and IETF RFC 2083) Question PNG-8 vs PNG-24
* Animated PNG (APNG) - Animated PNG allows large palette animations.
* Graphic Interchange Format (GIF) - for small palette animations.
* FLIF - free lossless image format - high compression ratio, experimental
* webp - from google, derivative of VP8 video format , can be lossy or lossless. Still an emerging format in 2019

#### Uncompressed Format

* FITS - (Flexible Image Transport System) General Data format for arrays. Allows wide range of ascii metadata and wide range of bitdepths per channel. (FITS standard by IAU FITS working group)
* TIFF - Tagged Image Format Actually a container that can contain uncompressed or lossy or lossless compressed images. Can store metadata in exif format. (Adobe standard)
* ASDF - (Advanced Scientific Data Format) is a proposed replacement for FITS with a YAML metadata header followed by ASCII or binary data.

### Vector Graphics Formats

Preferred Format is SVG. Inkscape can be used to convert between formats.

* SVG - An open standard for vector graphics (W3G SVG standard)
* Gerber - (RS-274X) Used in Printed circuit board fabrication.
* PGF/TikZ - vector graphics language for use in LaTeX documents.

### Containers

TIFF, PDF and EPS are common container formats for graphics files. 

## Audio Video Container formats

<https://www.dr-lex.be/info-stuff/mediaformats.html>

* Ogg - <https://en.wikipedia.org/wiki/Ogg> container for FLAC, vorbis, opus, dirac and theora. no menus. Designed for streaming.
* MKV - Matroska <https://en.wikipedia.org/wiki/Matroska> seems to be able to hold anlmost any fomrat video and audio. Menus pending. MKV files tend to be bigger than MP4 and not playable on all devices, but offer more flexibility in codecs and higher resolution/
* MP4 - nearly universal
* webm - a specific profile of Matroska allowing VP8 video and Vorbis audio

For video, MKV is best container, but is still not widely supported (use VLC!). MP4 allows for wider range of devices.
## Audio

recomendations

i) Ogg vorbis for lossy compression
ii) Flac for lossless compression
iii) Wav linear pcm for uncompressed audio
iv) Opus for real time audio (VOIP)

### Uncompressed Pulse Code Modulation Formats 

* Linear PCM
* A Law PCM
* mu law PCM

#### not open???
* Wav (Waveform Audio Format) Windows' linear pcm for uncompressed audio
* AIFF (Audio Interchange File Format) Apple's PCM format

### Lossless Compression

* Flac for lossless compression
* ALAC apple's previously proprietary lossless audio format

### Lossy Compression

* vorbis for lossy compression
* Opus for real time audio (VOIP) (replaces vorbis)
* mp3 (mpeg audio layer III) - patents have expired

#### Not Open

* aac (advanced Ausio Coding)
*

## Video

* Theora - lossy compression
* Dirac - poorer performance than theora at low bitrates, but capable of lossless compression
* Daala - possible future replacmeent for both of the above
* MPEG-4 - compresses faster than H.264
* H.264 - Highest quality for a given size
* VP9 - Better than H.264 and open

Recommend webm format (matroska container with VP9 video and opus audio)

## Executables

### Architecture specific executable formats

* ELF - (Executable anmd Linkable Format) <https://en.wikipedia.org/wiki/Executable_and_Linkable_Format>
* PE and PE32+ (Portable Executable) <https://en.wikipedia.org/wiki/Portable_Executable> (windows .exe files)
* Mach-O - (Mach Object) used on systems based on mach kernel like mac's
* COFF (common object format file) basis for PE.

### Text formats for encoding executable code

* Motorola S-Record <https://en.wikipedia.org/wiki/SREC_(file_format)>
* Intel HEX <https://en.wikipedia.org/wiki/Intel_HEX>

### General ASCII text encoding of arbitrary binary data

* Base16 - uses 0-9 and A-F to encode hecadecimal digits (50% efficiency)
* Base64 - Uses upper and lower case letters, digits and the symbols + and / to get 64 characters. Three bytes can be encoded with 4 characters. (75% efficiency).
* Base85 - Encodes 4 binary bytes with 5 printable ascii characters. RFC 1924 uses upper and lower case lettters, digits and 23 additional printable characters to give 85 symbols (80% efficiency)

## Archive and compression formats

Formats that can be read on multiple platforms with open source software.

* 7z
* PAQ
* SQX
* zip - most commonly used on windows (includes jar files and ODF files)
* dmg - disk images

* tar.gz, tgz, tar.Z, tar.bz2, tbz2, tar.lzma, tlz, tar.xz, txz - tarball formats. (gzip, compress, bzip2, lzma, and xz respectively)
* tar

The 7zip program can read and write zip, gzip,bzip2,xz,tar, wim and can read apm,arj,chm,cpio,deb,flv,jar,lha,lzh,lzma,mslz,rar,rpm,smzip,swf,xar,a dn z archives and cramfs, dmg, fat, hfs, iso, mbr, ntfs, squashfs, udf, and vhd disk images.

<https://en.wikipedia.org/wiki/Comparison_of_archive_formats>
<https://en.wikipedia.org/wiki/List_of_archive_formats>

### Website and wiki archiving

* MAFF (mozilla archive format)
* ZIM - offline wiki storage <https://en.wikipedia.org/wiki/ZIM_(file_format)> also look at Kiwix an offline webpage reader.

## Other

* openpgp
*
<https://www.loc.gov/preservation/digital/formats/fdd/descriptions.shtml>
<https://en.wikibooks.org/wiki/FOSS_Open_Standards>
<https://en.wikipedia.org/wiki/List_of_open_formats#Various>
<https://en.wikibooks.org/wiki/Choosing_The_Right_File_Format/Quick_Guide>

File Formats
File Hierarchy Standard – not a standard file format but a standard way of organizing files into a directory tree
File systems – FAT, FAT16, FAT32, ext2, ext3, ext4, xfs, ntfs
Disk partitioning systems – GUID and MBR

Library of Congress recommended formats:
https://www.loc.gov/preservation/resources/rfs/RFS%202016-2017.pdf 

jats xml http://blogs.plos.org/tech/structured-documents-for-science-jats-xml-as-canonical-content-format/ 
xhtml



