import argparse
from google.protobuf import text_format
import test_pb2


def main():
    parser = argparse.ArgumentParser(description='A simple Python script with command-line arguments')
    parser.add_argument('--verbose', action='store_true', help='Enable verbose output')
    parser.add_argument('--proto', type=str, help='Path to the .proto file to use')
    parser.add_argument('--config', type=str, default='config.txtpb', help='Path to txtpb config file')

    args = parser.parse_args()

    if args.verbose:
        print("Verbose mode enabled")

    print("Hello, World!")

    # PROTOBUF LOADING HERE
    config_list = test_pb2.ConfigList()

    with open(args.config, "r") as f:
        text_format.Parse(f.read(), config_list)

    if args.verbose:
        print("\nLoaded configs:")

    for config in config_list.configs:
        print(config.name, config.value)


if __name__ == '__main__':
    main()