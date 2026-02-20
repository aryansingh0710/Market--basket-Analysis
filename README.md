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
📂 Project Structure
Market--basket-Analysis/
│
├── Market_Basket_Analysis.ipynb   # Main notebook
├── datasets/                      # (Optional) transaction dataset
├── README.md                      # Project documentation
└── images/                        # Saved charts (if any)
Steps Performed in Notebook

Data Loading & Cleaning

Handle missing values

Convert transactions to list-based formats

Data Transformation

One-hot encoding for transaction–item mapping

Frequent Itemset Generation
Using Apriori:

from mlxtend.frequent_patterns import apriori

Association Rule Mining
Generate rules:

from mlxtend.frequent_patterns import association_rules

Visualization

Bar plot of top frequent items

Scatter plots for confidence vs support

Heatmaps for lift values

Visualizations Included

Visualization	Description
top_items.png	Top purchased items
frequent_itemsets.png	Most common product groups
rules_scatter.png	Support vs Confidence distribution
lift_heatmap.png	Strength of association between products

Sample Output
Rule: Bread → Butter  
Support: 0.12  
Confidence: 0.65  
Lift: 1.80  
Use-Cases & Applications

Product Placement Optimization

Inventory Planning

Recommendation Systems

Personalized Offers

Retail Analytics

Future Improvements

Implement FP-Growth algorithm

Deploy as a Streamlit dashboard

Real-time recommendation pipeline

Add interactive visualizations (Plotly)

Author

Aryan Singh
B.Tech | AI & Data Science
GitHub: @aryansingh0710
