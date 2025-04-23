"""
Association Rule Mining using Apriori Algorithm
- Generates frequent itemsets
- Extracts strong association rules
"""

from mlxtend.frequent_patterns import apriori, association_rules

def generate_frequent_itemsets(df_encoded, min_support=0.009):
    return apriori(df_encoded, min_support=min_support, use_colnames=True)

def generate_rules(frequent_itemsets, metric="confidence", min_threshold=0.5):
    return association_rules(frequent_itemsets, metric=metric, min_threshold=min_threshold)
