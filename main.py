import numpy as np
import sklearn
import umap


def dmdtim(mjd,mag,ldmints,ldtints):
	# ldmints is the LENGTH of
	# dmints
	# ldtints is the LENGTH of
	# dtints
	"""Push each dmdt point to
	its appropriate bin
	The function could be made faster using some tricks.
	Also, the normalization needs to be thought of better.
	Right now we divide by number of points in the pairs.
	One obvious change to do is to divide by points in lc instead,
	or even log of points or some such since twice the points
	are not two times better,
	especially for bif differences.
	The main question here is if two objects of the same class,
	one with a richer structure
	and another with a sparser set, pull algorithms apart.
	"""
	dmdt=np.zeros(shape=(ldmints,ldtints))
	maxval = 255
	maxpts = len(mjd)*(len(mjd)-1)/2
	dmjd = []
	dmag = []
	# generate differences (w.r.t.
	#time and mags)
	for i in range(len(mjd)):
		for j in range(i+1,len(mjd)):
			dmjd.append(mjd[j]-mjd[i])
			dmag.append(mag[j]-mag[i])
	# sort w.r.t. to first component
	# (dmjd)
	(sdmjd,sdmag) = zip(*sorted(zip(dmjd,dmag)))
	# sdmjd
	#(0.00096199999825330451, 0.00096299999859184027,
	# 0.00097200000163866207, 0.0019249999968451448, 0.0019350000002305023, 0.0021459999989019707, 0.0021469999992405064, 0.002148999999917578, 0.0025590000004740432, 0.0025789999999688007)
	# sdmag
	#(-0.034694000000000003, 0.0077630000000006305,
	# -0.023438000000000514, -0.026930999999999372, -0.015674999999999883, -0.012509999999998911, -0.019592000000001164, 0.02876299999999965, 0.03605400000000003, 0.039031999999998845) 
	minmjdbin = 0
	for i in range(len(sdmjd)):
		mjdbin = minmjdbin
		for k in range(minmjdbin,ldtints):
			if sdmjd[i] > dtints[k]:
				mjdbin = k
				minmjdbin = mjdbin
				magbin = 0
		for k in range(ldmints):
			if sdmag[i] > dmints[k]:
				magbin = k
				dmdt[magbin,mjdbin] += 1
	
	return (maxval*dmdt/maxpts)

raw_data = np.load("KeplerSampleFullQ.npy")

hehe = []

for i, _ in enumerate(raw_data):
     for j, _ in enumerate(raw_data[i]):
     	if (len(raw_data[i][j]) == 3534):
     		hehe.append(raw_data[i][j])

hehe = np.array(hehe)

umap.UMAP().fit_transform(hehe)