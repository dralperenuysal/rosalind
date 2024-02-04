# Check the working directory
getwd()

dominant_offspring <- function(file_path) {
  couples <- scan(file_path) # Read the input
  offspring_prob <- c(1, 1, 1, 0.75, 0.5, 0) # Probability vector
  offspring_per_couple <- 2 # constant
  dominant_offspring <- sum(couples * offspring_prob * offspring_per_couple) # calculation
  return(dominant_offspring) # Return the result
}

dominant_offspring("13_IEV/resource/rosalind_iev.txt")

