import io

with io.open("source.txt") as file:
    print(file.readline().split(','))
    file.close()