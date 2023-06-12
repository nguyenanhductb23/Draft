# Define some helper functions
def lowerhalf(I):
    # Return the lower half of an interval
    return (I[0], (I[0] + I[1]) / 2)

def upperhalf(I):
    # Return the upper half of an interval
    return ((I[0] + I[1]) / 2, I[1])

def rescale_lowerhalf(I):
    # Rescale the interval to [0, 0.5)
    return (2 * I[0], 2 * I[1])

def rescale_upperhalf(I):
    # Rescale the interval to [0.5, 1)
    return (2 * I[0] - 1, 2 * I[1] - 1)

def binary_repr(x, n):
    # Return the binary representation of a number x with n bits
    return format(x, '0' + str(n) + 'b')

# Define the main function
def arithmetic_coding(sequence, symbols, probabilities):
    # Output binary string for a sequence of symbols
    # Input: sequence: a list of symbols
    #        symbols: a list of unique symbols
    #        probabilities: a list of probabilities for each symbol
    # Output: bin_string: a binary string

    # Initialize the interval to [0, 1)
    I = (0, 1)

    # Initialize the output string to empty
    bin_string = ''

    # Loop through the sequence of symbols
    for x in sequence:

        # Find the corresponding sub-interval for x
        index = symbols.index(x) # Get the index of x in symbols
        lower = sum(probabilities[:index]) # Get the lower bound of sub-interval
        upper = lower + probabilities[index] # Get the upper bound of sub-interval
        s_x = (lower, upper) # Get the sub-interval

        # While the sub-interval does not contain 0.5
        while not (s_x[0] < 0.5 and s_x[1] > 0.5):

            # If the sub-interval is in the lower half of I
            if s_x[1] <= 0.5:

                # Emit "0" and rescale I to [0, 0.5)
                bin_string += '0'
                I = rescale_lowerhalf(I)
                print(I)

            # If the sub-interval is in the upper half of I
            elif s_x[0] >= 0.5:

                # Emit "1" and rescale I to [0.5, 1)
                bin_string += '1'
                I = rescale_upperhalf(I)
                print(I)

            # Update the sub-interval according to the new I
            s_x = (I[0] + (s_x[0] - lower) / (upper - lower) * (I[1] - I[0]),
                   I[0] + (s_x[1] - lower) / (upper - lower) * (I[1] - I[0]))

        # Set I to be the sub-interval for x
        I = s_x

        # If this is the last symbol in the sequence
        if x == sequence[-1]:

            # Emit binary representation of a point in s_x with enough bits
            n = int(math.ceil(math.log(1 / (upper - lower), 2))) # Number of bits needed
            point = int((s_x[0] + s_x[1]) / 2 * (2 ** n)) # A point in s_x scaled by 2^n
            bin_string += binary_repr(point, n) # Append binary representation of point

    # Return the output string
    return bin_string

# Example usage
sequence = ['a', 'b', 'c', 'a', 'd']
symbols = ['a', 'b', 'c', 'd']
probabilities = [0.4, 0.3, 0.2, 0.1]
bin_string = arithmetic_coding(sequence, symbols, probabilities)
print(bin_string)

