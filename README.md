
# Market Basket Insights
Market Basket Analysis, a powerful tool, delves into customer purchasing patterns, providing invaluable insights to enhance business strategies. Businesses can strategically place products, create targeted promotions, and enhance the overall shopping experience. It’s not just data; it's about knowing what customers truly want. So let,s look into the world of Market Basket Analysis and turn shopping data into actionable business strategies!


## Introduction
In this straight-forward project, we've dissected a dataset, identifying frequent itemsets prevalent in purchases. Follow our step-by-step analysis to gain practical insights, demonstrating how this technique can be effectively applied in real-world scenarios.
## Dataset Used
The dataset used for this analysis can be found on Kaggle: [Market Basket Analysis Dataset](https://www.kaggle.com/datasets/aslanahmedov/market-basket-analysis)

## Libraries Used
### Prerequisites

Before you begin, ensure you have installed the following libraries:

- **Pandas**
  ```bash
  pip install pandas

- **NumPy**
  ```bash
  pip install numpy

- **Matplotlib**
  ```bash
  pip install matplotlib

- **Seaborn**
  ```bash
  pip install seaborn

- **MLxtend**
  ```bash
  pip install mlxtend

- **Plotly**
  ```bash
  pip install plotly

## Preprocessing Steps

When working with the dataset, several preprocessing steps were carried out to ensure that it is suitable for analysis.

- **Handling Dataset Error:**
   - Manually removed problematic data `111th row` causing loading errors.
   - The dataset was downloaded in CSV format, and upon attempting to load it into Jupyter Notebook, an parsing error occurred due to the `111th row`. After manual deletion, the dataset was loaded successfully.

- **Cleaning Country Column:**
   - Removed unnecessary characters in the `'Country'` column for consistency.

- **Standardizing Price Format:**
   - Converted the `'Price'` column from comma-separated values to float type for uniformity.

- **Handling Missing Values:**
   - Checked for missing values using the `isnull()` function.
   - Dropped rows containing missing values to facilitate accurate association rule mining.

- **Data Aggregation:**
   - Grouped the dataset based on `'Bill Number'` and `'Date'`.

These steps were crucial to prepare the data for the next step of our project.

# Preparing Dataset for Applying Association Rules

**Splitting Item Names:**
- Split the 'Itemname' column into individual items, enabling a more detailed analysis of each purchased item.

**Enhancing Dataset Structure:**
- Concatenated the original DataFrame with the new items DataFrame, restructuring data for effective association rule mining.
- Dropped the original 'Itemname' column, as individual items were now organized into separate columns, simplifying the dataset structure.

**Applying One-Hot Encoding:**
- Converted items to boolean columns using one-hot encoding, a crucial step for association rule mining.
- One-hot encoding provided a binary representation of item presence, enhancing computational efficiency and preparing the data for analysis.

**Saving Processed Data:**
- Utilized one-hot encoding to convert the processed data into boolean columns, ensuring a suitable format for association rule mining.
- Saved the transaction data to a CSV file `transaction_data_encoded.csv`, preserving the structured data for further analysis.



## Association Rule Mining

- To perform Association Rule Mining, we utilized the Apriori algorithm from the `mlxtend` library. Here's how the algorithm was implemented in Python:

```python
from mlxtend.frequent_patterns import apriori, association_rules

# Generate frequent itemsets
frequent_itemsets = apriori(df_encoded, min_support=0.009, use_colnames=True)

# Generate association rules
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.5)
```



## Results & Insights
- We set `min_support=0.009` and `min_threshold=0.5` to strike a balance between computational efficiency and meaningful insights considering system limitations.
- We obtained 430 rules for this combination of `min_support` and `min_threshold`.

- These are the top five association rules for this support value.

| **Antecedents**                               | **Consequents**                      | **Support** | **Confidence** |
|-----------------------------------------------|---------------------------------------|-------------|-----------------|
| 60 CAKE CASES DOLLY GIRL DESIGN              | PACK OF 72 RETROSPOT CAKE CASES      | 0.010061    | 0.543027        |
| 60 TEATIME FAIRY CAKE CASES                  | PACK OF 72 RETROSPOT CAKE CASES      | 0.017318    | 0.500000        |
| ALARM CLOCK BAKELIKE CHOCOLATE               | ALARM CLOCK BAKELIKE GREEN            | 0.011381    | 0.663462        |
| ALARM CLOCK BAKELIKE CHOCOLATE               | ALARM CLOCK BAKELIKE PINK             | 0.009126    | 0.532051        |
| ALARM CLOCK BAKELIKE CHOCOLATE               | ALARM CLOCK BAKELIKE RED              | 0.011985    | 0.698718        |


- For example if we need to find higly associated products we can change the `min_support` and `min_threshold` accordingly.

|    | **Antecedents**                       | **Consequents**                        | **Support** | **Confidence** |
|--- |--------------------------------------|--------------------------------------|---------|-------------|
| 0  | (GARDENERS KNEELING PAD CUP OF TEA) | (GARDENERS KNEELING PAD KEEP CALM)  | 0.025   | 0.731       |
| 1  | (PINK REGENCY TEACUP AND SAUCER)    | (GREEN REGENCY TEACUP AND SAUCER)   | 0.024   | 0.821       |
| 2  | (GREEN REGENCY TEACUP AND SAUCER)   | (ROSES REGENCY TEACUP AND SAUCER)   | 0.028   | 0.775       |
| 3  | (PINK REGENCY TEACUP AND SAUCER)    | (ROSES REGENCY TEACUP AND SAUCER)   | 0.022   | 0.774       |

- From this dataset, setting `min_support=0.02` and `min_threshold=0.7` we obtained this products which are higly associated with each other.
- But this reduces the number of association rules which are generated thus one has to keep that in mind for obtaining sufficient and meaningful rules.

- A Line Plot which shows the number of rules generated for a `min_support=0.009` for different `min_threshold` values.
![Graph](https://github.com/Udiesh/IBM-NaanMudhalvan/blob/main/newplot%20(3).png)

- We can observe that with reducing the threshold value the number of rules generated are increasing. 



## Visualization 
- **Interactive Scatter Plot Support vs Confidence**

![Graph](https://github.com/Udiesh/IBM-NaanMudhalvan/blob/main/interactive_plot.png)

- **Sunburst Chart**
![Graph](https://github.com/Udiesh/IBM-NaanMudhalvan/blob/main/newplot%20(5).png)




## Conclusion
- Our journey through Market Basket Analysis has uncovered valuable insights within customer purchase patterns. By employing advanced techniques and rigorous preprocessing, we deciphered complex relationships among products, enabling businesses to optimize their strategies. From understanding customer preferences to tailoring marketing efforts, this analysis offers a roadmap to data-informed decision-making. 
- Thank you for exploring this journey of data-driven discovery with us. Feel free to delve into the code, explore the visualizations, and uncover further insights!

