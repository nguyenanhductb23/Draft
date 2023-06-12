import decimal

def encode(encode_str, N, alphabet):
    count = dict.fromkeys(alphabet, 1)  # probability table
    cdf_range = dict.fromkeys(alphabet, 0)
    pdf = dict.fromkeys(alphabet, 0)

    low = 0
    high = decimal.Decimal(1) / decimal.Decimal(len(alphabet))

    for key in sorted(cdf_range):
        cdf_range[key] = [low, high]
        low = high
        high += decimal.Decimal(1) / decimal.Decimal(len(alphabet))

    for key in sorted(pdf):
        pdf[key] = decimal.Decimal(1) / decimal.Decimal(len(alphabet))

    i = len(alphabet)

    lower_bound = 0  # upper bound
    upper_bound = 1  # lower bound

    u = 0

    # go thru every symbol in the string
    for sym in encode_str:
        i += 1
        u += 1
        count[sym] += 1

        curr_range = upper_bound - lower_bound  # current range
        upper_bound = lower_bound + (curr_range * cdf_range[sym][1])  # upper_bound
        lower_bound = lower_bound + (curr_range * cdf_range[sym][0])  # lower bound

        # update cdf_range after N symbols have been read
        if u == N:
            u = 0

            for key in sorted(pdf):
                pdf[key] = decimal.Decimal(count[key]) / decimal.Decimal(i)

            low = 0
            for key in sorted(cdf_range):
                high = pdf[key] + low
                cdf_range[key] = [low, high]
                low = high

    return lower_bound

def decode(encoded, strlen, every, alphabet):
    decoded_str = ""

    count = dict.fromkeys(alphabet, 1)  # probability table
    cdf_range = dict.fromkeys(alphabet, 0)
    pdf = dict.fromkeys(alphabet, 0)

    low = 0
    high = decimal.Decimal(1) / decimal.Decimal(len(alphabet))

    for key in sorted(cdf_range):
        cdf_range[key] = [low, high]
        low = high
        high += decimal.Decimal(1) / decimal.Decimal(len(alphabet))

    for key in sorted(pdf):
        pdf[key] = decimal.Decimal(1) / decimal.Decimal(len(alphabet))


    lower_bound = 0  # upper bound
    upper_bound = 1  # lower bound

    k = 0

    while strlen != len(decoded_str):
        for key in sorted(pdf):

            curr_range = upper_bound - lower_bound  # current range
            upper_cand = lower_bound + (curr_range * cdf_range[key][1])  # upper_bound
            lower_cand = lower_bound + (curr_range * cdf_range[key][0])  # lower bound

            if lower_cand <= encoded < upper_cand:
                k += 1
                decoded_str += key

                if strlen == len(decoded_str):
                    break

                upper_bound = upper_cand
                lower_bound = lower_cand

                count[key] += 1

                if k == every:
                    k = 0
                    for key in sorted(pdf):
                        pdf[key] = decimal.Decimal(count[key]) / decimal.Decimal(len(alphabet) + len(decoded_str))

                    low = 0
                    for key in sorted(cdf_range):
                        high = pdf[key] + low
                        cdf_range[key] = [low, high]
                        low = high

    return decoded_str

def main():
    encode_str = "Hello, world! This is a test string 123 #$%*"
    strlen = len(encode_str)
    every = 3
    alphabet = string.printable  # bao gồm tất cả các ký tự in được
    encoded = encode(encode_str, every, alphabet)
    decoded = decode(encoded, strlen, every, alphabet)
    print(encoded)
    print(decoded)

if __name__ == '__main__':
    main()
