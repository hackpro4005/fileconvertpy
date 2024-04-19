def file_convert(input_file, output_file):
    with open(input_file, 'rb') as input_file:
        binary_data = input_file.read()
    
    with open(output_file, 'wb') as output_file:
        output_file.write(binary_data)

