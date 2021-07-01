---
title: "Running a Program"
date: 2021-01-02
author: Jeffrey A. Jalkio
---
## how the linux kernel executes a program:

See this excellent article: <https://lwn.net/Articles/630727/>

Kernel first sets everythign up (lot's of details here)
Checks type of program by looking at first 2 characters (!# indicates script <https://www.in-ulm.de/~mascheck/various/shebang/>) Other codes for a.out and elf formats.

ELF files are executed as described here <https://lwn.net/Articles/631631/>

## system calls

article <https://lwn.net/Articles/604287/>
