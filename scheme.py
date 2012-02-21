import sys
import re


def next_token(expr):
	expr = expr.lstrip()

	operator = re.match("[()\+\-\*\/]", expr)
	if operator:
		return operator.group(0)

	quoted_match = re.match("^(\'[a-zA-Z0-9\-]+)", expr)
	if quoted_match:
		return quoted_match.group(1)

	float_match = re.match("^([0-9]+\.[0-9]*)|([0-9]*\.[0-9]+)", expr)
	if float_match:
		return float_match.group(0)

	int_match = re.match("^[0-9]+", expr)
	if int_match:
		return int_match.group(0)



def tokenize(expr):
	tokens = []
	expr = expr.strip()

	while len(expr) != 0:
		token = next_token(expr)
		i = expr.index(token)
		expr = expr[i + len(token):]

		tokens.append(token)

	return tokens


def run_interpreter():
	while True:
		try:
			expr = raw_input("STk> ").lower()
		except EOFError:
			print "Bye!"
			exit(0)

		print tokenize(expr)


def run_file(filename):
	pass


def main(args):
	if len(args) == 1:
		run_interpreter()
	elif len(args) == 2:
		run_file(args[1])
	else:
		usage()
		exit(1)


def usage():
	print "Usage: python scheme.py [FILE.scm]"


if __name__ == '__main__':
	main(sys.argv)
