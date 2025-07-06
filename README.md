# Task 

An external system / supplier is sending patient data to our platform using the FHIR standard. Our analytics teams find this format difficult to work with when creating dashboards and visualizations. This application sees these datasets tranformed into a more workable tabular format as worksheets in excel, and also as tables in a SQL database.

## Installation

- Perform a GIT PULL for this repository

- Install the necessary requirements found in the requirements.txt file using the command:
pip install -r requirements.txt
This step can be skipped if running the application through Docker

## Process_raw_data function

The Python script - `app.py` reads in all, or any specified FHIR formatted json file from the list of files in the 'data' folder.
It then attempts to flatten the nested data into a tabular dataframe, before exporting them into a spreadsheet and again into a SQL database.

Append line 19 in the app to specify a file, or leave it as `.json` to capture all files.

In your terminal, run the command:
python app.py      

This will initially create an excel workbook and a sql database including the tabular data created.

Alternatively, using Docker, run the following command in your terminal:
docker compose build

Once built, use the following command to start the container:
docker compose up -d

As long as the container is running, you should be able to see the created files directly on Docker Desktop.

This process can be repeated.