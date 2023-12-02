def fractionToDecimal(numr, denr):

	res = ""

	mp = {}

	rem = numr % denr

	while ((rem != 0) and (rem not in mp)):

		mp[rem] = len(res)

		rem = rem * 10

		res_part = rem // denr
		res += str(res_part)

		rem = rem % denr

	if (rem == 0):
		return ""
	else:
		return res[mp[rem]:]


#Driver code
numr, denr = 50, 22
res = fractionToDecimal(numr, denr)

if (res == ""):
	print("No recurring sequence")
else:
	print("Recurring sequence is", res)
