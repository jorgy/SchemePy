import parser

def eval(expr):
	if is_constant(expr):
		return eval_constant(expr)
	return "okay"


def eval_constant(expr):
	return expr[0][1]


def is_constant(expr):
	if len(expr) != 1:
		return False

	lex = expr[0][0]

	if lex in [parser.NUMBER, parser.STRING, parser.BOOLEAN]:
		return True

	return False
