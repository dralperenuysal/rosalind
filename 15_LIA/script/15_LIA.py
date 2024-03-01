from scipy.stats import binom

# Function to calculate the probability of having at least N AaBb offspring
def probability_at_least_N_AaBb(k, N):
    total_offspring = 2 ** k
    p_AaBb = 1 / 16  # Probability of an offspring being AaBb

    # Calculate the probability of having at least N AaBb offspring
    prob = sum([binom.pmf(n, total_offspring, p_AaBb) for n in range(N, total_offspring + 1)])

    return prob

# Example usage
k = 2  # Example value for k
N = 1  # Example value for N
prob = probability_at_least_N_AaBb(k, N)
print(f"Probability: {prob}")