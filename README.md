# Applied_Data_Science_Capstone
Capstone Project for  IBM Data Science Professional Certificate

This capstone project will predict if the Falcon 9 first-stage rocket will land successfully using a variety of Data Science libraries and techniques.

Task 1, Web-Scraping:
  A. Perform web scraping to collect SpaceX Falcon 9 Heavy launches from Wikipedia.
  B. Utilized BeautifuSoup Library to extract HTML tables from Wikipedia.
  C. Parse and Convert the table to Pandas Data Frame.
  
Task 2, Data Gathering:
  A. Gather SpaceX data via SpaceX API utilizing requests.
  B. Clean data utilizing pandas, numpy, and datetime libraries. 
  C. Filter and Wrangle Data.
  D. Resolve missing values.
  
Task 3, SQL Inquiries:
  A. Utilize CSV and Sqlite3 to connect to load and establish a connection with SQL database.
  B. Load the dataset into the corresponding Db2 database.
  C. Perform SQL queries to solve the supplied questions. 
  D. Ran SQL queries with sub-queries accessing two databases. 

Task 4, Perform Exploratory Data Analysis to predict landing success:
  A. Utilize Numpy and Pandas to Calculate the number of launches on each site.
  B. Calculate occurrences of outcomes per orbit type.
  C. Utilized the Outcome column from the Data Frame to create outcome labels.
  D. Determined rate of success. 

Task 5, Folium Launch Site Analysis:
  A. Utilize the Folium library to create an interactive map of SpaceX launch sites.
  B. Integrated SpaceX DataFrame into Folium map to provide details of locations. 
  C. Maped, marked, and calculated distances from the launch pad to the closest Points of Interest. 

Task 6, Machine Learning Prediction:
  A. Utilize Pandas, Numpy, MatPlotLib, Seaborn, and as well as various Sklearn learn libraries. 
  B. Utilize preprocessing, StandardScaler(), and transform() to standardize data.
  C. Created Test Train training sets with train_test_split() from the Sklearn library.
  D. Conduct GridSearchCV with parameters supplied in the assignment to perform \
    Logistic Regression, Support Vector Machine (SVC), Decision Tree, and K-Nearest Neighbor.
