import hashlib
import os

def remove_duplicate(path):
    unique = {}
    os.chdir(path)
    for file in os.scandir(path):
        if file.is_file():
            with open(file.name, 'rb') as f:
                filehash = hashlib.md5(f.read()).hexdigest()
                if filehash not in unique:
                    unique[filehash] = [file.name]
                else:
                    unique[filehash].append(file.name)

    for filehash, filenames in unique.items():
        if len(filenames) > 1:
            print(f'Removing duplicates: {", ".join(filenames[1:])}')
            for filename in filenames[1:]:
                os.remove(filename)

if __name__ == '__main__':
    path = r'D:\sample'
    remove_duplicate(path)
