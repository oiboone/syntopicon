---
title: The Linux Graphics Stack
date: 2021-01-02
author: Jeffrey A. Jalkio
---

## Consider reorganizing information

## API's

GL and GLES do the actual rendering, but need a context, provided by EGL, CGL, WGL, or GLX

GLUT - independent interface

EGL - API for creating OpenGL contexts and connecting them to rendering surfaces

earlier interfaces for specific windowing environments (still in use):

CGL apple interface
WGL - windows interface
GLX - X window interface

## Drivers and OS Level
Kernel Space Drivers - (vendor specific, talk to GPU (radeon, nouveau, i915, nvidia)

DRI (Direct Rendering Infrastructure) - framework for allowing user programs direct access to graphics hardware dri.sourceforge.net/doc/DRIintro.html

DRM (Direct rendering manager) kernel module that allows DRI. It handles memory management, DMA, and security issues. 


User Space Drivers communicate via DRI/DRM with kernel mode drivers to implement the OpenGL specificaiton and expose it as an OpenGL library (libGL)

Mesa is an open source collection of user space drivers (different Mesa drivers for each kernel space driver.

Gallium - interfaces and supporting libraries to ease development of graphics card device drivers and provide common code for mesa drivers

GEM (Graphics execution manager) - ??

KMS (Kernel Mode Setting) ???

## Display Server
Wayland - compositor and communication protocol for clients. Differentiate between wayland protocol and wayland server
X Window System - old centralized graphics server that provided network transparency (X client can be on one machine and X server on another connected via network). (XWayland is an x server running as a wayland client)(differentiate between protocol and server)

## Graphics Libraries
Cairo - 2-d graphics library that can support multiple backends (surfaces) including xlib and xcb for X windows, Quartz for macOS, win32, image buffers, postscript, PDF,and SVG file output. As of 2017 backends for openGL, BeOS, OS/2 and DirectFB were under development.
OpenGL - API for vector graphics primatives on GPUs
Mesa 3D - open source implementation of openGL, Vulkan and other 3d graphics protocols
GLAMOR - implements 2D drawing in OpenGL
Glitz -openGL compositing library
VA-API provide functionality to encode/decode video streams through the GPU
VDPAU and XVDA are specific to NVidea and ATI respectively. 

## font stack
Freetype – font rasterization. font glyph rendering into bitmaps supporting wide range of operating systems and font formats. Supports hinting
Fontconfig – performs font selection based on a pattern of desired characteristics.
FreeBidi – provides bidirectional script support.
Harffbuzz – layout engine - glyph selection from font taking into account substitutions, compositions, etc.
pango - text layout taking into account localization issues

## Application frameworks
GTK+ - gnome
QT - KDE
wxWidgets - cross platform. Uses other "native" toolkits for implementation on different platforms. Aims to look native on each platform
tk - GUI for tcl

## Browser Layout engines
Gecko - mozilla
Webkit – from kde’s KHTML
Blink – a fork of webkit used by opera and chromium

## Window Managers - provide window frame and decorations for applications.

Openbox - small, highly configurable window manager that supports key standards
kwin - large, compositing window manager that is now also a wayland compositor
xfwm4 - window manager for xfce
icewm - nice user interface with taskbar <https://ice-wm.org/>
enlightenment - <https://www.enlightenment.org/about>
awesomewm - tiling wm extensible and configurable in lua

## Desktop Environments - Build upon window managers by adding application launchers, panels, desktop widgets, etc.

Gnome
KDE - uses kwin window manager by default. Highly configurable
Mate
Cinnamon
Lxqt – lightweight distribution based on lxdt and qt toolkit Can run on top of openbox or another window manager
xfce - fast, lightweight, and standards complient while still visually appealing and easy to use. Started as Linux version of CDE 

## references
http://longwei.github.io/Linux-Graphic-And-Wayland/ 
http://blog.mecheye.net/2012/06/the-linux-graphics-stack/#rendering-stack

http://behdad.org/text/ - 2012 state of the font stack


https://eev.ee/blog/2015/05/20/i-stared-into-the-fontconfig-and-the-fontconfig-stared-back-at-me/ - adventures with adjusting fontconfig file
look at fonts tweak tool https://github.com/jamesni/fonts-tweak-tool and
Gucharmap https://wiki.gnome.org/action/show/Apps/Gucharmap?action=show&redirect=Gucharmap 
Infinality installs a set of fontconfig rules – that may be good or bad