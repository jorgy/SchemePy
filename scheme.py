import sys
import parser
import eval



def tokenize(expr):
	tokens = []
	expr = expr.strip()

	while len(expr) != 0:
		token = parser.next_token(expr)

		if token == None:
			print 'Syntax error!'
			return tokens

		i = expr.index(token[1])
		expr = expr[i + len(token[1]):]

		tokens.append(token)

	return tokens


def run_interpreter():
	while True:
		try:
			expr = raw_input("STk> ").lower()
		except EOFError:
			print "Bye!"
			exit(0)

		tokens = tokenize(expr)
		evaluated = eval.eval(tokens)
		print evaluated


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
