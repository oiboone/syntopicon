---
title: "Data Communication Standards"
date: 2019-11-15
author: Jeffrey A. Jalkio
---

# Physical Layer

## Connector Standards

### Power Connectors (AC)

NEMA 1-15P and 5-15P - North American AC Power connectors, polarized, 2 and 3 pin respectively

IEC 60320 (commonly called 320) Cord to chassis standard connections C13/C14 male or female (commonly used on PC power supplies), C7 - polarized or non-polarized 2 pin (commonly found on external power supplies), C5 - 3 pin (mickey mouse shaped connector)

CEE 7 - European power connector standards

### Power Connectors (DC)

Molex - widely used inside computers

IEC 60130-10 coaxial dc power connectors

EIAJ - dc power, different diameters for different voltages, 2A max

### Data Connectors

DIN 41-612 Used in 19 inch rack mount systems for connecting plug in daughterboards to backplane. Examples include VME and VXI buses.

D-subminiature several sizes and several pin densities.

USB-C connector

## Medium Standards

unsheilded twisted pair
coaxial
ribbon

## Signalling Standards

1) CML Current Mode Logic is a differential logic family capable of speeds from 312.5 Mbps to 3.125 Gbps with 50 Ohm termination

2) Low Voltage Differential Signaling - TIA/EIA-644 655Mbps-3 Gbps uses 2.5V swing with a 1.2V common mode voltage between wires.

3) standard digital voltage levels 5VTTL, 3.3VCMOS, etc.

# Logical Link Layer

1) TMDS Transition minimized differential signaling - Used by DVI and HDMI video interfaces. 8b/10b encoding with minimal transitions and DC balance. Uses twisted pair current mode logic terminated to 3.3V for physical layer.


# Video standards

1) CGA
2) VGA
3) DVI
4) HDMI
5) DisplayPort

# Mobile phone standards

1) DECT - Digital European Cordless Telecommunications - also used for baby monitors.
2) PHS - Personal Handy phone - Japan China, Asia cordless telephone but with handoff from tower to tower.
3) GSM - global system for mobile communications

# Serial communication standards

1) RS-232 - single ended signaling, 7or 8 bit frames, start bit, stop bit, optional parity, synchronization via start bit.
2) RS-422 - differential signaling
3) RS-485 - RS-422 levels with multiple nodes.
4) CAN (controller area network) - differential signaling with dominant, high voltage (1.5-3V) 0 and recessive (12 to -120 mv) 1. Arbitration field at start of message frame - first dominant bit wins arbitration. variable length frames with ack field.
5) USB
6) USB-4 aka Thunderbolt-3 - provides USB 3, 4 lanes of PCI-e, and 8 lanes of DisplayPort 1.2 and up to 100W of power.

# On-chip and inter-chip bus standards

1. AMBA APB - advanced peripheral bus
2. AMBA AXI - high speed interconnect from ARM
3. Wishbone
4. TileLink
5. SPI
6. I2C


# Bus standards

1) S-100 based on the 8080 bus signals American National Standard IEEE Std 696-1983 16 bit data, 24 bit address bus.
2) ISA bus - Original PC bus. 8086 bus signals
2) VME bus -  ANSI/IEEE 1014-1987 based on Motorola 68000 bus signals. Uses Eurocard card sizes ((DIN 41612) but defines bus signals which eurocard does not. (data rate up to 420 MiB/s) Inherently a multi-master bus where all transfers are DMA.
2) VXI - VME extensions for instrumentation.
2) CompactPCI - eurocard connectors with PCI signalling
2) PXI - Compact PCI with additional signaling for instrumentation (PCI extensions for Instrumentation)

This webpage has data rate numbers: https://www.microway.com/knowledge-center-articles/performance-characteristics-of-common-transports-buses/ 

1) PCI - parallel multi-master, processor architecture independent bus for peripherals.Transaction based. Separate configuration address space.
2) PCI Express - point to point serial lanes (1 to 16 lanes per channel) that allows hot plugging, autonegotiation of data rates and lane width. 250 MB/s per lane in each direction. Ideal for host to peripheral communications. Does not scale well due to need for root complex.
3) HyperTransport - Open specification Standardized high speed point to point communication protocol intended to replace proprietary front side busses. Used as the processor bus for AMD. 200 MHz to 3.2 GHz clock with double data rate frequency autonegotiated. Bit width from 2 - 32 bits per link two unidirectional links per bus. physical link similar to LVDS. Packet based. At max clock speed and 32 bit width, throughput is 25.6 GBps in each direction.
4) Infinity Fabric - superset of hypertransport announced by AMD in 2016 for 30-512 GByte/second rates
5) Intel QuickPath Interconnect - Intel's alternative to Hypertransport. Each QPI has 2 20 lane point to point links.
6) Intel UltraPath Interconnect - update of quickpath to allow 10.4 GT/s 
6) Intel Direct Media Interface (DMI) - slower than Quickpath, intended to connect highly integrated CPUs to I/O hub.
6) Infiniband - high throughput, low latency network designed for high performance computing networks. A scalable switched fabric network topology. copper to 10 m and fiber to 10 km 
6) Omni-Path - 100 Gbps proprietary alternative to Infiniband from Intel
6) RapidIO - Intended for low latency, peer-to-peer communication in fault tolerant embedded applications of less than one kilometer.
7) Fibre Channel - intended for storage area netowrks 1- 128 Gbps. 1 to 4 fiber links per channel. Topology can be point to point, arbitrated loop (like token ring), or switched fabric (like modern ethernet). Typically uses SFP (small form factor pluggable transceivers) links up to 2km at full speed , 50 km at 2 Gbps. Can be used to transport SCSI, IP, FICON, PCIe, or NVMe protocols

# Network standards

1) Ethernet - robust protocol intended for changing network topology and large link latency.
2) token ring - deterministic access times. guaranteed access
