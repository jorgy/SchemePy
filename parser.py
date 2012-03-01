import re


# Define lexical categories
ID       = 'identifier'
BOOLEAN  = 'boolean'
NUMBER   = 'number'
STRING   = 'string'
LPAREN   = 'left-paren'
RPAREN   = 'right-paren'
VSTART   = 'vector-start'
QUOTE    = 'quote-mark'
BACKTICK = 'backtick'
DOT      = 'dot'


def match_identifier(st):
	'''Match a single Scheme identifier'''

	special_initial = "\!\$\%\&\*\/\:\<\=\>\?\^\_\~"
	initial = "[a-z" + special_initial + "]"
	special_subsequent = "\+\-\.\@"
	subsequent = "[a-z0-9" + special_initial + special_subsequent + "]"
	peculiar = "(\+)|(\-)|(\.\.\.)"

	pattern = "^(" + initial + subsequent + "*)|(" + peculiar + ")"
	identifier = re.match(pattern, st)
	if identifier:
		return identifier.group(0)
	else:
		return None


def match_boolean(st):
	'''Match a single literal boolean'''

	boolean = re.match("^#t|#f", st)
	if boolean:
		return boolean.group(0)
	else:
		return None


def match_number(st):
	'''
	Match a single Scheme number.

	This matcher is not yet fully R5RS compliant.
	'''

	def radix(R):
		d = {2: "#b", 8: "#o", 10: "(#d)?", 16: "#x"}
		return d[R]

	def digit(R):
		d = {2: "[01]", 8: "[0-7]", 10: "[0-9]", 16: "[0-9a-f]"}
		return d[R]

	def uinteger(R):
		return digit(R) + "+#*"

	def decimal():
		pattern = "(\." + digit(10) + "+#*" + suffix + ")"
		pattern += "|(" + digit(10) + "+\." + digit(10) + "*#*" + suffix + ")"
		pattern += "|(" + digit(10) + "+#+\.#*" + suffix + ")"
		pattern += "|(" + uinteger(10) + suffix + ")"

		return pattern

	def ureal(R):
		pattern = ""
		if R == 10:
			pattern += "(" + decimal() + ")|"
		pattern += "(" + uinteger(R) + ")"
		return pattern

	def real(R):
		return sign + ureal(R)

	def prefix(R):
		return "(" + radix(R) + exactness + ")|(" + exactness + radix(R) + ")"

	exponent = "[esfdl]"
	sign = "[\+\-]?"
	exactness = "(#i|#e)?"
	suffix = "(" + exponent + sign + digit(10) + "+)?"

	#number = "^((" + real(2) + ")|(" + real(8) + ")|(" + real(10) + ")|(" + real(16) + "))"
	number = "^(" + real(10) + ")"
	pattern = re.compile(number)

	is_match = re.match(pattern, st)
	if is_match:
		return is_match.group(0)
	else:
		return None


def match_string(st):
	'''Match a single Scheme string.'''

	string_element = r"[^\"\\]|(\")|(\\)"
	pattern = r"^\"(" + string_element + r")*\""

	match = re.match(pattern, st)
	if match:
		return match.group(0)
	else:
		return None



def next_token(st):
	'''Return the next token in ST'''
	st = st.lstrip()

	number = match_number(st)
	if number:
		return (NUMBER, number)

	identifier = match_identifier(st)
	if identifier:
		return (ID, identifier)

	boolean = match_boolean(st)
	if boolean:
		return (BOOLEAN, boolean)

	string = match_string(st)
	if string:
		return (STRING, string)

	lparen = re.match("^\(", st)
	if lparen:
		return (LPAREN, lparen.group(0))

	rparen = re.match("^\)", st)
	if rparen:
		return (RPAREN, rparen.group(0))

	vector = re.match("^#\(", st)
	if vector:
		return (VSTART, vector.group(0))

	quote = re.match("^'", st)
	if quote:
		return (QUOTE, quote.group(0))

	dot = re.match("^\.", st)
	if dot:
		return (DOT, quote.group(0))

	return None

