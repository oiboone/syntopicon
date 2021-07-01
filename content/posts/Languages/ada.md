---
title: "The Ada Programming Language"
date: 2021-01-02
author: Jeffrey A. Jalkio
---
# Concepts

## Type system

- built in type hierarchy
- user type defrinitions: type color is (red, blue, green);
- derived types: new, incompatible version of existing type: type voltage is new float;
- compatible subtype: subtype low_voltage is voltage range -1.0..1.0
- tagged types: cntain tags that indicate derived type at runtime. Methods can dispatch to version for that derived type.
- 
##
- attributes:  name'attribute
- aspects: 