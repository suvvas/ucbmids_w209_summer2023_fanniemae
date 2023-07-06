import math

def sigmoid(x):
    """Calculate the sigmoid of x."""
    return 1 / (1 + math.exp(-x))