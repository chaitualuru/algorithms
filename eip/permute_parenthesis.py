def permute_parentheses(num_open, num_close, S):
	if num_open == 0 and num_close == 0:
		print S

	if num_open > 0:
		permute_parentheses(num_open - 1, num_close + 1, S + '{')

	if num_close > 0:
		permute_parentheses(num_open, num_close - 1, S + '}')

permute_parentheses(3, 0, '')