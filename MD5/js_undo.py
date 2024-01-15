from jsbeautifier import beautify_file

# 指定混淆的JavaScript文件和输出的文件
input_file = 'test.js'
output_file = 'deobfuscated.js'

# 使用 js-beautify 进行反混淆
beautify_file(input_file, output_file)
