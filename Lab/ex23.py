
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

df = pd.read_csv("clinical_trial.csv")

control = df["control"]
treatment = df["treatment"]

t_stat, p_value = stats.ttest_ind(
    treatment, control, equal_var=False
)

print("Control Mean:", control.mean())
print("Treatment Mean:", treatment.mean())
print("T-statistic:", t_stat)
print("P-value:", p_value)

if p_value < 0.05:
    print("Reject Null Hypothesis")
    print("Treatment has a significant effect")
else:
    print("Accept Null Hypothesis")
    print("No significant effect found")

plt.boxplot([control, treatment],
            labels=["Control", "Treatment"])

plt.title("Clinical Trial Comparison")
plt.ylabel("Treatment Outcome")
plt.show()
