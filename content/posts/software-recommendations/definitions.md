---
title: "Definitions For Software Tools"
date: 2021-01-02
author: Jeffrey A. Jalkio
---
In understanding computer hardware and software it is important to differentiate between a number of closely related concepts. This document is an attempt to clarify these concepts.

API (Application Programming Interface)
: A protocol for providing access to a service or resource. API's are typically specified in a document and implemented in software. In some cases the specification is developed and maintained by a standards group as an open standard.

Open Source License
: One of several licenses designed to provide clear legal access to intellectual property. Several different licences exist to allow for differences between different types of intellectual property (e.g. artwork, works of fiction, documentation, software libraries, fonts, and executables), granting different rights (e.g. to use, redistribute, modify, sell, etc.), and imposing different requirements on users (e.g. requirement to keep license on derivitive works, etc.) A description of many of these standards and when they might be used can be found in <licenses>

Kernel and User Space
: To allow protection of processes from one another, operating systems prohibit processes fromperforming operations that would harm other processes. However, processes must be able to communicate with one another and to access shared resources. To allow this, operating systems (and the underlying hardware (or simulation)) provide a separation between user and kernel operating modes. User mode processes cannot access kernel memory or shared hardware resources. They can request services via operating system calls (also known as service calls, traps, and software interrupts). It is generally desireable to minimize the amount of code running in kernel space to reduce the probability of catestrophic programming errors. Therefore, only the most critical code is placed in kernel space software while the rest runs in user space.

Communication protocol
: To simplify access to resources, common communication protocols may be used for accessing multiple resources. In the case of hardware, these protocols include internal and external busses like PCI, PCIe, SATA, USB, ethernet, etc. In the case of software, these include standards for operating systems calls, interprocess communication standards, SSH, HTTPS, etc. While the use of these protocols can be specified via an api, other APIs can be built upon them. For example  

Software Stack
: As one API builds upon another, software implementing those APIs build upon one another to form a stack of software. For example, network interface hardware device drivers, routing protocol software, and HTTPS protocols form a stack on top of which other software such as file or web servers can operate. Similarly, graphics device drivers, display manager software, window managers, and desktop environments form a graphics stack for GUI applications.

