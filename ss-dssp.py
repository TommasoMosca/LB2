import sys
import os

def ss_dssp(cc):
	x = cc.read().splitlines()
	for e in os.listdir("/home/tommaso/Desktop/LB2_keys/keys/project/150Random_DSSPs_files"):
		for j in x:
			ID = j.split('_')			#ID stands for the IDs list, id stands for DIR IDs
			ids = e.split('.')
			if ids[0] == ID[0]:
				open("/home/tommaso/Desktop/LB2_keys/keys/project/150Random_DSSPs_files/"+ids[0]+".pdb.dssp", "r")
				dd = open("/home/tommaso/Desktop/LB2_keys/keys/project/150Random_DSSPs_files/"+ids[0]+".pdb.dssp", "r")
#				print(id[0])
#				print(dd.readlines())
#				open(j+".txt", "w+")			#per avere solo la sequenza per mandare psiblast
#				out = open(j+".txt", "w+")		#per avere solo la sequenza per mandare psiblast
				open(j+".seqs.dssp", "w+")
				out = open(j+".seqs.dssp", "w+")
				ss = ''
				flag = 0
				helix=['H', 'I', 'G']
				beta=['E', 'B']
				coil=['S', 'T',' ']
				rr= ''
				for i in dd:
					if '#' in i:
						flag=1
						continue
					elif flag == 0: continue
					elif flag == 1:
#						print(i[11])
						if i[11] == ID[1]:
							if i[16] in helix:
								ss += 'H'
								rr += i[13]
							elif i[16] in beta:
								ss += 'E'
								rr += i[13]
							elif i[16] in coil:
								ss += '-'
								rr += i[13]
#				print(ss)
#				print(str_len)
#				out.write('>'+j+'\n'+rr+'\n')				#per avere solo la sequenza per mandare psiblast
				out.write('>'+j+'\n'+ss+'\n')				#per avere solo la sequenza per mandare performance 
#				out.write('>'+j+'\n'+ss+'\n'+rr+'\n'+str(len(ss))+'\n')
				out.close()

if __name__ == '__main__':
	with open(sys.argv[1]) as filein:
		print(ss_dssp(filein))

