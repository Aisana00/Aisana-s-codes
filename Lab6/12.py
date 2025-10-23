input_file = input("Enter input file: ")
output_file = input("Enter output file: ")

with open(input_file, 'r') as reader:
    with open(output_file, 'w') as writer:
        writer.write(reader.read())

print(f"Contents copied from {input_file} to {output_file}")