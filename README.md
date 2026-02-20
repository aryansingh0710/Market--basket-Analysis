A Data Mining Project for Identifying Product Associations and Customer Buying Patterns

Market Basket Analysis (MBA) is a powerful data-mining technique used in retail and e-commerce to understand customer purchase behavior. This project uses the Apriori algorithm to uncover frequent itemsets and generate association rules that reveal which products are often bought together.

Project Overview

This project analyzes transactional retail data to:

Identify frequently purchased product combinations

Generate association rules using the Apriori algorithm

Compute support, confidence, and lift

Visualize most common itemsets and rules

Provide insights for:

Cross-selling

Product placement

Discount bundling

Recommendation systems

The project is implemented in Python using Jupyter Notebook.
Key Concepts
Frequent Itemsets

Groups of items frequently purchased together (e.g., Milk & Bread).

Association Rules

Rules like:
If a customer buys A → they are likely to buy B

Measured using:

Support – frequency of itemset in the dataset

Confidence – probability of B given A

Lift – strength of the association

 Tech Stack
Component	Technology
Language	Python
Notebook	Jupyter Notebook
Libraries	pandas, numpy, mlxtend, matplotlib, seaborn
Algorithm	Apriori (Association Rule Mining)

Dataset:-
The dataset contains retail-style transactional data, where each row represents a basket of items purchased by a customer.
