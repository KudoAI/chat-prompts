def read(file_path):
    import tomli
    with open(file_path, 'rb') as file:
        return tomli.load(file)

def write(file_path, data):
    import tomli_w
    with open(file_path, 'wb') as file:
        tomli_w.dump(data, file)
