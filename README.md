# DU-DataScrape-Project

2/20/26: Pluto added in main.py with the hard parser, installed git hook and pylint. Unsure as to whether or not this will go on to the rest of the repo. Needs to add the yaml to make pylint and pre-commit work.

3/4/26: Pluto added in the .pre-commit-config.yaml for pre-commit and pylint.

3/25/26: Pluto added in the argparse module and added in a few lines to set up the argparse in main. Updated pylint as well, however it is still having some issues as pylint is not up to date with python 3.14. Had to comment out some of the .yaml file as it is giving issues.

4/10/26: Had to create a new virtiual environment to successfully install protobuf into the python system. From there, I made a simple test.proto file that had config messages. Using that, I was able to create the test_pb2.py file by running "protoc --python_out=. test.proto" which is just the python bindings. I then made a config.txtpb which is sample data for the mean time. After that I adjusted main.py to load the protobuf data and output it and it seemed to workout just fine. 