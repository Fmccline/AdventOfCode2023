def read_file_to_list(filename):
    contents = []
    with open(filename) as file:
        for line in file:
            contents.append(line)
    return contents

