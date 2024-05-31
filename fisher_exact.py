import scipy.stats as stats

# Construct the contingency table
table = [[39, 63], [30961, 30937]]

# Perform Fisher's exact test
oddsratio, p_value = stats.fisher_exact(table, alternative='less')

# Print the p-value with at least 4 decimal places
print(f"P-value: {p_value:.4f}")
