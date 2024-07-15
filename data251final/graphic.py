import pandas
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(style="ticks")

# Load the example dataset for Anscombe's quartet

plt.rcParams['figure.figsize'] = [10, 10]
plt.rcParams['figure.dpi'] = 100
plt.tick_params(axis='both', which='major', labelsize=10, labelbottom = False, bottom=False, top = False, left = False, labeltop=True)
sns.set_style("whitegrid")


sns.set_theme(color_codes=True)
tips = sns.load_dataset("tips")
type(tips)
p = sns.lmplot(x="total_bill", y="tip", data=tips)
p.savefig("lm2.png",bbox_inches='tight',transparent=True)
