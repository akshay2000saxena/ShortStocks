import keywordreturn

def classifier (lst):
	keywords = keywordreturn.keywordreturn()
	management = keywords[0]
	legal = keywords[1]
	financial = keywords[2]
	humanresc = keywords[3]
	innovation = keywords[4]
	management_ctr = 0
	legal_ctr = 0
	financial_ctr = 0
	humanresc_ctr = 0
	innovation_ctr = 0
	for word in lst:
		for key in management:
			if (key==word):
				management_ctr = management_ctr + 1
		for key in legal:
			if (key==word):
				legal_ctr = legal_ctr + 1
		for key in financial:
			if (key==word):
				financial_ctr = financial_ctr + 1
		for key in humanresc:
			if (key==word):
				humanresc_ctr = humanresc_ctr + 1
		for key in innovation:
			if (key==word):
				innovation_ctr = innovation_ctr + 1
	tags = []
	if (len(tags)==0):
		classdict = {2: management_ctr, 3: legal_ctr, 4: financial_ctr, 5:humanresc_ctr, 6: innovation_ctr}
		tags.append([max(classdict, key=classdict.get), 1])
	return tags[0]

