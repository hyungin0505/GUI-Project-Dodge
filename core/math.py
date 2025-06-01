def abs(x):
    return x if x >= 0 else -x

def sqrt(x, tolerance=1e-15, max_iterations=100):
    if x < 0:
        raise ValueError("math domain error")

    if x == 0:
        return 0.0

    guess = x / 2.0
    for _ in range(max_iterations):
        new_guess = 0.5 * (guess + x / guess)
        if abs(new_guess - guess) < tolerance:
            return new_guess
        guess = new_guess

    return guess