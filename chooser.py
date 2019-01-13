def chooser (mla, inp):
	finalres = []
	for i in range(0, len(mla)):
		if (mla[i]==1):
			finalres.append(inp[i])
	return finalres
