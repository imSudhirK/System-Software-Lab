with open('employees.txt', 'r') as input_file:
    lines = input_file.readlines()

with open('output.txt', 'w') as output_file:
    for line in lines:
        words = line.split()
        for word in words:
            if word.isalpha():
                output_file.write(word[3:] + word[:3] + " ")
        output_file.write('\n')