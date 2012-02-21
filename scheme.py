import sys
import re

# Define lexical categories
ID      = 'identifier'
COMMENT = 'comment'


def match_identifier(st):
	extended_chars = r"!$%&*+-./:<=>?@^_~"
	pattern = re.compile("^[\+\-]|(\.\.\.)|([a-z" + extended_chars + "][a-z0-9" + extended_chars + "]*)")
	identifier = re.match(pattern, st)
	if identifier:
		return identifier.group(0)
	else:
		return None


def match_comment(st):
	comment = re.match("\s*(;.*)$", st)
	if comment:
		return comment.group(1)
	else:
		return None



def next_token(expr):
	expr = expr.lstrip()

	identifier = match_identifier(expr)
	if identifier:
		return (ID, identifier)

	comment = match_comment(expr)
	if comment:
		return (COMMENT, comment)



def tokenize(expr):
	tokens = []
	expr = expr.strip()

	while len(expr) != 0:
		token = next_token(expr)
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
