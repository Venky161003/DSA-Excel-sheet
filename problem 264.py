class Solution():

	def __init__(self):
		pass

	def printItinerary(self,d):

		reverse_d = dict()
		for i in d:
			reverse_d[d[i]] = i

		for i in reverse_d:
			if reverse_d[i] not in reverse_d:
				starting_pt = reverse_d[i]
				break;
			    
		while(starting_pt in d):
			print(starting_pt,"->",d[starting_pt],end=", ")
			starting_pt = d[starting_pt]



if __name__=="__main__":

	d = dict()
	d["Chennai"] = "Banglore"
	d["Bombay"] = "Delhi"
	d["Goa"] = "Chennai"
	d["Delhi"] = "Goa"


	obj = Solution()
	obj.printItinerary(d)
