def read_file(filename):
	lines = []
	with open(filename, 'r', encoding = 'utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
		return lines
def convert(lines):
	AWC = 0
	ASC = 0
	VWC = 0
	VSC = 0
	AIC = 0
	VIC = 0
	for line in lines:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		if name == 'Allen':
			if s[2] == '貼圖':
				ASC += 1
			elif s[2] == '圖片':
				AIC += 1
			else: 
				for m in s[2:]:
					AWC += len(m)
		elif name =='Viki':
			if s[2] == '貼圖':
				VSC += 1
			elif s[2] == '圖片':
				VIC += 1
			else: 
				for m in s[2:]:
					VWC += len(m)
	print('Allen說了', AWC, '個字')
	print('Allen傳了', ASC, '個貼圖')
	print('Allen傳了', AIC, '張圖片')
	print('Viki說了', VWC, '個字')
	print('Viki傳了', VSC, '個貼圖')
	print('Viki傳了', VIC, '張圖片')
def write(filename, lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')

def main():
	lines = read_file('-LINE-Viki.txt')
	lines = convert(lines)

main() 
