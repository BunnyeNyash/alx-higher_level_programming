#!/usr/bin/python3
if __name__ == "__main__":
    import sys   # to access argv

    argv = sys.argv[1:]  # Exclude the script name from the arguments

    num_args = len(argv)

    print("{} argument{}:".format(num_args, 's' if num_args != 1 else ''))
    for i, arg in enumerate(argv, 1):
        print("{}: {}".format(i, arg))
