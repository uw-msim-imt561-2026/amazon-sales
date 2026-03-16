# Amazon Sales Dashboard

## Streamlit Dashboard
https://amazon-sales-xt9xnmjw24ta7xpnjeugas.streamlit.app

The ultimate goal is to create a dashboard that enables stakeholders to monitor key performance indicators (KPIs), identify growth opportunities, and uncover relationships between different factors.

## Data Set

The Amazon.csv data is retrieved from Kaggle (https://www.kaggle.com/datasets/rohiteng/amazon-sales-dataset)

The Amazon Sales dataset was created by Rohit Kumar, a machine learning student from India, for analytics and machine learning training. The dataset is synthetic, meaning it is not collected from Amazon’s internal systems but is designed to simulate real-world e-commerce transactions.

We selected this dataset because Amazon is a major player in U.S. e-commerce, and many consumers, including ourselves, frequently use the platform for online shopping and groceries. Since our group is interested in retail analytics, the dataset provides a useful way to explore sales patterns, customer behavior, and product performance. For example, we are interested in examining whether discount levels influence purchasing behavior.

Over the period of 2020-2025, the dataset contains 100,000 records of transactions. Key features include:
- Geographic: City, State, Country
- Product: Category, ProductID, Product Name, Brand
- Financial: Unit Price, Quantity, Discount, Total Amount, Tax, Shipping Cost
- Logistics: Order ID, Order Status, Order Date, Seller ID, Customer ID, Customer Name, Payment Method

For our analysis, we focus on the following core variables:
- Geographic: State
- Product: Category
- Financial: Unit Price, Quantity, Discount, Total Amount, Tax
- Logistics: Order Date, Payment Method

Because the dataset is synthetic, it is generally well-structured and clean. However, we identified inconsistencies in the city/state and country fields. For example, entries such as “Austin, TX” were paired with the country “Australia.” Since the city and state clearly correspond to U.S. locations, we removed the country column and limited the analysis to the United States, where Amazon usage is strongest.

From an ethical perspective, synthetic data does not fully represent real-world behavior. As a result, the insights generated from this dataset should not be interpreted as representative of all Amazon users or markets. It is important to clearly disclose that the analysis is based on simulated data, and any patterns identified should be interpreted with caution.

## Ethical Considerations

The primary ethical concern with this dataset is its synthetic nature, meaning it was not collected from real Amazon transactions and, therefore, should not be used for real-world insights. The dataset also contains geographical inconsistencies, such as cities like Washington, DC being incorrectly mapped to countries like India. If presented as authentic data, these errors could create misleading geographic patterns, potentially causing stakeholders to draw incorrect conclusions or make flawed strategic decisions based on what are essentially “geographical hallucinations.”

The dataset also shows signs of systemic demographic bias. For example, naming conventions are predominantly South Asian regardless of the region listed, which could produce skewed demographic interpretations if taken literally. In addition, the dataset contains an unusually balanced distribution of product categories, creating a uniformity bias that does not reflect the complexity of real-world retail markets.

Because of these limitations, there is a risk that bad actors or misinformed stakeholders could misuse visualizations to claim evidence of consumer behavior or market trends that are not supported by real data. To mitigate this risk, any analysis or visualization derived from the dataset should be clearly labeled as simulated or educational to prevent the spread of misleading business insights.

## Audience
### Amazon Sales Team (primary stakeholder)
- They are sales managers, business development managers, and business analysts who work directly with third-party sellers on the Amazon marketplace. Their role is to support sellers, monitor marketplace performance, and identify opportunities to grow sales across different product categories and regions.
- The dataset provides key information about product categories, pricing, discounts, geographic sales distribution, and purchasing behavior over time. These variables allow the sales team to examine patterns across the marketplace and identify broader trends.
- Their goal is to use these insights to optimize marketplace performance and support strategic decision-making. Specifically, the data visualization can help them identify high-performing product categories, understand regional demand patterns, evaluate the effectiveness of promotions, and recognize seasonal sales trends. 

### Third-party vendors & sellers (secondary stakeholder)
- They are third-party vendors and sellers who list products on the Amazon marketplace. These sellers operate as independent businesses and are responsible for managing their product listings, pricing strategies, promotions, and inventory levels. 
- The dataset provides insights into market demand, product performance, and the potential impact of pricing strategies on sales outcomes.
- Their goal is to maximize product visibility, increase sales, and remain competitive within the marketplace. They are particularly interested in identifying which product categories generate the most revenue, which geographic regions show strong demand, and how discounts influence customer purchasing behavior. Insights from the dashboard can help them make data-driven decisions about pricing, inventory planning, and product strategy, allowing them to better position their products in a competitive e-commerce environment.

## Context
This project was designed to transform a large transactional dataset into an interactive dashboard that allows users to explore patterns in Amazon marketplace sales. The main challenge stakeholders face is that large transactional datasets are difficult to interpret using raw tables alone. The dashboard therefore aims to help stakeholders to organize and visualize these data to identify patterns and relationships within the data by summarizing key variables through interactive visualizations.

Some of the key questions that stakeholders seek to answer are:
- Which geographic regions generate the highest and lowest sales?
- How do product category sales change over time?
- How do payment methods and discounts relate to customer spending?
- What relationships exist among major numerical variables in the dataset?
- Which areas of sales performance may require strategic attention?

Together, these questions help stakeholders investigate how geographic factors, payment behavior, pricing variables, and product categories interact to shape overall sales performance within the dataset. The dashboard enables users to explore complex transactional data and generate insights about patterns in marketplace activity.

## Start
You can download our repository code and follow through. Please start with the below.
```bash
python -m venv .venv
source .venv/bin/activate  # (Windows: .venv\Scripts\activate)
pip install -r requirements.txt
streamlit run app.py
```
