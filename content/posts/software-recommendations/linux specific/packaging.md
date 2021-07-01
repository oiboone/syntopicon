---
#
#
#
title: The Debian Packaging System
author: Jeffrey A. Jalkio
date: 2020-05-15
#bibliography: [packaging.bib]
#csl: ieee.csl
---

## Archive File Formats

### ar - unix archive file

A concatenation of files with minimal metadata. Currently used primarily for static libraries. <https://en.wikipedia.org/wiki/Ar_(Unix)>

### tar - tape archive format

Originally designed for making tape archives of directory trees. Lot's more metadata for each file including file type, permissions, and path name. Often stored and distributed in compressed formats. e.g. foo.tar is compressed to form foo.tar.gz or foo.tgz. <https://en.wikipedia.org/wiki/Tar_(computing)>

### deb - debian package format

An archive (ar file) containing two tar files. One containing the files to install and the other containing the control information on how to install them.

## dpkg

Program for installing .deb files

## apt

Suite of programs for downloading .deb files from repostiories and installing them. Front end for dpkg
<https://itsfoss.com/apt-command-guide/>

### subcommands

apt-cache policy - lists all repos being checked
apt-cache show [package-name]

apt-key list
: shows trusted gpg signing keys


## Repositories and security

Repositories have a collection of deb files along with information about their versions and dependencies. Signatures can be used to validate this information.
<https://wiki.debian.org/SecureApt>, <https://blog.packagecloud.io/eng/2014/10/28/howto-gpg-sign-verify-deb-packages-apt-repositories/>

aptly
: tool for mirroring repositories, taking snapshots, etc. <https://www.aptly.info/>


<https://linuxconfig.org/easy-way-to-create-a-debian-package-and-local-package-repository>

<https://medium.com/sqooba/create-your-own-custom-and-authenticated-apt-repository-1e4a4cf0b864>
