# latitude requirements
- Generate a csv file containing first_name, last_name, address, date_of_birth
- Process the csv file to anonymise the data
- Columns to anonymise are first_name, last_name and address
- You might be thinking  that is silly
- Now make this work on 2GB csv file (should be doable on a laptop)
- Demonstrate that the same can work on bigger dataset
- Hint - You would need some distributed computing platform

# Data processing
This is a Data processing mini project, which actually works by generating a CSV and then convert the columns that needs to be anonymise and vreate a new CSV.
There will be two files created after the data_processing.py is run under /tmp

* persons.csv -- Generated CSV depending on the file size given
* anon_persons.csv - converted CSC after anonymise the data.

Now to run the the conversion for Bigger data set we will use Databrics Notebook

* Login to Datbricks community edition
* first generate the source data(Huge file size) set using our data_processing.py 
* copy the CSV to databricks Filestore

## Requirements
This application requires Python 3 and Databricks community edition.

* Databricks ( for DataFrames to load and run the data in spark cluster)

* python 3 


## Requirement Installation


```bash
sudo pip install unicodecsv
sudo pip install Faker

```

## Run

* python data_processing.py (This python script will generate CSV depending on the input file size provided and also covert the columns that needs to anonymise)
