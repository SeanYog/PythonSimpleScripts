from pathlib import Path

while True:
    dir = Path(input("Enter a directory path:"))

    if Path.is_dir(dir):
        print('thanks! the files in the directory are now being renamed')
        break

    print('the path entered is not valid!')

i = 0
for f in dir.iterdir():
    if f.is_file():
        f.rename(Path.joinpath(dir, f.suffix[1:] + str(i) + f.suffix))
        i += 1

print('done!')