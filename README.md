# translate_coordinate
Translates transcript coordinates to genomic coordinates. 

The objective of this software is to translates transcript coordinates to genomic coordinates. 

For example consider the simple transcript TR1, which aligns to the a genome as follows:

![Screen Shot 2021-01-29 at 1 09 36 AM](https://user-images.githubusercontent.com/11094958/106255510-f6ff0f00-61ce-11eb-9f65-629d4d441635.png)

We can compactly express this alignment in the same way that we compactly represent a read alignment in the SAM/BAM format using a position and CIGAR string. In this case, the (0-based) position is CHR1:3, and the CIGAR string is 8M7D6M2I2M11D7M. 

The objective is then to translate a (0-based) transcript coordinate to a (0-based) genome coordinate. For example, the fifth base in TR1 (i.e.TR1:4) maps to genome coordinate CHR1:7. Similarly,TR1:13 maps to CHR1:23 and TR1:14 maps to an insertion immediately before CHR1:24.

