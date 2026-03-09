# Amazon Sales Dashboard

## Streamlit Dashboard
https://amazonsale1-2uku3ty6pxgg4ikfndbb58.streamlit.app

The ultimate goal is to create a dashboard that enables stakeholders to monitor key performance indicators (KPIs), identify growth opportunities, and detect operational bottlenecks.

## Audience

The stakeholders are the Global Sales & Operations Manager, Regional Marketing Leads, and Finance Manager. These users are responsible for monitoring performance across the different countries, allocating marketing budgets, setting discount thresholds, and recognizing underperforming categories in specific regions.  

## Data Set

The Amazon.csv data is retrieved from Kaggle (https://www.kaggle.com/datasets/rohiteng/amazon-sales-dataset)

The data set is synthetic, meaning it is not real but still intended to closely resemble real-world online retail behavior. Thus, the dataset is already very clean and well-structured. However, there are inconsistencies—particularly mismatches between the city/state and country fields. For example, entries such as “Austin, TX” are paired with a country like “Australia.” Because the city and state clearly correspond to U.S. locations, we removed the country column and focused the analysis solely on the U.S., where Amazon usage is strongest.


It contains 10,000 records of transactions, key features include:
- Geographic: City, State, and Country
- Product: Category, Product Name, and Brand
- Financial: Unit Price, Quantity, Discount, Total Amount
- Logistics: Order Status, Order Date, Payment Method

## Context

Some of the key questions that stakeholders seek to answer are:
- Which city/state is the primary revenue driver?
- Within those, which categories are most profitable?
- Do certain months show cross-category growth, or is growth category-specific?
- Is there a clear relationship between tax rate and sales volume?
- Is the discount rate increasing, decreasing, or stable over the years? Do higher discount rates correspond with increased usage of certain payment methods?

### Ethical Considerations

Since this is not real Amazon data, it may not fully reflect real-world conditions. Synthetic data is generated rather than observed so it can contain hidden biases or unrealistic patterns. Therefore, our group will clearly disclose that the dataset is synthetic and avoid presenting the findings as real business insights. Without this transparency, the analysis could mislead readers or decision-makers, especially since the dataset is not representative of all Amazon users or markets.

## Start
You can download our repository code and follow through. Please start with the below.
```bash
python -m venv .venv
source .venv/bin/activate  # (Windows: .venv\Scripts\activate)
pip install -r requirements.txt
streamlit run app.py
```
