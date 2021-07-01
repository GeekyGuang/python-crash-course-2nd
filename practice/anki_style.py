import re

try:
    with open('esl.txt', encoding="utf-8") as f:
	    contents = f.read()
except FileNotFoundError:
	print('Error: esl.txt文件不存在')
else:
	contents = re.sub(r'^(.*?) – ', r'<span>\1</span>\t', contents)
	contents = re.sub(r'(?<=\n)(.*?) – ', r'<span>\1</span>\t', contents)
	contents = re.sub(r'\n([^\*<])', r' \1', contents)
	contents = re.sub(r'\n\*\s', r'\t', contents)

	with open('esl_new.txt', 'w', encoding="utf-8") as f:
		f.write(contents)

	print('处理完成！')