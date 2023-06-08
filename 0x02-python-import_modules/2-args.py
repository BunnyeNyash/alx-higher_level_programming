#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    def print_arguments():
        arguments = sys.argv[1:]
        num_arguments = len(arguments)

        print("Number of argument(s):", num_arguments)
        print("Argument" if num_arguments == 1 else "Arguments", end="")
        print(":", end=" " if num_arguments > 0 else ".\n")

        for i, arg in enumerate(arguments, 1):
            print(i, ":", arg)

        if num_arguments == 0:
            print("No arguments provided.")

    print_arguments()
