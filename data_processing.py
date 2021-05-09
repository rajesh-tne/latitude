
import unicodecsv as csv
from faker import Factory
from collections import defaultdict
import random
import string
import os


def generate_csv(file_name, file_size):
    with open(file_name, 'wb') as csvfile:
        filewriter = csv.DictWriter(csvfile, fieldnames=['first_name', 'last_name', 'address', 'dob'])
        file_stats = os.stat(file_name)
        filewriter.writeheader()
        while(file_stats.st_size / (1024 * 1024) < int(file_size)):
            first_name = str(''.join(random.choice(string.ascii_lowercase) for i in range(5)))
            last_name = str(''.join(random.choice(string.ascii_lowercase) for i in range(5)))
            address = str(''.join(random.choice(string.digits) for i in range(5)) +' '+\
                      ''.join(random.choice(string.ascii_lowercase) for i in range(5)) +\
                      ' '+''.join(random.choice(string.ascii_lowercase) for i in range(5)))
            dob = str(random.randint(1, 30)) +\
                  '-'+str(random.randint(1, 12)) + '-' + str(random.randint(1970, 2000))
            filewriter.writerow({"first_name":first_name, "last_name":last_name, "address":address, "dob":dob})
            file_stats = os.stat(file_name)
        csvfile.close()

def anonymize_rows(rows):
    """
    Rows is an iterable of dictionaries that contain name and
    address fields that need to be anonymized.
    """
    # Load the faker and its providers
    faker  = Factory.create()

    # Create mappings of names & address to faked names & address.
    names  = defaultdict(faker.name)
    addresses = defaultdict(faker.address)


    # Iterate over the rows and yield anonymized rows.
    for row in rows:
        # Replace the name and email fields with faked fields.
        row['first_name']  = names[row['first_name']]
        row['last_name'] = names[row['last_name']]
        row['address'] = addresses[row['address']]

        # Yield the row back to the caller
        yield row


def anonymize(source, target):
    """
    The source argument is a path to a CSV file containing data to anonymize,
    while target is a path to write the anonymized CSV data to.
    """

    with open(source, 'rb') as f:
        with open(target, 'wb') as o:
            # Use the DictReader to easily extract fields
            reader = csv.DictReader(f)
            writer = csv.DictWriter(o, reader.fieldnames)

            # Read and anonymize data, writing to target file.
            for row in anonymize_rows(reader):
                writer.writerow(row)


#Main
#input_file_size = 1 ## Please change this value depending on your requirmenet in MB
input_file_size = input('Please give the file size in MB to generate CSV: ')
src_file_name = '/tmp/persons.csv'
dest_file_name = '/tmp/anon_persons.csv'
generate_csv(src_file_name, input_file_size)
anonymize(src_file_name, dest_file_name)
