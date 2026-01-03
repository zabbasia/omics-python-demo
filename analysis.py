import os
import pandas as pd

  # ساخت پوشه results
os.makedirs("results", exist_ok=True)

 # خواندن داده‌ها
expr = pd.read_csv("data/expression_matrix.csv", index_col=0)
samples = pd.read_csv("data/samples.csv")

print("data read:")
print(expr.head())

 # نگاشت نمونه به گروه

sample_to_group = dict(zip(samples["sample"], samples["condition"]))
print("\n sample sheet mapping", sample_to_group)

 # محاسبه میانگین هر گروه
groups = sorted(samples["condition"].unique())
group_means = {}

for g in groups:
    cols = [s for s in expr.columns if sample_to_group[s] == g]
    group_means[g] = expr[cols].mean(axis=1)
    print(f"\n GroupMean {g}:")
    print(group_means[g].head())

 # ساخت جدول نهایی
group_means_df = pd.DataFrame(group_means)
group_means_df["log2FC"] = (group_means_df["treated"] + 1) / (group_means_df["control"] + 1)
group_means_df["log2FC"] = group_means_df["log2FC"].apply(lambda x: round(x, 3))

 # ذخیره
group_means_df.to_csv("results/group_means.csv")
print("\n✅ analysis finished & file results/group_means.csv made")
