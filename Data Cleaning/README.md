# BACKGROUND
There’s a Supermarket in US, lets say the name is PW Mart (fictional). They sell many products ranging from meats, fishs, fruits, sweets, liquors, even golds. They have severall channel of purchase. People can come through an offline store, web store, or catalog store. They also have membership for their customers. This way, they can record some personal data of customers.

Usually, Supermarket run campaigns to boost their sales and keep their customers engaged. Supermarket usually do a season / theme based campaign. They usually integrate discounted items into a campaign to highlight the concept of the campaign.

Over the last year, PW Mart held a series of campaign. They already run the campaign 6 times. They can’t really tell wheter the campaign is working well or not. They just run the campaign as it should be run. They already record the customers data based on their demographic, purchasing behavior, and participation in the campaign from their membership data for further analysis.

PW Mart feel that their campaign is running on auto-pilot. The participant seems stagnant and only catch small percentage of their total customers. They want to run the next campaign with more tailored strategy based on experience data.

Supermarket Campaign Team, the one in Marketing Division of PW Mart, they hire a Data Analyst to help them analyze the data they already gather for the last 2 years and design the base of their next campaign.
# PROBLEM
Let’s see what might be our problem first based on the given data.
![q1](https://github.com/user-attachments/assets/70bad66d-fc64-49fb-90ac-14b534dde1b2)

As you can see, the campaign participation is so low. only 1 out of 5 people has participated, more over the participation rate is only 1.2x, which means most of the participant only participated 1 time during the 4 campaign. If you look at participation per campaign, it’s only 1 out of 13 people participated in each campaign.
# OBJECTIVE
To best formulate next campaign, we should should evaluate our campaign performance and compared to our data as general. By then, we might conclude and answer these key questions that shape a campaign:

1. Based on experience, evaluate campaign participations!
2. Based on demographics, what’s the best target audience?
3. Based on experience, is discount needed?
4. If needed, which products that should be discounted?
5. What channel of purchase should we integrate more in the campaign?
# DATASET
Let's take a look into our dataset.
This is the version before data cleansing.

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ID</th>
      <th>Year_Of_Birth</th>
      <th>Academic_Level</th>
      <th>Income</th>
      <th>Registration_Time</th>
      <th>Recency</th>
      <th>Liquor</th>
      <th>Vegetables</th>
      <th>Pork</th>
      <th>Seafood</th>
      <th>...</th>
      <th>Promo_20</th>
      <th>Complain</th>
      <th>Gender</th>
      <th>Phone</th>
      <th>Phone_Number</th>
      <th>Year_Register</th>
      <th>Month_Register</th>
      <th>Total_Purchase</th>
      <th>Living_With</th>
      <th>Payment_Method</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>3064</th>
      <td>2801</td>
      <td>1990.0</td>
      <td>Basic</td>
      <td>20425.0</td>
      <td>29-10-2021</td>
      <td>5.0</td>
      <td>5.0</td>
      <td>14.0</td>
      <td>5.0</td>
      <td>3.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>Other</td>
      <td>8.414996e+10</td>
      <td>NaN</td>
      <td>2021.0</td>
      <td>10.0</td>
      <td>7.0</td>
      <td>Married_1</td>
      <td>Online</td>
    </tr>
    <tr>
      <th>3065</th>
      <td>8551</td>
      <td>1990.0</td>
      <td>PhD</td>
      <td>65295.0</td>
      <td>23-12-2022</td>
      <td>19.0</td>
      <td>366.0</td>
      <td>34.0</td>
      <td>117.0</td>
      <td>34.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>Female</td>
      <td>NaN</td>
      <td>8.409877e+10</td>
      <td>2022.0</td>
      <td>12.0</td>
      <td>20.0</td>
      <td>Single_0</td>
      <td>Cash</td>
    </tr>
    <tr>
      <th>3066</th>
      <td>7831</td>
      <td>1998.0</td>
      <td>Graduation</td>
      <td>31632.0</td>
      <td>14-07-2022</td>
      <td>92.0</td>
      <td>18.0</td>
      <td>10.0</td>
      <td>12.0</td>
      <td>11.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>Female</td>
      <td>8.431896e+10</td>
      <td>NaN</td>
      <td>2022.0</td>
      <td>7.0</td>
      <td>6.0</td>
      <td>Single_0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3067</th>
      <td>6426</td>
      <td>1994.0</td>
      <td>Master</td>
      <td>61794.0</td>
      <td>14-09-2022</td>
      <td>74.0</td>
      <td>265.0</td>
      <td>49.0</td>
      <td>188.0</td>
      <td>54.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>Male</td>
      <td>8.452917e+10</td>
      <td>NaN</td>
      <td>2022.0</td>
      <td>NaN</td>
      <td>20.0</td>
      <td>Married_1</td>
      <td>Mobile</td>
    </tr>
    <tr>
      <th>3068</th>
      <td>4950</td>
      <td>1983.0</td>
      <td>NaN</td>
      <td>75437.0</td>
      <td>09-11-2022</td>
      <td>25.0</td>
      <td>796.0</td>
      <td>2.0</td>
      <td>545.0</td>
      <td>95.0</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>Female</td>
      <td>NaN</td>
      <td>8.415671e+10</td>
      <td>2022.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Together_0</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 31 columns</p>

There are 31 rows and 3069 columns.
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Count</th>
      <th>Unique</th>
      <th>Null</th>
      <th>%Null</th>
      <th>DType</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>ID</th>
      <td>3069</td>
      <td>2240</td>
      <td>0</td>
      <td>0.00%</td>
      <td>int64</td>
    </tr>
    <tr>
      <th>Num_Deals_Purchases</th>
      <td>2841</td>
      <td>15</td>
      <td>228</td>
      <td>7.43%</td>
      <td>float64</td>
    </tr>
    <tr>
      <th>Candy</th>
      <td>2840</td>
      <td>177</td>
      <td>229</td>
      <td>7.46%</td>
      <td>float64</td>
    </tr>
    <tr>
      <th>Promo_10</th>
      <td>2834</td>
      <td>2</td>
      <td>235</td>
      <td>7.66%</td>
      <td>float64</td>
    </tr>
    <tr>
      <th>Total_Purchase</th>
      <td>2833</td>
      <td>39</td>
      <td>236</td>
      <td>7.69%</td>
      <td>float64</td>
    </tr>
    <tr>
      <th>Year_Of_Birth</th>
      <td>2832</td>
      <td>28</td>
      <td>237</td>
      <td>7.72%</td>
      <td>float64</td>
    </tr>
    <tr>
      <th>Promo_20</th>
      <td>2826</td>
      <td>2</td>
      <td>243</td>
      <td>7.92%</td>
      <td>float64</td>
    </tr>
    <tr>
      <th>Promo_30</th>
      <td>2826</td>
      <td>2</td>
      <td>243</td>
      <td>7.92%</td>
      <td>float64</td>
    </tr>
    <tr>
      <th>Num_Store_Purchases</th>
      <td>2826</td>
      <td>14</td>
      <td>243</td>
      <td>7.92%</td>
      <td>float64</td>
    </tr>
    <tr>
      <th>Registration_Time</th>
      <td>2824</td>
      <td>663</td>
      <td>245</td>
      <td>7.98%</td>
      <td>object</td>
    </tr>
    <tr>
      <th>Num_Web_Purchases</th>
      <td>2823</td>
      <td>15</td>
      <td>246</td>
      <td>8.02%</td>
      <td>float64</td>
    </tr>
    <tr>
      <th>Living_With</th>
      <td>2821</td>
      <td>23</td>
      <td>248</td>
      <td>8.08%</td>
      <td>object</td>
    </tr>
    <tr>
      <th>Promo_40</th>
      <td>2815</td>
      <td>3</td>
      <td>254</td>
      <td>8.28%</td>
      <td>float64</td>
    </tr>
    <tr>
      <th>Seafood</th>
      <td>2813</td>
      <td>182</td>
      <td>256</td>
      <td>8.34%</td>
      <td>float64</td>
    </tr>
    <tr>
      <th>Complain</th>
      <td>2813</td>
      <td>2</td>
      <td>256</td>
      <td>8.34%</td>
      <td>float64</td>
    </tr>
    <tr>
      <th>Num_Catalog_Purchases</th>
      <td>2811</td>
      <td>14</td>
      <td>258</td>
      <td>8.41%</td>
      <td>float64</td>
    </tr>
    <tr>
      <th>Vegetables</th>
      <td>2810</td>
      <td>158</td>
      <td>259</td>
      <td>8.44%</td>
      <td>float64</td>
    </tr>
    <tr>
      <th>Liquor</th>
      <td>2807</td>
      <td>776</td>
      <td>262</td>
      <td>8.54%</td>
      <td>float64</td>
    </tr>
    <tr>
      <th>Pork</th>
      <td>2806</td>
      <td>558</td>
      <td>263</td>
      <td>8.57%</td>
      <td>float64</td>
    </tr>
    <tr>
      <th>Recency</th>
      <td>2804</td>
      <td>100</td>
      <td>265</td>
      <td>8.63%</td>
      <td>float64</td>
    </tr>
    <tr>
      <th>Promo_50</th>
      <td>2801</td>
      <td>2</td>
      <td>268</td>
      <td>8.73%</td>
      <td>float64</td>
    </tr>
    <tr>
      <th>Academic_Level</th>
      <td>2799</td>
      <td>5</td>
      <td>270</td>
      <td>8.80%</td>
      <td>object</td>
    </tr>
    <tr>
      <th>Num_Web_Visits_Month</th>
      <td>2799</td>
      <td>16</td>
      <td>270</td>
      <td>8.80%</td>
      <td>float64</td>
    </tr>
    <tr>
      <th>Gender</th>
      <td>2794</td>
      <td>3</td>
      <td>275</td>
      <td>8.96%</td>
      <td>object</td>
    </tr>
    <tr>
      <th>Jewellery</th>
      <td>2792</td>
      <td>213</td>
      <td>277</td>
      <td>9.03%</td>
      <td>float64</td>
    </tr>
    <tr>
      <th>Income</th>
      <td>2782</td>
      <td>1974</td>
      <td>287</td>
      <td>9.35%</td>
      <td>float64</td>
    </tr>
    <tr>
      <th>Payment_Method</th>
      <td>2270</td>
      <td>4</td>
      <td>799</td>
      <td>26.03%</td>
      <td>object</td>
    </tr>
    <tr>
      <th>Month_Register</th>
      <td>2100</td>
      <td>12</td>
      <td>969</td>
      <td>31.57%</td>
      <td>float64</td>
    </tr>
    <tr>
      <th>Year_Register</th>
      <td>2084</td>
      <td>3</td>
      <td>985</td>
      <td>32.10%</td>
      <td>float64</td>
    </tr>
    <tr>
      <th>Phone</th>
      <td>1561</td>
      <td>1240</td>
      <td>1508</td>
      <td>49.14%</td>
      <td>float64</td>
    </tr>
    <tr>
      <th>Phone_Number</th>
      <td>1257</td>
      <td>1000</td>
      <td>1812</td>
      <td>59.04%</td>
      <td>float64</td>
    </tr>
  </tbody>
</table>

Here are what I do in data cleaning:
### 1. Duplicate Removing:
I also noticed that for the same customer ID, the number of observation rows can appear multiple times and contain many null attributes within the observation. However, these observation rows with null values compensate for each other (for example, if ID number 1017 is repeated 3 times but when the observation row with index 3000 of that ID has null values in the Liquor column, I can fill in the Liquor column values from the remaining 2 observation rows with indexes 16 and 1491 to replace it). Therefore, the team grouped these IDs and filled them according to the same rule. After that, the team will remove all duplicate rows existing in the dataframe.
```
# Grouping and filling null values
raw_df = raw_df.groupby('ID').apply(lambda group: group.ffill().bfill())

# Removing duplicate rows
raw_df = raw_df.drop_duplicates(subset='ID')
raw_df.shape
```
So the number of rows have reduced from 3069 columns in total to 2240. And the magic is...
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Count</th>
      <th>Unique</th>
      <th>Null</th>
      <th>%Null</th>
      <th>DType</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>ID</th>
      <td>2240</td>
      <td>2240</td>
      <td>0</td>
      <td>0.00%</td>
      <td>int64</td>
    </tr>
    <tr>
      <th>Total_Purchase</th>
      <td>2240</td>
      <td>39</td>
      <td>0</td>
      <td>0.00%</td>
      <td>float64</td>
    </tr>
    <tr>
      <th>Gender</th>
      <td>2240</td>
      <td>3</td>
      <td>0</td>
      <td>0.00%</td>
      <td>object</td>
    </tr>
    <tr>
      <th>Complain</th>
      <td>2240</td>
      <td>2</td>
      <td>0</td>
      <td>0.00%</td>
      <td>float64</td>
    </tr>
    <tr>
      <th>Promo_20</th>
      <td>2240</td>
      <td>2</td>
      <td>0</td>
      <td>0.00%</td>
      <td>float64</td>
    </tr>
    <tr>
      <th>Promo_10</th>
      <td>2240</td>
      <td>2</td>
      <td>0</td>
      <td>0.00%</td>
      <td>float64</td>
    </tr>
    <tr>
      <th>Promo_50</th>
      <td>2240</td>
      <td>2</td>
      <td>0</td>
      <td>0.00%</td>
      <td>float64</td>
    </tr>
    <tr>
      <th>Promo_40</th>
      <td>2240</td>
      <td>3</td>
      <td>0</td>
      <td>0.00%</td>
      <td>float64</td>
    </tr>
    <tr>
      <th>Promo_30</th>
      <td>2240</td>
      <td>2</td>
      <td>0</td>
      <td>0.00%</td>
      <td>float64</td>
    </tr>
    <tr>
      <th>Num_Web_Visits_Month</th>
      <td>2240</td>
      <td>16</td>
      <td>0</td>
      <td>0.00%</td>
      <td>float64</td>
    </tr>
    <tr>
      <th>Living_With</th>
      <td>2240</td>
      <td>23</td>
      <td>0</td>
      <td>0.00%</td>
      <td>object</td>
    </tr>
    <tr>
      <th>Num_Catalog_Purchases</th>
      <td>2240</td>
      <td>14</td>
      <td>0</td>
      <td>0.00%</td>
      <td>float64</td>
    </tr>
    <tr>
      <th>Num_Web_Purchases</th>
      <td>2240</td>
      <td>15</td>
      <td>0</td>
      <td>0.00%</td>
      <td>float64</td>
    </tr>
    <tr>
      <th>Num_Store_Purchases</th>
      <td>2240</td>
      <td>14</td>
      <td>0</td>
      <td>0.00%</td>
      <td>float64</td>
    </tr>
    <tr>
      <th>Jewellery</th>
      <td>2240</td>
      <td>213</td>
      <td>0</td>
      <td>0.00%</td>
      <td>float64</td>
    </tr>
    <tr>
      <th>Candy</th>
      <td>2240</td>
      <td>177</td>
      <td>0</td>
      <td>0.00%</td>
      <td>float64</td>
    </tr>
    <tr>
      <th>Seafood</th>
      <td>2240</td>
      <td>182</td>
      <td>0</td>
      <td>0.00%</td>
      <td>float64</td>
    </tr>
    <tr>
      <th>Pork</th>
      <td>2240</td>
      <td>558</td>
      <td>0</td>
      <td>0.00%</td>
      <td>float64</td>
    </tr>
    <tr>
      <th>Vegetables</th>
      <td>2240</td>
      <td>158</td>
      <td>0</td>
      <td>0.00%</td>
      <td>float64</td>
    </tr>
    <tr>
      <th>Liquor</th>
      <td>2240</td>
      <td>776</td>
      <td>0</td>
      <td>0.00%</td>
      <td>float64</td>
    </tr>
    <tr>
      <th>Recency</th>
      <td>2240</td>
      <td>100</td>
      <td>0</td>
      <td>0.00%</td>
      <td>float64</td>
    </tr>
    <tr>
      <th>Registration_Time</th>
      <td>2240</td>
      <td>663</td>
      <td>0</td>
      <td>0.00%</td>
      <td>object</td>
    </tr>
    <tr>
      <th>Num_Deals_Purchases</th>
      <td>2240</td>
      <td>15</td>
      <td>0</td>
      <td>0.00%</td>
      <td>float64</td>
    </tr>
    <tr>
      <th>Academic_Level</th>
      <td>2240</td>
      <td>5</td>
      <td>0</td>
      <td>0.00%</td>
      <td>object</td>
    </tr>
    <tr>
      <th>Year_Of_Birth</th>
      <td>2240</td>
      <td>28</td>
      <td>0</td>
      <td>0.00%</td>
      <td>float64</td>
    </tr>
    <tr>
      <th>Income</th>
      <td>2216</td>
      <td>1974</td>
      <td>24</td>
      <td>1.07%</td>
      <td>float64</td>
    </tr>
    <tr>
      <th>Payment_Method</th>
      <td>1794</td>
      <td>4</td>
      <td>446</td>
      <td>19.91%</td>
      <td>object</td>
    </tr>
    <tr>
      <th>Month_Register</th>
      <td>1667</td>
      <td>12</td>
      <td>573</td>
      <td>25.58%</td>
      <td>float64</td>
    </tr>
    <tr>
      <th>Year_Register</th>
      <td>1660</td>
      <td>3</td>
      <td>580</td>
      <td>25.89%</td>
      <td>float64</td>
    </tr>
    <tr>
      <th>Phone</th>
      <td>1240</td>
      <td>1240</td>
      <td>1000</td>
      <td>44.64%</td>
      <td>float64</td>
    </tr>
    <tr>
      <th>Phone_Number</th>
      <td>1000</td>
      <td>1000</td>
      <td>1240</td>
      <td>55.36%</td>
      <td>float64</td>
    </tr>
  </tbody>
</table>

The number of attribute that contained null value decreased from 30 columns to only 6 columns. In order to understand easier, we using plotly to draw some interactable charts.
![image](https://github.com/user-attachments/assets/51a3fe94-aa9e-4c37-bdd1-20eb390644b2)

### 2. Null cleaning:
Based on the chart above, I noticed that **whenever the `Phone` column has a value, the `Phone_Number` column loses its value**. Therefore, I will combine these two columns together.
I convert the `Register_Time` to datetime format and then fills missing values in `Month_Register` and `Year_Register` columns based on the respective month and year from the main datetime column.
Handling null values of `Payment_Method`:

* If 'Num_Web_Purchases' > 'Num_Store_Purchases' then it is an `Online` payment method.
* Otherwise, it is `Cash` payment method.
Last but not least is the `Income` columns.

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Count</th>
      <th>Unique</th>
      <th>Null</th>
      <th>%Null</th>
      <th>DType</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Income</th>
      <td>2216</td>
      <td>1974</td>
      <td>24</td>
      <td>1.07%</td>
      <td>float64</td>
    </tr>
  </tbody>
</table>

![image](https://github.com/user-attachments/assets/fd726334-5019-4d4b-9bbd-3b837eb3f1e2)

Because **the number of null values in this column is very low** (only 1% compared to the total number of rows), I decide to **delete these rows** to avoid incorrectly replacing values and affecting the distribution of the attribute.

**All cleaned ...**
### 3. Logical Checking
Although the dataframe is now cleaned from null values, we cannot be certain that no erroneous values have been "secretly" assigned to the dataset. Therefore, I will check the logical consistency of the data columns to ensure correctness before proceeding to the outlier preprocessing stage.
> First, in the `Academic_Level` column, "Master" and "2n Cycle" have the same meaning, so they will be merged into "Master".
> Second. In the Living_With column, marital status and number of children are combined, so we will separate them into a column Status for marital status and Children for the number of children.
> After that, we redefine the "Status" into 5 states: 'Married', 'Together', 'Single' (Single & Alone), 'Divorced', 'Widow'.
> Lastly, I noticed that in the promotion-related categorical variables, some data rows contain the value "-1" even though the data type of the column is boolean. Therefore, we will check which columns contain this value.
 ![image](https://github.com/user-attachments/assets/b038bef7-44f9-4052-917b-10bd9a8d156d)

And because the number of "-1" values in this column is too high compared to the total number of rows, combined with the fact that when comparing correlation heatmaps, this column does not show strong correlations with any other columns. Therefore, I have decided to drop this column.
### 4. Outliers removing
In outlier processing, there are typically two main approaches: the **Interquartile Range (IQR) method** and the **3-sigma method**. Each method offers a distinct approach to identifying and handling outliers within a dataset. 
Here, I will use the 3-sigma method.

##### **3-sigma method for removing outliers**:

The 3-sigma method, also known as the three standard deviation rule, identifies outliers by considering data points that lie outside of three standard deviations from the mean.

1. Calculate the mean (μ) and standard deviation (σ) of the dataset.
2. Define the upper and lower bounds for outliers:
   - Upper bound: μ + 3σ
   - Lower bound: μ - 3σ
3. Remove any data points that fall outside of these bounds, as they are considered outliers.
```
# Calculating limit of all columns in dataframe 
mean_values = df2[outliers_chk_col_lst].mean()
std_values = df2[outliers_chk_col_lst].std(ddof=1)
uplim_values = mean_values + 3 * std_values
lowlim_values = mean_values - 3 * std_values

# Initialize an empty dictionary to store the outliers count for each column
outliers_3s = {}  
for col in outliers_chk_col_lst:
    outliers_3s[col] = len(df2[(df2[col] > uplim_values[col]) | (df2[col] < lowlim_values[col])])

# Show results
for col, count in outliers_3s.items():
    print(f'Col {col}: {count} outliers')
```
Col Income: 8 outliers
Col Recency: 0 outliers
Col Liquor: 15 outliers
Col Vegetables: 64 outliers
Col Pork: 39 outliers
Col Seafood: 57 outliers
Col Candy: 61 outliers
Col Jewellery: 46 outliers
Col Num_Deals_Purchases: 31 outliers
Col Num_Web_Purchases: 3 outliers
Col Num_Catalog_Purchases: 4 outliers
Col Num_Store_Purchases: 0 outliers
Col Num_Web_Visits_Month: 9 outliers
Col Total_Purchase: 3 outliers
Col Age: 0 outliers

Visualizing all numeric columns by boxplot
![image](https://github.com/user-attachments/assets/f9eb5d5a-70fc-4bac-85f2-0d318a941eba)

```
# Perform removing outliers
for col in outliers_chk_col_lst:
    mean = df2[col].mean()
    std = df2[col].std(ddof=1)
    uplim = mean + 3 * std
    lowlim = mean - 3 * std
    # values out of 2 limits = OUT!
    outliers_col = df2[col][(df2[col] < lowlim) | (df2[col] > uplim)]
    index_outliers_col = list(outliers_col.index)
    df2.drop(index_outliers_col, axis=0, inplace=True)
```
Visualizing all numeric columns again after removing outliers
![image](https://github.com/user-attachments/assets/739ac467-0786-48b3-a732-2d66b81bc185)
This is the version after data cleansing:
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>ID</th>
      <th>Year_Of_Birth</th>
      <th>Academic_Level</th>
      <th>Income</th>
      <th>Registration_Time</th>
      <th>Recency</th>
      <th>Liquor</th>
      <th>Vegetables</th>
      <th>Pork</th>
      <th>Seafood</th>
      <th>...</th>
      <th>Complain</th>
      <th>Gender</th>
      <th>Phone</th>
      <th>Year_Register</th>
      <th>Month_Register</th>
      <th>Total_Purchase</th>
      <th>Payment_Method</th>
      <th>Age</th>
      <th>Status</th>
      <th>Children</th>
    </tr>
    <tr>
      <th>ID</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
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
      <th>1001</th>
      <th>831</th>
      <td>1001</td>
      <td>1994</td>
      <td>Graduation</td>
      <td>61074.0</td>
      <td>2021-08-17</td>
      <td>37</td>
      <td>790.0</td>
      <td>2.0</td>
      <td>133.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0</td>
      <td>Other</td>
      <td>8.412036e+10</td>
      <td>2021</td>
      <td>8</td>
      <td>31</td>
      <td>Card</td>
      <td>30.0</td>
      <td>Married</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1002</th>
      <th>1132</th>
      <td>1002</td>
      <td>1989</td>
      <td>Graduation</td>
      <td>60093.0</td>
      <td>2022-06-26</td>
      <td>92</td>
      <td>503.0</td>
      <td>14.0</td>
      <td>109.0</td>
      <td>16.0</td>
      <td>...</td>
      <td>0</td>
      <td>Male</td>
      <td>8.494833e+10</td>
      <td>2022</td>
      <td>6</td>
      <td>21</td>
      <td>Mobile</td>
      <td>35.0</td>
      <td>Married</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1005</th>
      <th>301</th>
      <td>1005</td>
      <td>1978</td>
      <td>Master</td>
      <td>79689.0</td>
      <td>2022-05-12</td>
      <td>65</td>
      <td>312.0</td>
      <td>28.0</td>
      <td>640.0</td>
      <td>180.0</td>
      <td>...</td>
      <td>0</td>
      <td>Female</td>
      <td>8.444028e+10</td>
      <td>2022</td>
      <td>5</td>
      <td>27</td>
      <td>Online</td>
      <td>46.0</td>
      <td>Single</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1006</th>
      <th>1101</th>
      <td>1006</td>
      <td>1987</td>
      <td>Master</td>
      <td>41021.0</td>
      <td>2021-12-30</td>
      <td>12</td>
      <td>15.0</td>
      <td>9.0</td>
      <td>9.0</td>
      <td>6.0</td>
      <td>...</td>
      <td>0</td>
      <td>Female</td>
      <td>8.494006e+10</td>
      <td>2021</td>
      <td>12</td>
      <td>7</td>
      <td>Online</td>
      <td>37.0</td>
      <td>Together</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1008</th>
      <th>1948</th>
      <td>1008</td>
      <td>1996</td>
      <td>PhD</td>
      <td>75032.0</td>
      <td>2022-04-28</td>
      <td>74</td>
      <td>953.0</td>
      <td>14.0</td>
      <td>180.0</td>
      <td>47.0</td>
      <td>...</td>
      <td>0</td>
      <td>Female</td>
      <td>8.451825e+10</td>
      <td>2022</td>
      <td>4</td>
      <td>20</td>
      <td>Cash</td>
      <td>28.0</td>
      <td>Married</td>
      <td>1</td>
    </tr>
    <tr>
      <th>...</th>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>9980</th>
      <th>110</th>
      <td>9980</td>
      <td>1992</td>
      <td>Graduation</td>
      <td>22010.0</td>
      <td>2022-06-30</td>
      <td>51</td>
      <td>12.0</td>
      <td>4.0</td>
      <td>9.0</td>
      <td>3.0</td>
      <td>...</td>
      <td>0</td>
      <td>Male</td>
      <td>8.464713e+10</td>
      <td>2022</td>
      <td>6</td>
      <td>7</td>
      <td>Online</td>
      <td>32.0</td>
      <td>Together</td>
      <td>1</td>
    </tr>
    <tr>
      <th>9985</th>
      <th>1920</th>
      <td>9985</td>
      <td>1986</td>
      <td>Graduation</td>
      <td>38361.0</td>
      <td>2022-12-27</td>
      <td>74</td>
      <td>40.0</td>
      <td>2.0</td>
      <td>56.0</td>
      <td>20.0</td>
      <td>...</td>
      <td>0</td>
      <td>Female</td>
      <td>8.447441e+10</td>
      <td>2022</td>
      <td>12</td>
      <td>10</td>
      <td>Cash</td>
      <td>38.0</td>
      <td>Together</td>
      <td>1</td>
    </tr>
    <tr>
      <th>9986</th>
      <th>2315</th>
      <td>9986</td>
      <td>1990</td>
      <td>Graduation</td>
      <td>56628.0</td>
      <td>2023-03-21</td>
      <td>30</td>
      <td>480.0</td>
      <td>7.0</td>
      <td>82.0</td>
      <td>7.0</td>
      <td>...</td>
      <td>0</td>
      <td>Male</td>
      <td>8.489301e+10</td>
      <td>2023</td>
      <td>3</td>
      <td>20</td>
      <td>Mobile</td>
      <td>34.0</td>
      <td>Single</td>
      <td>1</td>
    </tr>
    <tr>
      <th>9990</th>
      <th>1903</th>
      <td>9990</td>
      <td>1993</td>
      <td>Graduation</td>
      <td>75330.0</td>
      <td>2021-10-04</td>
      <td>94</td>
      <td>556.0</td>
      <td>84.0</td>
      <td>257.0</td>
      <td>93.0</td>
      <td>...</td>
      <td>0</td>
      <td>Other</td>
      <td>8.457901e+10</td>
      <td>2021</td>
      <td>10</td>
      <td>29</td>
      <td>Online</td>
      <td>31.0</td>
      <td>Married</td>
      <td>2</td>
    </tr>
    <tr>
      <th>9997</th>
      <th>1054</th>
      <td>9997</td>
      <td>1994</td>
      <td>Graduation</td>
      <td>56243.0</td>
      <td>2022-12-30</td>
      <td>26</td>
      <td>348.0</td>
      <td>2.0</td>
      <td>35.0</td>
      <td>4.0</td>
      <td>...</td>
      <td>0</td>
      <td>Male</td>
      <td>8.410226e+10</td>
      <td>2022</td>
      <td>12</td>
      <td>20</td>
      <td>Online</td>
      <td>30.0</td>
      <td>Single</td>
      <td>3</td>
    </tr>
  </tbody>
</table>
<p>2240 rows × 31 columns</p>

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
