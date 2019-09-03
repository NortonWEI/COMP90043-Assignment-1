# Author: Norton Wei

def extended_euclidean(a, b):
    """It is known that the equation can be written as: gcd = ax + by.
    In this function we assume b = qa + b%a.
    Since b = a*0 + b*1 and for the next iteration, a = a*1 + b*0,
    we have prev_x, x, prev_y, y = 0, 1, 1, 0"""
    prev_x, x = 0, 1
    prev_y, y = 1, 0

    """Loop until a becomes 0."""
    while a != 0:
        q = b // a
        b, a = a, b % a

        """It will be proved that why x = prev_x - q * x and y = prev_y - q * y."""
        x, prev_x = prev_x - q * x, x
        y, prev_y = prev_y - q * y, y

    gcd = b
    return gcd, prev_x, prev_y


def inverse(a, n):
    """We should make sure a and n are 2 positive integers."""
    try:
        val_a, val_n = int(a), int(n)
        if val_a <= 0 or val_n <= 0:
            raise ValueError('Please input 2 positive integers!')
    except ValueError:
        print('Please input 2 positive integers!')
        return

    """Reuse the extended_euclidean function."""
    gcd, x, y = extended_euclidean(a, n)

    """Check if the inverse exists."""
    if gcd != 1:
        try:
            raise ValueError(a, 'mod', n, 'does not have an inverse!')
        except ValueError:
            print(a, 'mod', n, 'does not have an inverse!')
            return

    """Ensure the result to be positive."""
    if x < 0:
        x += n

    return x


def main():
    gcd, x, y = extended_euclidean(323, 51)
    print('gcd =', gcd, ', x =', x, ', y =', y)

    print('The inverse is:', inverse(15, 25))


if __name__ == '__main__':
    main()
