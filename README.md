# 🛒 Market Basket Insights

Market Basket Analysis is a powerful technique to uncover customer purchasing patterns and turn raw transaction data into strategic business insights. Businesses can use these insights to optimize store layout, bundle products, personalize promotions, and more. It’s not just about data—it’s about truly understanding what customers want.

---

## 📚 Table of Contents

- [Introduction](#introduction)
- [Dataset Used](#dataset-used)
- [Libraries Used](#libraries-used)
- [Preprocessing Steps](#preprocessing-steps)
- [Preparing Dataset for Association Rules](#preparing-dataset-for-applying-association-rules)
- [Association Rule Mining](#association-rule-mining)
- [Results & Insights](#results--insights)
- [Visualizations](#visualization)
- [Conclusion](#conclusion)
- [Author](#author)
- [License](#license)

---

## 🧠 Introduction

In this project, we analyzed retail transaction data to discover frequent itemsets and association rules using the Apriori algorithm. The goal was to showcase practical use of market basket analysis techniques for business impact.

---

## 📂 Dataset Used

The dataset used for this analysis was sourced from Kaggle:  
🔗 [Market Basket Analysis Dataset](https://www.kaggle.com/datasets/aslanahmedov/market-basket-analysis)

---

## 🛠️ Libraries Used

Make sure you have these installed:

```bash
pip install pandas numpy matplotlib seaborn mlxtend plotly
```

---

## 🧹 Preprocessing Steps

To clean and prepare the dataset:

- Removed the problematic **111th row** due to CSV loading issues.
- Cleaned unnecessary characters in the `'Country'` column.
- Standardized `'Price'` column to float type.
- Dropped rows with missing values.
- Grouped by `'Bill Number'` and `'Date'` for transaction-level aggregation.

---

## 🧾 Preparing Dataset for Applying Association Rules

- **Item Splitting**: Parsed `Itemname` into separate entries.
- **Data Restructuring**: Reformatted items into individual columns.
- **One-Hot Encoding**: Transformed item presence into binary format.
- **Output**: Saved final processed dataset as `transaction_data_encoded.csv`.

---

## 🧮 Association Rule Mining

We used the `Apriori` algorithm from the `mlxtend` library:

```python
from mlxtend.frequent_patterns import apriori, association_rules

frequent_itemsets = apriori(df_encoded, min_support=0.009, use_colnames=True)
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.5)
```

- Minimum Support: **0.009**
- Confidence Threshold: **0.5**
- Total Rules Discovered: **430**

---

## 📈 Results & Insights

Example Top 5 Rules:

| Antecedents                          | Consequents                     | Support   | Confidence |
|-------------------------------------|----------------------------------|-----------|------------|
| 60 CAKE CASES DOLLY GIRL DESIGN     | PACK OF 72 RETROSPOT CAKE CASES | 0.010061  | 0.543      |
| ALARM CLOCK BAKELIKE CHOCOLATE      | ALARM CLOCK BAKELIKE RED        | 0.011985  | 0.698      |
| ...                                 | ...                              | ...       | ...        |

Adjusting thresholds (e.g., min_support=0.02, min_confidence=0.7) yields **fewer but stronger rules**.

---

## 📊 Visualization

- **Line Plot** — Rules generated across varying confidence thresholds  
  ![Line Plot](https://github.com/Udiesh/IBM-NaanMudhalvan/blob/main/newplot%20(3).png)

- **Interactive Scatter Plot: Support vs Confidence**  
  ![Scatter Plot](https://github.com/Udiesh/IBM-NaanMudhalvan/blob/main/interactive_plot.png)

- **Sunburst Chart** — Hierarchical representation of frequent itemsets  
  ![Sunburst](https://github.com/Udiesh/IBM-NaanMudhalvan/blob/main/newplot%20(5).png)

---

## 🧾 Conclusion

This project successfully demonstrates how businesses can turn raw shopping data into actionable insights. From decoding item affinities to improving shelf arrangements and offers, market basket analysis is a cornerstone of data-driven retail strategy.

---

## 👤 Author

- **Udiesh Kumar**
- [LinkedIn](https://www.linkedin.com/in/udiesh-kumar) | [GitHub](https://github.com/Udiesh)

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

