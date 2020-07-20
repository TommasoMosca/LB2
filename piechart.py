import matplotlib.pyplot as plt
import os
import numpy as np

def data_preparator():
	helix = 0
	coil = 0
	strand = 0

	training_ids = open('/home/tommaso/Desktop/LB2_keys/keys/project/jpred4.list.txt')
	blind_ids = open('/home/tommaso/Desktop/LB2_keys/keys/project/SVM/IDs_blind.txt')
	for id in blind_ids:
		id=id.rstrip()
#		dssp_file = open('/home/tommaso/Desktop/LB2_keys/keys/project/dssp/'+id + ".dssp").read().splitlines()  #jpred
		dssp_file = open('/home/tommaso/Desktop/LB2_keys/keys/project/150Random_DSSPs_dssp/'+id + ".ss.dssp").read().splitlines()       #blind observed
#		dssp_file = open('/home/tommaso/Desktop/LB2_keys/keys/project/SVM/for_project/final_predicted_sequences/'+id + ".seqs").read().splitlines()     #blind SVM predicted
#		dssp_file = open('/home/tommaso/Desktop/LB2_keys/keys/project/GOR/gor_blind_predictions/SS-prediction_'+id + ".dssp").read().splitlines()       #blind GOR predicted
		ss_seq = dssp_file[1]
		for ss in ss_seq:
			if ss == "H":
				helix += 1
			elif ss == "E":
				strand += 1
			elif ss == "-":
				coil += 1
	perc_helix = helix/(helix+strand+coil)
	perc_strand = strand/(helix+strand+coil)
	perc_coil = coil/(helix+strand+coil)
	return(perc_helix, perc_strand, perc_coil)

def piechart(perc_helix, perc_strand, perc_coil):
	dist = [perc_helix*100, perc_strand*100, perc_coil*100]
	labeling = ["Helix "+str(round(perc_helix*100))+"%", "Strand "+str(round(perc_strand*100))+"%", "Coil "+str(round(perc_coil*100))+"%"]
	fig, ax = plt.subplots(subplot_kw=dict(aspect="equal"))
	wedges, texts = ax.pie(dist, wedgeprops=dict(width=0.3), startangle=45)
	kw = dict(arrowprops=dict(arrowstyle="-"), zorder=0, va="center", size="xx-large")

	for i, p in enumerate(wedges):
		ang = (p.theta2 - p.theta1) / 2. + p.theta1
		y = np.sin(np.deg2rad(ang))
		x = np.cos(np.deg2rad(ang))
		horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
		connectionstyle = "angle,angleA=0,angleB={}".format(ang)
		kw["arrowprops"].update({"connectionstyle": connectionstyle})
		ax.annotate(labeling[i], xy=(x, y), xytext=(1.2 * np.sign(x), 1 * y),
					horizontalalignment=horizontalalignment, **kw)


	plt.rcParams.update({'font.size': 22})
#	ax.set_title("Training Set SS")
#	ax.set_title("Blind-test Set SS (observed)")
#	ax.set_title("Blind-test Set SS (GOR-predicted)")
#	ax.set_title("Blind-test Set SS (SWM-predicted)")

	plt.show()



if __name__=="__main__":

	h, s, c = data_preparator()
#	print(h, s, c)
	piechart(h, s, c)
