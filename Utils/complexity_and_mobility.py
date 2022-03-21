import numpy as np 

#input signal as 1 dimensional list of values
def mobility(signal):
	n = len(signal)
	dSignal = np.diff([0] + signal)
	ddSignal = np.diff([0] + dSignal)
	mx2 = np.mean(square(signal))
	mdx2 = np.mean(square(dSignal))
	mddx2 = np.mean(square(ddSignal))
	mob = mdx2 / mx2
	mobility = np.sqrt(mob)
	return mobility

#input signal as 1 dimensional list of values
def complexity(signal):
	n = len(signal)
	dSignal = np.diff([0] + signal)
	ddSignal = np.diff([0] + dSignal)
	mx2 = np.mean(square(signal))
	mdx2 = np.mean(square(dSignal))
	mddx2 = np.mean(square(ddSignal))
	mob = mdx2 / mx2
	complexity = np.sqrt((mddx2 / mdx2) - mob)
	return complexity

def square(list):
    return [i ** 2 for i in list]