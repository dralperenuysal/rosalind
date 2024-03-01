# Function to calculate the probability of having at least N AaBb offspring
probability <- function(k, N) {
  total_offspring <- 2^k
  p_AaBb <- 1/16  # Probability of an offspring being AaBb

  # Calculate the probability of having at least N AaBb offspring
  prob <- sum(dbinom(N:total_offspring, total_offspring, p_AaBb))

  return(prob)
}

# Example usage
k <- 2  # Example value for k
N <- 1  # Example value for N
prob <- probability(k, N)
print(paste("Probability:", prob))
