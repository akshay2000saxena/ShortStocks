def chooser (mla, inp):
	finalres = []
	if (len(mla) <= len(inp)):
		for i in range(len(mla)):
			if (mla[i]==1):
				finalres.append(inp[i])
	if (len(mla) > len(inp)):
		for i in range(len(inp)):
			if (mla[i]==1):
				finalres.append(inp[i])
	return finalres
