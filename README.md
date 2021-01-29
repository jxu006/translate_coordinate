# translate_coordinate
Translates transcript coordinates to genomic coordinates. 

Problem Statement
The objective is to write software that translates transcript coordinates to genomic coordinates. 

For example consider the simple transcript TR1, which aligns to the a genome as follows:

![alt tag](https://github.com/jxu006/translate_coordinate/issues/1#issue-796711654)

https://github.com/jxu006/translate_coordinate/issues/1#issue-796711654


We can compactly express this alignment in the same way that we compactly represent a read alignment in the S​AM/BAM format:​using a position and CIGAR string. In this case, the (0­based) position is CHR1:3, and the CIGAR string is ​8M7D6M2I2M11D7M.​For this exercise, you may assume that the transcript is always mapped from genomic 5’ to 3’.


The objective is then to translate a (0­based) transcript coordinate to a (0 based) genome coordinate. For examplethefifthbaseinTR1(i.e.TR1:4) mapstogenomecoordinateCHR1:7.Similarly,TR1:13mapsto CHR1:23 and TR1:14 maps to an insertion immediately before CHR1:24.
