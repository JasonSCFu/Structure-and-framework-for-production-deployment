import argparse

def init_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--e" , type = float)
    return parser

def parse_args():
    parser = init_args()
    return parser.parse_args()

if __name__ == "__main__":
    pass
