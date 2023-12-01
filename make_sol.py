#!/usr/bin/env python3

import os

def main(n, name):
    dirname = f"day{n:02d}_{name}"
    if os.path.isdir(dirname):
        print("Folder already exists. Risk of overwrite of data!")

    with open("to_do.sh", 'w') as f:

        f.write(f"""\
mkdir -p {dirname}

touch {dirname}/input.txt
touch {dirname}/output.txt

sed 's/XX/{n:02d}/g;s/YYY/{name}/g' template/name.py > {dirname}/{name}.py
sed 's/XX/{n:02d}/g;s/YYY/{name}/g' template/test.py > {dirname}/test_{name}.py
chmod u+x {dirname}/{name}.py
""")

    print("Commands have been written to to_do.sh.")

if __name__=="__main__":
    import argparse

    parser = argparse.ArgumentParser(description=
        'Create solution files. To action the commands run to_do.sh with bash'
        )
    parser.add_argument('day', type=int, nargs=1,
                        help='day for which to create a solution')
    parser.add_argument('name', type=str, nargs=1,
                        help='Name of the puzzle')

    args = parser.parse_args()
    main(args.day[0], args.name[0])
