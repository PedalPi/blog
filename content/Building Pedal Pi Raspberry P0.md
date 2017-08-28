Title: Building Pedal Pi - Raspberry P0
Date: 08/31/2017
Category: About
Tags: DIY, Pedal Pi
Authors: SrMouraSilva
--cover: images/components.png

The brazilian article ["Pedal Pi - DIY audio plugin multiprocessor"](https://github.com/PedalPi/Documentacao/raw/master/ERIPI/Pedal%20Pi%20-%20Multi-processador%20de%20plugins%20de%20%C3%A1udio%20DIY.pdf) (pt-BR) introduces the project for the cientific comunity. In hin, informations about the specification choises and software achitecture are presented.

The cientific article isn't a guide for to mount a Pedal Pi machine. This article is for this. We will be configure a **Pedal Pi** version with _Raspberry P0_ and _Webservice_ components. With them, it's possible controls the _current pedalboard_ and manages pedalboards, effects and their parameters.

The content presented here has divided in three parts, _i)_ project presentation, _ii)_ your hardware and software installation and _iii)_ the physical installation.

## 1. Project presentation

Motivation

The Pedal Pi executes into a device that executes an Linux Operational System.
Since this equipment is to be used in _out the house_, is a cool idea uses something transportable,
like a _notebook_ or an embedded system. We choise in here the second option.
The following steps shows the material list and the installation.

[Project image]

Paragraph with the components explanation.

## 2. Embedded System configuration

### 2.1 Materials list

For to mount the Pedal Pi based in this article, it's necessary the following materials:

![Pedal Pi components: Raspberry Pi, charger, SD Card and USB Audio interface]({filename}/images/components.png)

1. [Raspberry Pi](https://www.raspberrypi.org/products/) (preferably version 2 or version 3);
1. USB Audio interface;
1. [USB Changer](https://www.raspberrypi.org/products/raspberry-pi-universal-power-supply/) more than 1.5A;
1. MicroSD card with 4 Gigabytes or more.

The USB Audio interface used in this tutorial is a generic called [3D Sound](https://www.aliexpress.com/wholesale?catId=0&initiative_id=SB_20170809041325&SearchText=3D+USB+Sound+Card+5.1). This choise is for demonstrative purposes, based in your low cost (between $0.85 and $6.00)

Others embedded systems can be used (as an [Orange Pi](http://www.orangepi.org/) or a [Banana Pi](http://www.banana-pi.org/)), but for now, the library used for physical controller components are only implemented for Raspberry Pi. 😕

### 2.2 Software installation

First time, is necessary install the Operational System (OS) in the MicroSD card.
For install the [Raspbian](https://www.raspberrypi.org/downloads/raspbian/), the OS
that we use in Pedal Pi, you can view the
[Installing Operating System Images](https://www.raspberrypi.org/documentation/installation/installing-images/)
Raspberry's tutorial.

With the Operation System installed, now it's time to install the Pedal Pi softwares.
We prepared the a script for install the softwares. [Access the terminal](https://www.raspberrypi.org/documentation/usage/terminal/) and execute:

```bash
wget https://raw.githubusercontent.com/PedalPi/scripts/master/RaspberryP0%2Bwebservice.sh
sh RaspberryP0+webservice.sh
```

Others scripts will be added in [Pedal Pi Scripts repo](https://github.com/PedalPi/scripts).

## 3. Physical component installation

### 3.1 Physical materials list

For physical controls the current pedalboard, it's necessary install.

* [image] 2 seven segments display;
* [image] Footswitches buttons;
* [image] Box.

![Physical schematic](https://raw.githubusercontent.com/PedalPi/Raspberry-P0/master/docs/schematic.jpg)

### 3.2 Mounting

## 4. Considerations

* Application for management

## 5. Acknowledgment

Thanks for the open community by the free images used in this blog post!

* [Micro sd.svg](https://commons.wikimedia.org/wiki/File:Micro_sd.svg)
* [Raspberry Pi B+ illustration.svg](https://commons.wikimedia.org/wiki/File:Raspberry_Pi_B%2B_illustration.svg)
* [Vector Phone Charger](http://freevectorfinder.com/free-vectors/phone-charger-vector/)

## References

* [Pedal Pi - Raspberry P0 repository](https://github.com/PedalPi/Raspberry-P0);
* [Pedal Pi Scripts repository](https://github.com/PedalPi/scripts);
* Silva, P. M. M.; Costa, L. S; Jucá; Sandro ????; [Pedal Pi - Muli-processador de plugins de áudio DIY](https://github.com/PedalPi/Documentacao/raw/master/ERIPI/Pedal%20Pi%20-%20Multi-processador%20de%20plugins%20de%20%C3%A1udio%20DIY.pdf)
