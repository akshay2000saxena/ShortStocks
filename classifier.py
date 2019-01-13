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
				management_ctr++
		for key in legal:
			if (key==word):
				legal_ctr++
		for key in financial:
			if (key==word):
				financial_ctr++
		for key in humanresc:
			if (key==word):
				humanresc_ctr++
		for key in innovation:
			if (key==word):
				innovation_ctr++
    tags = []
    if (management_ctr >= 3):
    	tags.append("management")
    if (legal_ctr >= 3):
    	tags.append("legal")
    if (financial_ctr >= 3):
    	tags.append("financial")
    if (humanresc_ctr >= 3):
    	tags.append("humanresc")
    if (innovation_ctr >= 3):
    	tags.append("innovation")
    if (len(tags)==0):
    	classdict = {"management": management_ctr, "legal": legal_ctr, "financial": financial_ctr, "humanresc":humanresc_ctr, "innovation": innovation_ctr}
    	tags.append(max(classdict, key=classdict.get))
    return tags

