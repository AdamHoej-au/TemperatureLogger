---
layout: post
title: "Projektes formål"
---

# Hvad skal måles
Der skal måles i 3 akvariumer, hvor temperaturen er indstillet til 3 forskellige indstillinger.

# Hvorfor skal det måles?
For at sikre at temperaturen i akvariet ikke afviger fra en række givne parametre.

# Hvordan skal det måles?
Hver måling bliver lavet med en DS18B20 og vil blive logget på en Raspberry Pi Zero, hvorpå der vil køre en række Python scripts til udførsel af databehandling direkte på enheden. Denne data kan let tilgåes vha. en FTP server.