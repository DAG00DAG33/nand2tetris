import sys

class table_element:
	def __init__(self, symbol, binary):
		self.symbol = symbol
		self.binary = binary

address_table = []
address_table.append(table_element("R0", "0000000000000000"))
address_table.append(table_element("R1", "0000000000000001"))
address_table.append(table_element("R2", "0000000000000010"))
address_table.append(table_element("R3", "0000000000000011"))
address_table.append(table_element("R4", "0000000000000100"))
address_table.append(table_element("R5", "0000000000000101"))
address_table.append(table_element("R6", "0000000000000110"))
address_table.append(table_element("R7", "0000000000000111"))
address_table.append(table_element("R8", "0000000000001000"))
address_table.append(table_element("R9", "0000000000001001"))
address_table.append(table_element("R10", "0000000000001010"))
address_table.append(table_element("R11", "0000000000001011"))
address_table.append(table_element("R12", "0000000000001100"))
address_table.append(table_element("R13", "0000000000001101"))
address_table.append(table_element("R14", "0000000000001110"))
address_table.append(table_element("R15", "0000000000001111"))
address_table.append(table_element("SP", "0000000000000000"))
address_table.append(table_element("LCL", "0000000000000001"))
address_table.append(table_element("ARG", "0000000000000010"))
address_table.append(table_element("THIS", "0000000000000011"))
address_table.append(table_element("THAT", "0000000000000100"))
address_table.append(table_element("SCREEN", "0100000000000000"))
address_table.append(table_element("KBD", "0110000000000000"))

c_table_comp = []
c_table_comp.append(table_element("0", "0101010"))
c_table_comp.append(table_element("1", "0111111"))
c_table_comp.append(table_element("-1", "0111010"))
c_table_comp.append(table_element("D", "0001100"))
c_table_comp.append(table_element("A", "0110000"))
c_table_comp.append(table_element("!D", "0001101"))
c_table_comp.append(table_element("!A", "0110001"))
c_table_comp.append(table_element("-D", "0001111"))
c_table_comp.append(table_element("-A", "0110011"))
c_table_comp.append(table_element("D+1", "0011111"))
c_table_comp.append(table_element("A+1", "0110111"))
c_table_comp.append(table_element("D-1", "0001110"))
c_table_comp.append(table_element("A-1", "0110010"))
c_table_comp.append(table_element("D+A", "0000010"))
c_table_comp.append(table_element("D-A", "0010011"))
c_table_comp.append(table_element("A-D", "0000111"))
c_table_comp.append(table_element("D&A", "0000000"))
c_table_comp.append(table_element("D|A", "0010101"))

c_table_comp.append(table_element("M", "1110000"))
c_table_comp.append(table_element("!M", "1110001"))
c_table_comp.append(table_element("-M", "1110011"))
c_table_comp.append(table_element("M+1", "1110111"))
c_table_comp.append(table_element("M-1", "1110010"))
c_table_comp.append(table_element("D+M", "1000010"))
c_table_comp.append(table_element("D-M", "1010011"))
c_table_comp.append(table_element("M-D", "1000111"))
c_table_comp.append(table_element("D&M", "1000000"))
c_table_comp.append(table_element("D|M", "1010101"))

c_table_dest = []
c_table_dest.append(table_element("", "000"))
c_table_dest.append(table_element("M", "001"))
c_table_dest.append(table_element("D", "010"))
c_table_dest.append(table_element("MD", "011"))
c_table_dest.append(table_element("A", "100"))
c_table_dest.append(table_element("AM", "101"))
c_table_dest.append(table_element("AD", "110"))
c_table_dest.append(table_element("AMD", "111"))

c_table_jump = []
c_table_jump.append(table_element("", "000"))
c_table_jump.append(table_element("JGT", "001"))
c_table_jump.append(table_element("JEQ", "010"))
c_table_jump.append(table_element("JGE", "011"))
c_table_jump.append(table_element("JLT", "100"))
c_table_jump.append(table_element("JNE", "101"))
c_table_jump.append(table_element("JLE", "110"))
c_table_jump.append(table_element("JMP", "111"))


def remove_coments(line):
	coment_pos =  line.rfind('//')
	return line[:coment_pos]

def comand_type(line):
	if not line:
		return 's'
	elif line[0] == '@':
		return 'a'
	elif line[0] == '(':
		return 'l'
	else:
		return 'c'

def aparser(line, table, f):
	#line = unicode(line, 'utf-8')
	if line[1:].isnumeric():
		#print("{0:b}".format(int(line[1:])))
		f.write(format(int(line[1:]), '016b'))
		print(format(int(line[1:]), '016b'), end = "")
		
	else:
		#write(line[1:], table, f)
		for element in table:
			if element.symbol == line[1:]:
				f.write(element.binary)
				f.write(chr(13) + "\n")
				print(element.binary)
				return 0
		global var_count
		table.append(table_element(line[1:], format(var_count, '016b')))
		f.write(table[-1].binary)
		print(table[-1].binary, end = "")
		var_count += 1
	f.write(chr(13) + "\n")
	print("")

def write(string, table, f):
	for element in table:
		if element.symbol == string:
			f.write(element.binary)
			print(element.binary, end = "")

def cparser(line, table_dest, table_comp, table_jump, f):
	first_split = line.rsplit("=")
	if len(first_split) == 1:
		first_split.insert(0, "")
	second_split = first_split[-1].rsplit(";")
	if len(second_split) == 1:
		second_split.insert(1, "")
	f.write("111")
	print("111", end = "")
	write(second_split[0], table_comp, f)
	write(first_split[0], table_dest, f)
	write(second_split[1], table_jump, f)
	f.write(chr(13) + "\n")
	print("")


with open(sys.argv[1] + ".hack", 'w') as hack_file:
	with open(sys.argv[1] + ".asm", "r") as asm_file: 
		n = 0
		for line in asm_file:
			line = remove_coments(line.replace(" ", "").replace(chr(13), ""))
			if comand_type(line) in "ca":
				n = n + 1
			if comand_type(line) == 'l':
				address_table.append(table_element(line[1:].replace(")", ""),format(n, '016b')))
				print(n, line[1:], format(n, '016b'))
		asm_file.seek(0)
		var_count = 16
		for line in asm_file:
			line = remove_coments(line.replace(" ", "").replace(chr(13), ""))
			if comand_type(line) == 'a': #cambiar por un case statement
				aparser(line, address_table, hack_file)
			elif comand_type(line) == 'c':
				cparser(line, c_table_dest, c_table_comp, c_table_jump, hack_file)
			print(line)
