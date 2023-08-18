# Applied_Data_Science_Capstone
Capstone Project for  IBM's Data Science Professional Certificate offered and conducted through Coursera.org. https://www.coursera.org/programs/career-academy-pilot-qzxug/professional-certificates/ibm-data-science

I conducted an in-depth analysis of the landings of the Falcon 9 rocket, which SpaceX manufactures. My analysis was executed with confidence and precision, utilizing a rigorous and exploratory approach. My analysis's findings are comprehensive and insightful, shedding light on the intricate details of the rocket's landings.

Task 1, Web-Scraping:
  1. Perform web scraping to collect SpaceX Falcon 9 Heavy launches from Wikipedia.
  1. Utilized BeautifuSoup Library to extract HTML tables from Wikipedia.
  1. Parse and Convert the table to Pandas Data Frame.
  
Task 2, Data Gathering:
  1. Gather SpaceX data via SpaceX API utilizing requests.
  1. Clean data utilizing pandas, numpy, and Datetime libraries. 
  1. Filter and Wrangle Data.
  1. Resolve missing values.
  
Task 3, SQL Inquiries:
  1. Utilize CSV and Sqlite3 to connect to load and establish a connection with the SQL database.
  1. Load the dataset into the corresponding Db2 database.
  1. Perform SQL queries to solve the supplied questions. 
  1. Ran SQL queries with sub-queries accessing two databases. 

Task 4, Perform Exploratory Data Analysis to predict landing success:
  1. Utilize Numpy and Pandas to Calculate the number of launches on each site.
  1. Calculate occurrences of outcomes per orbit type.
  1. Utilized the Outcome column from the Data Frame to create outcome labels.
  1. Determined rate of success. 

Task 5, Folium Launch Site Analysis:
  1. Utilize the Folium library to create an interactive map of SpaceX launch sites.
  1. Integrated SpaceX DataFrame into Folium map to provide details of locations. 
  1. Maped, marked, and calculated distances from the launch pad to the closest Points of Interest. 

Task 6, Create a Plotly Dash dashboard:
  1. Utilized skeleton key from assignment to add drop-down bar displaying all the sites as options.
  1. Created a Pie chart depicting all sites or individual sites based on bar selection.
  1. Created a slider to allow adjustments on the type of data required.
  1. Dispayed a ScatterPlot as another visual source to understand the data better.
  
Task 7, Machine Learning Prediction Analysis (classification):
  1. Utilize Pandas, Numpy, MatPlotLib, Seaborn, and as well as various Sklearn learn libraries. 
  1. Utilize preprocessing, StandardScaler(), and transform() to standardize data.
  1. Created Test Train training sets with train_test_split() from the Sklearn library.
  1. Conduct GridSearchCV with parameters supplied in the assignment to perform \
    Logistic Regression, Support Vector Machine (SVC), Decision Tree, and K-Nearest Neighbor.
