from gendiff.arg_argparse import get_args
from gendiff.generate import generate_diff

args = get_args()


def main():
    diff = generate_diff(args.first_file, args.second_file, args.format)
    print(diff)


if __name__ == '__main__':
    main()
