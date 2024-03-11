def convert_file_encoding(input_filename, output_filename, input_encoding='windows-1251', output_encoding='utf-8'):
    # 打开输入文件，使用Windows-1251编码读取内容
    with open(input_filename, 'r', encoding=input_encoding) as input_file:
        contents = input_file.read()

    # 打开输出文件，使用UTF-8编码写入内容
    with open(output_filename, 'w', encoding=output_encoding) as output_file:
        output_file.write(contents)


if __name__ == "__main__":
    input_filename = 'russian.txt'  # 输入源文件文件的名称，Windows-1251编码
    output_filename = 'output_utf8.txt'  # 输出，UTF-8
    convert_file_encoding(input_filename, output_filename)