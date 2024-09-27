# DATA ANALYSIS: DEMOGRAPHY
#### Which campaign is successfull the most?
![image](https://github.com/user-attachments/assets/99ec042b-9370-4784-96f0-6d07294d3e4c)

If we look closely in participated customers number, there's a hope that this campaigns could work better next time. In the **3rd** campaigns, we see a significance rise in participants, doubles the last and overall past campaigns participants.

To best formulate next campaign, we should design the campaign carefully based our evaluation of past campaigns.

We should see what might happened in last campaign to formulate next campaigns. And also, looks at **2nd** and **5th** campaigns that failed to gather participants, so we're not repeating same mistake in next campaigns.

Based on our given data, we can see the demographics for potential target audience, so many will participate in next campaign.

Next, let’s take a look at each demographical analysis. Let’s take a look into it by analyzing proportion of population per demography, proportion per demography per campaign, participation rates per demography, and interest of participation per campaign.

![q2](https://github.com/user-attachments/assets/9edb64dd-0892-43f1-bc03-8dfef31c3a1d)

![Q3](https://github.com/user-attachments/assets/4189e3bd-4323-43e2-b047-53b8244687b4)

![q4](https://github.com/user-attachments/assets/ac319d94-5e9f-4f80-b96c-a96c715dc83a)

![q10](https://github.com/user-attachments/assets/2526caef-69ef-452f-8bf0-e276b21b2887)

![q11](https://github.com/user-attachments/assets/b9e2eb16-968f-4f72-b088-ef387e77e616)

From graphs above, we can see that participation per campaign takes interest in some demographic class (right top graph).

Campaign was more focused on:

Generation: Gen X
Education: PhD
Marital: Married
Economic Class: Lower Middle Class
Family: Not Family
We can also see which class has higher population per demography as listed below.

Highest Population:

Millennials (89.2%)
Graduation (50.4%)
Married (38.6%) and Together (25.9%) = (64.5%)
Lower Middle Class (74.9%)
Family (71.6%)

## DEMOGRAPHY CORRELATION TEST
```
dictComb = {'combination' : [],
            'countN' : []}

for i in df['Generation'].unique() :
    for k in df['Academic_Level'].unique() :
        for m in df['Status'].unique() :
            for n in df['ecoClass'].unique() :
                for o in df['isChildren'].unique() :
                    countN = df[(df['Generation'] == i)
                                    & (df['Academic_Level'] == k)
                                    & (df['Status'] == m)
                                    & (df['ecoClass'] == n)
                                    & (df['isChildren'] == o)]['ID'].count()
                    for p in dictComb :
                        if p == 'combination' :
                            dictComb[p].append([i , k , m , n , o])
                        else :
                            dictComb[p].append(countN)

dfComb = pd.DataFrame(dictComb)
dfComb.sort_values('countN', ascending=False)
```
![image](https://github.com/user-attachments/assets/8cbfe2c2-de91-4f3e-a684-accd1eb4b03b)


**If we get all the highest demographics combined, we only get 198 People at max**

So, it better to make hierarchy or priority which Demography we should focus on more.

But, still the higest demography combined match the result from analysis per demography.

The priority should follow:

1. Millennials (89.2%)
2. Graduation (50.4%)
3. Married (38.6%) and Together (25.9%) = (64.5%)
4. Lower Middle Class (74.9%)
5. Family (71.6%)

We can see in the right-side graph, that if the population is higher, the participant is also higher. It means we should target higher population to get more participant for 6th campaign. But if we try to calculate sample based on all highest class per demography combined, we only get **198 people at max**. It means the demography class should not be treated equal, but with priority.
# DATA ANALYSIS: CAMPAIGN TOOLS
We should take a look at other matrix to help enhance the campaign, we can analyze discount and channel as tools to help boosting the campaign performance.
## DISCOUNT ANALYSIS
![Q12](https://github.com/user-attachments/assets/ff5492eb-d505-4577-8974-eed50a549ec4)

From graphs above we can conclude that almost everyone has ever bought in discount but the rate of purchase is quite small, only 1 out of 6 purchases. Discount is a good tool to attract participants but should meet needs of top demography.
## CHANNEL OF PURCHASE
From graphs above we can conclude that almost everyone has bought from Store and Web. All favored Store as main channel of purchase. Store is the best channel of purchase followed by Web.
## RFM ANALTSIS FOR CUSTOMER SEGMENTATION
##### What is RFM? and Why it is used for?

RFM stands for Recency, Frequency, and Monetary value, which is a popular method used in marketing and customer relationship management (CRM) to analyze and segment customers based on their purchasing behavior.
![RFM](https://github.com/user-attachments/assets/0c22093f-cc9f-4f00-b8fe-2ec85f6f3974)

**The RFM model evaluates customers based on three key metrics:**

*Recency:* How recently a customer has made a purchase

*Frequency:* How frequently a customer makes purchases

*Monetary Value:* How much a customer spends on purchases

* RFM analysis assigns each customer a score for each of these metrics, which are then used to segment customers into groups based on their overall score.
* This segmentation helps businesses identify which customers are most valuable and should receive priority attention, and which customers are less valuable and may require less attention or targeted marketing efforts.
##### By using RFM Analysis:
* Businesses can develop targeted marketing strategies for each customer segment.
* Improve customer retention.
* Increase overall revenue by focusing on their most valuable customers.
Now let's us use RFM for Campaign Marketing dataset.
1. Calculating RFM Metrics
```
# Recency
rfm['Recency'] = df['Recency']
# Frequency
rfm['Frequency'] = df['Num_Deals_Purchases'] + df['Num_Catalog_Purchases'] + df['Num_Store_Purchases'] + df['Num_Web_Purchases']
# Monetary
rfm['Monetary'] = df['Liquor'] + df['Vegetables'] + df['Pork'] + df['Seafood'] + df['Candy'] + df['Jewellery']
```
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Recency</th>
      <th>Frequency</th>
      <th>Monetary</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>37.0</td>
      <td>31.0</td>
      <td>1105.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>92.0</td>
      <td>21.0</td>
      <td>738.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>65.0</td>
      <td>27.0</td>
      <td>1318.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>12.0</td>
      <td>7.0</td>
      <td>67.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>55.0</td>
      <td>33.0</td>
      <td>1665.0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>2231</th>
      <td>51.0</td>
      <td>7.0</td>
      <td>36.0</td>
    </tr>
    <tr>
      <th>2232</th>
      <td>74.0</td>
      <td>10.0</td>
      <td>140.0</td>
    </tr>
    <tr>
      <th>2233</th>
      <td>30.0</td>
      <td>20.0</td>
      <td>764.0</td>
    </tr>
    <tr>
      <th>2234</th>
      <td>94.0</td>
      <td>29.0</td>
      <td>1112.0</td>
    </tr>
    <tr>
      <th>2235</th>
      <td>26.0</td>
      <td>20.0</td>
      <td>399.0</td>
    </tr>
  </tbody>
</table>
<p>2236 rows × 3 columns</p>

2. Calculating RFM Scores
```
rfm_df = rfm.copy()
rfm_df.loc[:, 'recency_score'] = pd.qcut(rfm_df['Recency'], 5, labels=[5, 4, 3, 2, 1])
rfm_df.loc[:, 'frequency_score'] = pd.qcut(rfm_df['Frequency'], 5, labels=[1, 2, 3, 4, 5])
rfm_df.loc[:, 'monetary_score'] = pd.qcut(rfm_df['Monetary'], 5, labels=[1, 2, 3, 4, 5])
rfm_df.loc[:, 'RFM_SCORE'] = (rfm_df['recency_score'].astype(str) + rfm_df['frequency_score'].astype(str))
```
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Recency</th>
      <th>Frequency</th>
      <th>Monetary</th>
      <th>recency_score</th>
      <th>frequency_score</th>
      <th>monetary_score</th>
      <th>RFM_SCORE</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>37.0</td>
      <td>31.0</td>
      <td>1105.0</td>
      <td>4</td>
      <td>5</td>
      <td>4</td>
      <td>45</td>
    </tr>
    <tr>
      <th>1</th>
      <td>92.0</td>
      <td>21.0</td>
      <td>738.0</td>
      <td>1</td>
      <td>4</td>
      <td>4</td>
      <td>14</td>
    </tr>
    <tr>
      <th>2</th>
      <td>65.0</td>
      <td>27.0</td>
      <td>1318.0</td>
      <td>2</td>
      <td>5</td>
      <td>5</td>
      <td>25</td>
    </tr>
    <tr>
      <th>3</th>
      <td>12.0</td>
      <td>7.0</td>
      <td>67.0</td>
      <td>5</td>
      <td>1</td>
      <td>2</td>
      <td>51</td>
    </tr>
    <tr>
      <th>4</th>
      <td>55.0</td>
      <td>33.0</td>
      <td>1665.0</td>
      <td>3</td>
      <td>5</td>
      <td>5</td>
      <td>35</td>
    </tr>
  </tbody>
</table>

3. Creating & Analysing RFM Segments
```
# Clusters by RFM Score
seg_map = {
    r'[1-2][1-2]': 'hibernating',
    r'[1-2][3-4]': 'at_Risk',
    r'[1-2]5': 'cant_loose',
    r'3[1-2]': 'about_to_sleep',
    r'33': 'need_attention',
    r'[3-4][4-5]': 'loyal_customers',
    r'41': 'promising',
    r'51': 'new_customers',
    r'[4-5][2-3]': 'potential_loyalists',
    r'5[4-5]': 'champions'
}
# Performing calculations
rfm_df.loc[:,'segment'] = rfm_df['RFM_SCORE'].replace(seg_map, regex=True)
rfm_df[['segment', 'Recency', 'Frequency', 'Monetary']].groupby('segment').agg(['mean', 'count'])
```
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th colspan="2" halign="left">Recency</th>
      <th colspan="2" halign="left">Frequency</th>
      <th colspan="2" halign="left">Monetary</th>
    </tr>
    <tr>
      <th></th>
      <th>mean</th>
      <th>count</th>
      <th>mean</th>
      <th>count</th>
      <th>mean</th>
      <th>count</th>
    </tr>
    <tr>
      <th>segment</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>about_to_sleep</th>
      <td>49.377049</td>
      <td>183</td>
      <td>6.852459</td>
      <td>183</td>
      <td>80.338798</td>
      <td>183</td>
    </tr>
    <tr>
      <th>at_Risk</th>
      <td>78.586842</td>
      <td>380</td>
      <td>17.465789</td>
      <td>380</td>
      <td>880.692105</td>
      <td>380</td>
    </tr>
    <tr>
      <th>cant_loose</th>
      <td>80.062893</td>
      <td>159</td>
      <td>25.981132</td>
      <td>159</td>
      <td>1208.918239</td>
      <td>159</td>
    </tr>
    <tr>
      <th>champions</th>
      <td>9.267857</td>
      <td>168</td>
      <td>22.952381</td>
      <td>168</td>
      <td>1072.773810</td>
      <td>168</td>
    </tr>
    <tr>
      <th>hibernating</th>
      <td>80.162319</td>
      <td>345</td>
      <td>7.031884</td>
      <td>345</td>
      <td>86.857971</td>
      <td>345</td>
    </tr>
    <tr>
      <th>loyal_customers</th>
      <td>39.849432</td>
      <td>352</td>
      <td>23.181818</td>
      <td>352</td>
      <td>1118.639205</td>
      <td>352</td>
    </tr>
    <tr>
      <th>need_attention</th>
      <td>50.141176</td>
      <td>85</td>
      <td>14.929412</td>
      <td>85</td>
      <td>654.764706</td>
      <td>85</td>
    </tr>
    <tr>
      <th>new_customers</th>
      <td>9.491525</td>
      <td>118</td>
      <td>5.381356</td>
      <td>118</td>
      <td>50.703390</td>
      <td>118</td>
    </tr>
    <tr>
      <th>potential_loyalists</th>
      <td>19.014837</td>
      <td>337</td>
      <td>12.646884</td>
      <td>337</td>
      <td>441.142433</td>
      <td>337</td>
    </tr>
    <tr>
      <th>promising</th>
      <td>29.669725</td>
      <td>109</td>
      <td>5.357798</td>
      <td>109</td>
      <td>42.422018</td>
      <td>109</td>
    </tr>
  </tbody>
</table>

![image](https://github.com/user-attachments/assets/67b76ff4-0d2e-474b-b1da-3612bbea5906)

![newplot](https://github.com/user-attachments/assets/73bfc8e3-a956-4529-8b14-0e241d95d875)

#### At Risk

This group made their last purchase an average of 78.59 days ago. The group has an average shopping frequency of 17.47 times, and the average total spend is 880.69 units. The time since their last purchase is quite long, so these customers may be at risk of being lost.

Strategy:

* Investigate why these customers have not shopped in a long time, possibly due to dissatisfaction.
* Send a survey via email to check their shopping experience.
* If there is no dissatisfaction, send reminders and offer discount codes to encourage them to shop again.
#### Need Attention

This group made their last purchase an average of 50.14 days ago, with an average shopping frequency of 14.93 times, and the average spend is 654.76 units.

Strategy:

* Focus on offering products that have faster consumption rates, based on what these customers usually buy.
* Provide special promotions or discounts to encourage them to come back sooner.
* This approach could help shorten the time between purchases and increase shopping frequency.
#### Potential Loyalists

This group made their last purchase an average of 19.01 days ago, with an average shopping frequency of 12.65 times, and the average spend is 441.14 units.

Strategy:

* Closely monitor these customers and increase their satisfaction through personalized phone calls.
* Offer promotions such as free shipping to increase the average spend per order.
* With the right support, these customers could become loyal customers.
