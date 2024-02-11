#!/bin/python3


import argparse
import csv
import os.path as pathlib
import pprint
import json


parser = argparse.ArgumentParser(
	prog='ProgramName',
	description='What the program does',
	epilog='Text at the bottom of help')


parser.add_argument("--i", metavar="FILE", required=True)
parser.add_argument("--o", metavar="FILE")
parser.add_argument("--species", default=False, action="store_true", help="Input file is a BirdNet species list")
parser.add_argument("--duration", metavar="Seconds", default=0)
parser.add_argument("--operator", metavar="Name", default="None")
parser.add_argument("--reviwer", metavar="Name", default="None")

args = parser.parse_args()

if not pathlib.isfile(args.i):
	print("File",args.i, "does not exist.")
	exit()

if args.species:
	# Split by "_" and only write back the last half
	new_species = []
	with open(args.i,"r") as species_file:
		for line in species_file.readlines():
			new_species.append(line.split("_")[1].strip("\n").split(" "))

	spec = sorted(new_species, key=lambda specs: specs[-1])
	spec_merged = [" ".join(x) for x in spec]

	with open(args.i.replace(".txt","_avianz.txt"), "w") as outfile:
		outfile.write(json.dumps(spec_merged))

else:

	avianz_file = [{"Operator":args.operator, "Reviewer":args.reviwer, "Duration":args.duration}]

	# The native BirdNet format is tab-separated CSV like
	with open(args.i,"r") as birds_file:
		tsv_reader = csv.DictReader(birds_file, delimiter="\t")
		for bird in tsv_reader:

			new_entry = []
			new_entry.append(float(bird["Begin Time (s)"]))
			new_entry.append(float(bird["End Time (s)"]))
			new_entry.append(float(bird["Low Freq (Hz)"]))
			new_entry.append(float(bird["High Freq (Hz)"]))
			new_entry.append([{"species": bird["Common Name"], "certainty": float(bird["Confidence"])*100, "filter": "M"}])
			avianz_file.append(new_entry)

	#pprint.pprint(avianz_file)
	json_string = json.dumps(avianz_file)
	if args.o == None:
		out_name = args.i.replace(".BirdNET.selection.table.txt",".wav.data")
	else:
		out_name = args.o

	with open(out_name, "w") as outfile:
		outfile.write(json_string)
