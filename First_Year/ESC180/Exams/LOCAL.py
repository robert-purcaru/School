import math
import numpy as np

def initialize_file(fileName):
    return open(fileName, encoding="utf8").read()


if __name__ == "__main__":
    file = initialize_file("diseases/Acariasis.html")
    