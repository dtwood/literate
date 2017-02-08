#! /usr/bin/env python3


def main():
    import argparse
    import subprocess

    parser = argparse.ArgumentParser()
    parser.add_argument('command', metavar='CMD', type=str)
    parser.add_argument('input', metavar='IN', type=str)

    args = parser.parse_args()

    in_python_block = False
    output = ''

    with open(args.input) as f:
        for line in f:
            if in_python_block:
                if line == '```\n':
                    in_python_block = False
                else:
                    output += line
            else:
                if line == '```python\n':
                    in_python_block = True

    subprocess.run(args.command, input=output.encode('utf-8'))


if __name__ == '__main__':
    main()
