>**Note**: Please **fork** the current Udacity repository so that you will have a **remote** repository in **your** Github account. Clone the remote repository to your local machine. Later, as a part of the project "Post your Work on Github", you will push your proposed changes to the remote repository in your Github account.

### Date created
July 3rd, 2021
07/03/2021

### Project Title
Explore US Bikeshare Data: Identify trends in sharing bikes across NYC, Chicago, and Washington

### Description
In this project, I wrote Python code to import US bike share data and answer interesting questions about it by computing descriptive statistics. I also wrote a script that takes in raw input to create an interactive experience in the terminal to present these statistics.

### Files used
chicago.csv
new_york_city.csv
washington.csv

### Credits
External Articles Referenced:

  How to Indefinitely Request User Input Until Valid in Python
  Link: https://betterprogramming.pub/how-to-indefinitely-request-user-input-until-valid-in-python-388a7c85aa6e

  Syntax Error: EOL while scanning string literal
  https://www.askpython.com/python/syntax-error-eol-while-scanning-string-literal

  pandas.to_datetime
  https://pandas.pydata.org/docs/reference/api/pandas.to_datetime.html

  pandas.DataFrame.mode
  https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.mode.html

  Pandas DataFrame: sum() function
  https://www.w3resource.com/pandas/dataframe/dataframe-sum.php

  pandas.DataFrame.mean
  https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.mean.html

  pandas.Series.value_counts
  https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.value_counts.html

  Python KeyError Exceptions and How to Handle Them
  https://realpython.com/python-keyerror/

  Python | Extracting rows using Pandas .iloc[]
  https://www.geeksforgeeks.org/python-extracting-rows-using-pandas-iloc/

  Trouble displaying raw data
  https://knowledge.udacity.com/questions/58280

Course Resources Referenced:

  Practice Problem #1: Compute the Most Popular Start Hour
  Use pandas to load chicago.csv into a dataframe, and find the most frequent hour when people start traveling. There isn't an hour column in this dataset, but you can create one by extracting the hour from the "Start Time" column. To do this, you can convert "Start Time" to the datetime datatype using the pandas to_datetime() method and extracting properties such as the hour with these properties.

  Practice Problem #3: Load and Filter the Dataset
  This is a bit of a bigger task, which involves choosing a dataset to load and filtering it based on a specified month and day. In the quiz below, you'll implement the load_data() function, which you can use directly in your project. There are four steps:

  "5 lines of raw data" explanation
  https://knowledge.udacity.com/questions/493320
