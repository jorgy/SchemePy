import parser

def eval(expr):
	if is_constant(expr):
		return eval_constant(expr)

	if is_quoted(expr):
		return eval_quoted(expr)

	return None


def eval_constant(expr):
	return expr[0][1]


def is_constant(expr):
	if len(expr) != 1:
		return False

	lex = expr[0][0]

	if lex in [parser.NUMBER, parser.STRING, parser.BOOLEAN]:
		return True

	return False


def eval_quoted(expr):
	if expr[0][0] == parser.QUOTE:
		if expr[1][0] in [parser.ID, parser.NUMBER, parser.STRING, parser.BOOLEAN]:
			return expr[1][1]

	return None


def is_quoted(expr):
	if len(expr) < 2:
		return False

	if expr[0][0] == parser.QUOTE:
		return True

	return False
