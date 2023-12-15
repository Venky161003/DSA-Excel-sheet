def divide(dividend, divisor):
	
	sign = (-1 if((dividend < 0) ^ (divisor < 0)) else 1);

	dividend = abs(dividend);
	divisor = abs(divisor);

	quotient = 0;
	temp = 0;

	for i in range(31, -1, -1):
		if (temp + (divisor << i) <= dividend):
			temp += divisor << i;
			quotient |= 1 << i;

	if sign ==-1 :
	quotient=-quotient;
	return quotient;

# Driver code
a = 10;
b = 3;
print(divide(a, b));

a = 43;
b = -8;
print(divide(a, b));

