# BACKGROUND
There’s a Supermarket in US, lets say the name is PW Mart (fictional). They sell many products ranging from meats, fishs, fruits, sweets, liquors, even golds. They have severall channel of purchase. People can come through an offline store, web store, or catalog store. They also have membership for their customers. This way, they can record some personal data of customers.

Usually, Supermarket run campaigns to boost their sales and keep their customers engaged. Supermarket usually do a season / theme based campaign. They usually integrate discounted items into a campaign to highlight the concept of the campaign.

Over the last year, PW Mart held a series of campaign. They already run the campaign 6 times. They can’t really tell wheter the campaign is working well or not. They just run the campaign as it should be run. They already record the customers data based on their demographic, purchasing behavior, and participation in the campaign from their membership data for further analysis.

PW Mart feel that their campaign is running on auto-pilot. The participant seems stagnant and only catch small percentage of their total customers. They want to run the next campaign with more tailored strategy based on experience data.

Supermarket Campaign Team, the one in Marketing Division of PW Mart, they hire a Data Analyst to help them analyze the data they already gather for the last 2 years and design the base of their next campaign.
# PROBLEM
Let’s see what might be our problem first based on the given data.
![q1](https://github.com/user-attachments/assets/049d6ef8-3955-4b8e-9659-090771bcfef2)

As you can see, the campaign participation is so low. only 1 out of 5 people has participated, more over the participation rate is only 1.2x, which means most of the participant only participated 1 time during the 4 campaign. If you look at participation per campaign, it’s only 1 out of 13 people participated in each campaign.
# OBJECTIVE
To best formulate next campaign, we should should evaluate our campaign performance and compared to our data as general. By then, we might conclude and answer these key questions that shape a campaign:

1. Based on experience, evaluate campaign participations!
2. Based on demographics, what’s the best target audience?
3. Based on experience, is discount needed?
4. If needed, which products that should be discounted?
5. What channel of purchase should we integrate more in the campaign?
# ABOUT DATASET
After renaming the columns, here's a dictionary for you to take notes: 
### PEOPLE
* id: Customer's unique identifier
* birthYear: Customer's birth year
* education: Customer's education level
* statusMarital: Customer's marital status
* yearlyHouseIncome: Customer's yearly household income
* inHomeKid: Number of children in customer's household
* inHomeTeen: Number of teenagers in customer's household
* customerJoinDate: Date of customer's enrollment with the company
* daysLastPurchase: Number of days since customer's last purchase
* isComplain2Y: 1 if the customer complained in the last 2 years, 0 otherwise
### PRODUCT
* amountWines2Y: Amount spent on wine in last 2 years
* amountFruits2Y: Amount spent on fruits in last 2 years
* amountMeatProds2Y: Amount spent on meat in last 2 years
* amountFishProds2Y: Amount spent on fish in last 2 years
* amountSweetProds2Y: Amount spent on sweets in last 2 years
* amountGoldProds2Y: Amount spent on gold in last 2 years
### PROMOTION
* discPurchase: Number of purchases made with a discount
* isAcceptedCmp1: 1 if the customer accepted the offer in the 1st campaign, 0 otherwise
* isAcceptedCmp2: 1 if the customer accepted the offer in the 2nd campaign, 0 otherwise
* isAcceptedCmp3: 1 if the customer accepted the offer in the 3rd campaign, 0 otherwise
* isAcceptedCmp4: 1 if the customer accepted the offer in the 4th campaign, 0 otherwise
* isAcceptedCmp5: 1 if the customer accepted the offer in the 5th campaign, 0 otherwise
* isAcceptedCmpLast: 1 if the customer accepted the offer in the last campaign, 0 otherwise
### PLACE
* numWebPurchase: Number of purchases made through the company’s website
* numCatalogPurchase: Number of purchases made using a catalog
* numStorePurchase: Number of purchases made directly in stores
* numWebVisitsMonth: Number of visits to the company’s website in the last month
# DATA CLEANING 
Here are what I do in data cleaning:
### 1. Removed Duplicates
* Grouped rows by ID and filled missing values using ffill() and bfill().
* Removed duplicate rows, reducing from **3169 rows** to **2240 rows**.
### 2. Handled Missing Values
* Phone & Phone_Number: Merged columns.
* Month/Year Register: Filled using Registration_Time column.
* Payment Method: Filled based on purchase behavior.
* Income: Removed rows with missing values (1% of total).
### 3. Checked Logical Consistency
* Academic_Level: Merged "Master" and "2n Cycle".
* Living_With: Split into Status and Children.
* Invalid Promotion Data: Removed columns with incorrect values.
### 4. Removed Outliers
* Applied the **3-sigma** method to detect and remove outliers from numerical columns like Income and Vegetables.

For more details, please visit [here](https://github.com/lvbaotram/Campaign-Analysis/tree/main/Data%20Cleaning).
# EXPLORATORY DATA ANALYSIS
## 1. Demographic Analysis
I evaluate how the participation in each campaign and overall. I calculate:
* Proportion of the participation per demography
* Proportion of participation in whole campaigns
* Rate of participation per demography
* Rate of participation in whole campaigns
* Proportion of population per demography
* Discount analysis per demography and overall
* Channel of purchase per demography and overall
## 2. Using RFM for Customer Segmentation
![QQQ](https://github.com/user-attachments/assets/c36cd63a-9b8b-4529-bfb5-957efc25894d)

For more details, please visit [here](https://github.com/lvbaotram/Campaign-Analysis/tree/main/Exploratory%20Data%20Analysis).
## 3. Demographic Analysis Dashboard - PW Mart
This Power BI dashboard provides a comprehensive overview of customer demographic data for PW Mart. It visualizes key metrics and insights to help the business make data-driven decisions. 
### Goals
* Assist the management team in making informed decisions based on customer demographic data.
* Identify customer shopping trends across different demographic segments (generation, education level, payment method, etc.).
* Enhance marketing strategies and business development by understanding customer behavior.
  ![image](https://github.com/user-attachments/assets/734b3e05-d0d2-4c89-bb44-822137623607)
  
For more details, please visit [here](https://app.powerbi.com/groups/me/reports/7559dfbe-b5d2-4a5c-a7fd-41b9849bf907/e5cfc452f947b6acdfdc?experience=power-bi).
# CONCLUSION AND RECOMMENDATIONS
## Evaluation

Based on the demographic analysis (proportion and rate of participation), we know that the past campaigns focused more on:

- **Generation**: GenX
- **Education**: PhD
- **Marital Status**: Single
- **Economic Class**: Lower Middle Class
- **Family Status**: Not Family
  
Discount Analysis
* A discount might be needed because almost everyone has ever bought at a discount. However, the purchase ratio in total is small, at **16%**. This could be because the discounted items didn't match the needs of the consumers, only attracting the Working Class and Family, while the Working Class is not the highest population among other Economic Classes.

Channel of Purchase Analysis
* Despite demographic types, the most favored channel of purchase is **Store**, followed by **Web**.

RFM Analysis Insights
* **High-Value Segments**: Segments like `loyal_customers` and `potential_loyalists` are valuable for growth, while `champions` represent the highest value despite their smaller numbers.
* **At-Risk and Hibernating Segments**: These groups are significant in size, highlighting a need for targeted re-engagement strategies to reduce churn.
## Conclusion
We already know which demography classes is the best for audience targeting and how the last 5 campaigns went. We can conclude and recommend the PW Mart Marketing / Campaign Team to:

By making audience priority:

* Lower Middle Class (75%)
* Family (72%)
* Couple — Married (39%) and Together (26%) = (65%)
* Graduation (50%)
* Gen X (48%)
  
Integrates discount to campaign with items that meet the needs of top demography.

Boost campaign in Store. If budget is good, also boost on Web.

## Recommendation
* My main audience should be the **Lower Middle Class** with families (kids/teens at home). We can also include other demographic types like couples (Married and Together), Graduates, and Millennials to enhance our campaign.
* The discounted items should meet the needs of our primary audience, especially the **Lower Middle Class** with families (kids/teens at home).
* We should boost our campaign primarily in-store, then consider boosting it on our website as our secondary channel of purchase if budget permits.
* RFM-Based Actions
  * At Risk: Offer personalized discounts and send surveys to understand and resolve potential dissatisfaction. Focus on re-engagement to prevent customer loss.
  * Need Attention: Send targeted offers on fast-moving products and timely promotions to encourage quicker repeat purchases.
  * Potential Loyalists: Strengthen their connection with exclusive offers (e.g., free shipping) and personalized care to convert them into loyal customers.

