# Amazon Sales Dashboard

## Streamlit Dashboard
https://amazonsale1-2uku3ty6pxgg4ikfndbb58.streamlit.app

The ultimate goal is to create a dashboard that enables stakeholders to monitor key performance indicators (KPIs), identify growth opportunities, and detect operational bottlenecks.

## Data Set

The Amazon.csv data is retrieved from Kaggle (https://www.kaggle.com/datasets/rohiteng/amazon-sales-dataset)

The dataset is synthetic, meaning it is not real but designed to closely resemble real-world online retail behavior. It is created by Rohit Kumar, a machine learning student from India, intended for analytics and machine learning training. As a result, the data is already clean and well-structured. However, there are inconsistencies - particularly mismatches between the city/state and country fields. For example, entries such as “Austin, TX” are paired with a country like “Australia.” Because the city and state clearly correspond to U.S. locations, we removed the country column and focused the analysis solely on the U.S., where Amazon usage is strongest.

Over the period of 2020-2025, the dataset contains 100,000 records of transactions, key features include:
- Geographic: City, State, and Country
- Product: Category, Product Name, and Brand
- Financial: Unit Price, Quantity, Discount, Total Amount
- Logistics: Order Status, Order Date, Payment Method

We selected this dataset because Amazon is a major powerhouse in U.S. e-commerce. Since our group is interested in retail, the data provides a useful way to explore patterns in online transactions, including sales trends, customer behavior, and product performance.

## Ethical Considerations

Since this is not real Amazon data, it may not fully reflect real-world conditions. Synthetic data is generated rather than observed so it can contain hidden biases or unrealistic patterns. Therefore, our group clearly disclose that the dataset is synthetic and avoid presenting the findings as real business insights. Without this transparency, the analysis could mislead readers or decision-makers, especially since the dataset is not representative of all Amazon users or markets. 

## Audience
This dashboard will best serve the Amazon teams to better monitor key performance indicators (KPIs), identify growth opportunities, and detect operational bottlenecks
### Sales & Operations Team (primary stakeholder)
- They are responsible for managing product sales performance, inventory flow, and order fulfillment.
- The dataset provides insights into sales volume, product performance, and regional demand, helping them identify top-selling products and operational trends.
- Their goal is to optimize sales performance, improve inventory planning, and ensure efficient order fulfillment based on demand patterns.

### Marketing Team (secondary stakeholder)
- They are responsible for promoting products, driving customer engagement, and increasing sales through targeted campaigns. They analyze customer purchasing patterns and product popularity to guide marketing strategies.
- The dataset helps them understand customer purchasing behavior, identify high-performing products, and evaluate which regions or categories may benefit from targeted marketing.
- Their goal is to design more effective marketing campaigns, improve customer targeting, and increase overall sales through data-informed strategies.

## Context

Some of the key questions that stakeholders seek to answer are:
- Which city/state is the primary revenue driver?
- Which categories are most profitable?
- Do certain months show cross-category growth, or is growth category-specific?
- Is the discount rate increasing, decreasing, or stable over the years? Do higher discount rates correspond with increased usage of certain payment methods?


## Start
You can download our repository code and follow through. Please start with the below.
```bash
python -m venv .venv
source .venv/bin/activate  # (Windows: .venv\Scripts\activate)
pip install -r requirements.txt
streamlit run app.py
```
