# latitude requirements
- Generate a csv file containing first_name, last_name, address, date_of_birth
- Process the csv file to anonymise the data
- Columns to anonymise are first_name, last_name and address
- You might be thinking  that is silly
- Now make this work on 2GB csv file (should be doable on a laptop)
- Demonstrate that the same can work on bigger dataset
- Hint - You would need some distributed computing platform

# Data processing - Local
This is a Data processing mini project, which actually works by generating a CSV and then convert the columns that needs to be anonymise and vreate a new CSV.
There will be two files created after the data_processing.py is run under /tmp

* persons.csv -- Generated CSV depending on the file size given
* anon_persons.csv - converted CSC after anonymise the data.

# Data processing - Big data
Now to run the the conversion for Bigger data set we will use Databrics Notebook which has pyspark and spark clusters.

* Login to Databricks community edition
* first generate the source data(Huge file size) set using our data_processing.py(File will be generated under /tmp/persons.csv)
* copy the CSV to databricks Filestore ususally the file is copied to (/FileStore/tables/persons.csv). if you are new to Databricks i can send a seperate notes on how to upload the data(Its straight forward).
* just create a cluster and choose Databrick runtime as per notes in requirements section.
* Go to Workspace, you will find an option to import notebook. Choose anonymise.dbc(added here in git) file for import and you can see the Notebook code created for this project.
* Once you open the Notebook , choose the cluster created above in the dropdown and then just run the notebook(Cmd 1). If you see Faker module not present, just run 'pip install Faker'. I have given the command in Notebook itself (Cmd 2)

 

## Requirements
This application requires Python 3 and Databricks community edition.

* Databricks ( for DataFrames to load and run the data in spark cluster)

* python 3 

* Databricks run time version 8.1 (includes Apache Spark 3.1.1, Scala 2.12) 


## Requirement Installation


```bash
sudo pip install unicodecsv
sudo pip install Faker

```

## Run

* python data_processing.py (This python script will generate CSV depending on the input file size provided and also covert the columns that needs to anonymise)
