
import matplotlib.pyplot as plt
import os
import numpy as np

def data_preparator():
	residues = ["A", "R", "N", "D", "C", "Q", "E", "G", "H", "I", "L", "K", "M", "F", "P", "S", "T", "W", "Y", "V"]
	residue_info = {}
	ss_list = ["H", "E", "-", "t"]
	t_s = [0, 0, 0, 0]
	for r in residues:
		residue_info[r] = {"H": 0, "E": 0, "-": 0, "t": 0}
	training_ids = open('/home/tommaso/Desktop/LB2_keys/keys/project/jpred4.list.txt')
	blind_ids = open('/home/tommaso/Desktop/LB2_keys/keys/project/SVM/IDs_blind.txt')
	for id in blind_ids:
		id = id.rstrip()
#		dssp_file = open('/home/tommaso/Desktop/LB2_keys/keys/project/dssp/'+id + ".dssp").read().splitlines()	#jpred
		dssp_file = open('/home/tommaso/Desktop/LB2_keys/keys/project/150Random_DSSPs_dssp/'+id + ".ss.dssp").read().splitlines()	#blind observed
#		dssp_file = open('/home/tommaso/Desktop/LB2_keys/keys/project/SVM/for_project/final_predicted_sequences/'+id + ".seqs").read().splitlines()	#blind SVM predicted
#		dssp_file = open('/home/tommaso/Desktop/LB2_keys/keys/project/GOR/gor_blind_predictions/SS-prediction_'+id + ".dssp").read().splitlines()       #blind GOR predicted
		ss_seq = dssp_file[1]
#		fasta_file = open('/home/tommaso/Desktop/LB2_keys/keys/project/fasta/'+id + ".fasta").read().splitlines()	#jpred
		fasta_file = open('/home/tommaso/Desktop/LB2_keys/keys/project/150Random_DSSPs_fasta/'+id + ".dssp.fasta").read().splitlines()	#residues do not change of course
		fasta_seq = fasta_file[1]
		for ss in range(len(ss_seq)):
			try:
				residue_info[fasta_seq[ss]][ss_seq[ss]] += 1
				residue_info[fasta_seq[ss]]["t"] += 1
				t_s[ss_list.index(ss_seq[ss])] += 1
				t_s[3] += 1
			except:
				residue_info["C"][ss_seq[ss]] += 1
				residue_info["C"]["t"] += 1
				t_s[ss_list.index(ss_seq[ss])] += 1
				t_s[3] += 1

	for key in residue_info.keys():
		for inkey in residue_info[key].keys():
				residue_info[key][inkey] = round((residue_info[key][inkey]/(t_s[ss_list.index(inkey)]))*100, 2)
	return(residue_info)

def histogram(residue_info):

	residues = ["A", "R", "N", "D", "C", "Q", "E", "G", "H", "I", "L", "K", "M", "F", "P", "S", "T", "W", "Y", "V"]
	ss_str=["Helix", "Strand", "Coil", "Overall"]
	data = [[0 for i in range(len(residues))] for j in range(4)]	#4 rows 20 columns
	for item in range(len(list(residue_info['A'].items()))):
		for key in range(len(list(residue_info.keys()))):
			data[item][key] = residue_info[list(residue_info.keys())[key]][list(residue_info['A'].items())[item][0]]

	colors=["blue", "orange", "green", "red"]
	number_groups = 4
	bin_width = 1.0 / (number_groups+1)
	fig, ax = plt.subplots(figsize=(6,6))
	for i in range(len(residues)):
		for j in range(4):
			ax.bar(x=np.arange(len(residues))+0.1+float(j+j)*(bin_width*0.5), height=data[j], width=bin_width, color=colors[j], align='center')

	ax.set_xticks(np.arange(len(residues)) + number_groups / (2 * (number_groups + 1)))
	plt.rcParams.update({'font.size': 22})
	ax.set_xticklabels(residues)
	ax.tick_params(axis='both', which='major', labelsize=22)
#	ax.legend(ss_str, facecolor='w')
#	ax.legend(ss_str, bbox_to_anchor=(1, 1), loc='upper left', borderaxespad=0.)

#	ax.set_title("Training Set")
#	ax.set_title("Blind-test Set (observed)")
#	ax.set_title("Blind-test Set (GOR-predicted)")
#	ax.set_title("Blind-test Set (SVM-predicted)")
	plt.xlabel("Residues", fontsize=22)
	plt.ylabel("Frequency %", fontsize=22)
	plt.show()

if __name__=="__main__":
	data = data_preparator()
	histogram(data)
