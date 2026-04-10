import argparse

# Argument parser setup
parser = argparse.ArgumentParser(description='A simple Python script with command-line arguments')
parser.add_argument('--verbose', action='store_true', help='Enable verbose output')
parser.add_argument('--proto', type=str, help='Path to the .proto file to use') # Run "pip install protobuf" for the library
args = parser.parse_args()


def main():
    if args.verbose:
        print("Verbose mode enabled")
    print("Hello, World!")

if __name__ == '__main__':
    main()
