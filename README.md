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
Next, let’s take a look at each demographical analysis. Let’s take a look into it by analyzing proportion of population per demography, proportion per demography per campaign, participation rates per demography, and interest of participation per campaign.

# DATA ANALYSIS: CAMPAIGN TOOLS
# CONCLUSION AND RECOMMENDATION
