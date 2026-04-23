"""A simple Python script that currently only has our argument parser
"""
import argparse

def main():
    """
    Main function to parse command-line arguments and execute the script.
    """

    # Argument parser setup
    parser = argparse.ArgumentParser(
        description='A simple Python script with command-line arguments')
    parser.add_argument(
        '--log-level', choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
        default='INFO', help='Set the logging level')
    parser.add_argument(
        '--file-path', type=str, help='Path to the input file')
    parser.add_argument(
        '--platform', choices = ['X', 'Youtube', 'TikTok'], help = 'Select the platform to use')
    args = parser.parse_args()
    print(f"Logging level set to: {args.log_level}")
    print(f"Selected platform: {args.platform}")
    if args.file_path:
        print(f"Input file path: {args.file_path}")
    print("Hello, World!")

if __name__ == '__main__':
    main()
