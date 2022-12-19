# PDA_CA1
Programming for Data Analytics assignment 2

1) Primary objective: To design and develop a Data Acquisition and Preprocessing Pipeline.

2) Details of assignment brief 
3) Assessment Task (30%):

4) You are required to develop a Data Acquisition and Preprocessing Pipeline of your choice, including data acquisition (API, Web scraping, DB Extract etc.), Extraction of features and Transformations as appropriate, followed by loading into an appropriate database. The focus of the complexity of the pipeline is your choice.
Use Git (e.g. GitHub / Colab) and commit/pin version regularly.

5) GitHub/GitLab/Colab MUST be used for this project to develop both the artefact and documentation, and any code or material uploaded as a fait accompli will not be credited. Furthermore, any such code not attributed or presented contrary to its originating licence will be the subject of Academic Impropriety investigations.
6) If using Colab, it must be shared with your lecturer's @dbs.ie email address as editor, and documentation should be as text cells in line with the code. If using Git, documentation must be in the form of a text document (README.md / HTML / LaTeX) inside the git repository, and the repository must be public
7) The repository must be regularly active from week 7.
8) The documentation must contain a link to the repository itself, and the repository should be downloaded and submitted on the Moodle link

# Report
In this assignment I have set up a GitHub repository to commit all the code in the project to.
This Repository can be found at: https://www.github.com/DhanushVinayUttarkar/PDA_CA1

This project can be divided into mainly 3 parts:
1. Fetching the data using an API and storing it in a csv file
2. Storing the dataset from the csv file, storing it into a dataframe and processing.
3. Creating a database, collection, storing data into the database and then performing some database operations.

### Fetching the data using an API and storing it in a csv file
In this step we fetch apple's time series data from the alpha-vantage api provided by rapid api. we then store that data into a csv file called "Time_Series_Stock_data.csv"

### Storing the dataset from the csv file, storing it into a dataframe and processing.
In this part we fetch the data from the csv file and store it in a dataframe. We then perform a milling value check for the opening, closing, high and low values by plotting a graph. 

### Creating a database, collection, storing data into the database and then performing some database operations.
Here we connect to the cluster we created on mongodb using '_MongoClient_', we then create a database called '_stockmarket_timeseries_' after which we create a cluster called '_Apple_stock_'.
Next we fetch the data into a dataframe and then convert the dataframe into a dictionary with proper indexing and store that data into the mongodb database.

### Questions:
<p>
1) what type of data is this and what can it be used for?

A: This is a time series data where we need to predict future values, depending on a given period on time the model is trained on. This can be solved using models like an ARIMA (autoregressive integrated moving average) model and a few others.
</p>

<p>
2) What can we do to pre-process the data?

A: To pre-process this type of data we usually check for missing/null values and replace them with the mean of that respective column or the required value depending on the column.
in this project we have plotted a graph to check for null values, and we can see that the dataset does not contain any. We can also convert any non-numeric data to numeric and date and time to the date-time format to make it easier to use.
</p>

<p>
3) Can we fetch a value at a particular index value from the database?

A:yes we can, this is demonstrated in the code and the result we got was 
"_The value in collection at index 3 is: {'_id': ObjectId('63a011fbe1245502ca86ded1'), 'index': 3, 'timestamp': datetime.datetime(2022, 9, 30, 0, 0), 'open': 156.64, 'high': 164.26, 'low': 138.0, 'close': 138.2, 'volume': 2083968147}_"

which matches with the value at index 3 in the database.
</p>

<p>
4) Can we check which has the largest value in the open and closing?

A: The code demonstrates the largest opening and closing values to be
"_The largest value at low in the collection is: {'_ _id': ObjectId('63a01902282300e46ae4c2fb'), 'index': 122, 'timestamp': datetime.datetime(2012, 10, 31, 0, 0), 'open': 671.5, 'high': 676.75, 'low': 587.7, 'close': 595.32, 'volume': 433672500}_"

and

"_The largest value at high in the collection is: {'_ _id': ObjectId('63a01902282300e46ae4c2fc'), 'index': 123, 'timestamp': datetime.datetime(2012, 9, 28, 0, 0), 'open': 665.76, 'high': 705.07, 'low': 656.0, 'close': 667.105, 'volume': 328535900}_"

respectively.

This is done by arranging the data in descending order using the sort function and then 
using the limit function to pick the first value hence displaying the largest value.
As we can see the larges opening value is "**671.5**" located at index **122** and 
the largest closing value is "**667.105**" located at index **123**
</p>
