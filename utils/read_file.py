def read_file(path: str):
    text_file = open(path, "r")
    input_str = text_file.read()
    text_file.close()

    return input_str
