#!/usr/bin/env python 

import sys
import argparse

"""
Translate transcript coordinate to genome coordinate. 

The function translate_coordinate uses a transcript-genome mapping file to generate a transcript_coordinate:genome_coordinate dictionary. 

Example: 
	python translate_coordinate.py -m mapping_file.txt -q query_file.txt -o outfile.txt 
"""

def check_input_file(filename,k):
    """
    Check if the input file is in the correct format.   
    """
    i = open(filename)
    for line in i:
        number_column = len(line.rstrip().split("\t"))
        if number_column != k:
            print("Input file is not in valid format. The mapping file should be 4 columns tab-delimited file. The query file should be 2 columns tab-delimited file.")
            sys.exit(-1)

def translate_coordinate(mapping_file):
    """
    Generate a transcript_coordinate:genome_coordinate dictionary from a mapping file.
 
    The mapping file should be 4 columns tab-delimited file. The 1st column is the transcript name, and the remaining 3 columns indiciate the genomic mapping: chromome name, 0-based starting position on the chromosome, and CIGAR string indicating the mapping.  
    """
    mapping_dict = {}
    f = open(mapping_file)
    for line in f:
        gene_id = line.rstrip().split("\t")[0]
        chromosome = line.rstrip().split("\t")[1]
        genome_coordinate = int(line.rstrip().split("\t")[2])
        cigar_string = line.rstrip().split("\t")[3]
        transcript_coordinate = 0
        mapping_dict[gene_id] = (chromosome, {})
        for item in cigar_string.split("M")[:-1]:
            if "D" in item:
                deletion_length = int(item.split("D")[0])
                match_length = int(item.split("D")[1])
                genome_coordinate += deletion_length
                for i in range(match_length):
                    mapping_dict[gene_id][1][transcript_coordinate+i] = genome_coordinate+i
                transcript_coordinate += match_length
                genome_coordinate += match_length
            elif "I" in item:
                insertion_length=int(item.split("I")[0])
                match_length = int(item.split("I")[1])
                for i in range(insertion_length):
                    mapping_dict[gene_id][1][transcript_coordinate+i] = "Insertion before " +str(genome_coordinate)
                transcript_coordinate += insertion_length
                for i in range(match_length):
                    mapping_dict[gene_id][1][transcript_coordinate+i] = genome_coordinate+i
                transcript_coordinate += match_length
                genome_coordinate += match_length
            else:
                match_length = int(item)
                for i in range(match_length):
                    mapping_dict[gene_id][1][transcript_coordinate+i] = genome_coordinate+i
                transcript_coordinate += match_length
                genome_coordinate += match_length
    f.close()   
    return mapping_dict

def main():
    check_input_file(args.mapping_file, 4)
    check_input_file(args.query_file, 2)
    mapping_dict = translate_coordinate(args.mapping_file)
    q = open(args.query_file)
    o = open(args.outfile, "w")
    for line in q:
        gene_id = line.rstrip().split("\t")[0]
        query_coordinate = line.rstrip().split("\t")[1]
        o.write(gene_id+"\t"+query_coordinate+"\t"+mapping_dict[gene_id][0]+"\t"+str(mapping_dict[gene_id][1][int(query_coordinate)])+"\n")
    q.close()

if __name__=="__main__":
    parser = argparse.ArgumentParser(description="Translate transcript coordinates to genomic coordinates. ")
    parser.add_argument('-m', dest='mapping_file', required=True, type=str, help='The mapping file shows the alignment between transcript and genome.')
    parser.add_argument('-q', dest='query_file', required=True, type=str, help='The query file')
    parser.add_argument('-o', dest='outfile', required=True, type=str, help='Output file')
    if len(sys.argv) == 1:
        sys.argv.append('-h')
    args = parser.parse_args()
    main()


