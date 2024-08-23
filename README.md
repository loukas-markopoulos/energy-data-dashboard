# Data dashboard created for Collins Aerospace

This dashboard will allow the user to upload a data table (CSV file) to the web app which has 3 pages.

## Pages
Data - prints the uploaded CSV file as a data table that includes different consumer's energy cosnumption that can be scrolled through. To upload the CSV file, simply click on the 'Select Files' text or drag an drop the CSV file in that location.

Largest Consumer - the dropdown allows you to select one month which then prints a bar chart of each consumer's energy consumption in descending order. It will do this for the year which that month has passed in most recently (eg. if it is August and you select July, it will show this year's July's data. However if you select September, it will show last year's September's data since there is no data for next month yet).

Year Graph - the dropdown allows you to select one or more consumer which then prints a bar chart of those consumers' energy consumption next to each other for each month across the year selected.

## Creating a compatible CSV file
Saved in this repository is an example of an excel file (Data_test.xlsx) that should be adapted to create a table with your specific data. 

The column headers are the names of each machine and the year their data is from (eg. Consumer 1 2023 and Consumer 1 2024 are two seperate columns). The rows are the months in the year (JAN to DEC).

In each cell within the table, a value for the energy consumption of that machine in that month (can be in any units you want) should be input. For months that have not yet finished (no data) a 0 must be put in the cell.

In this case, 61 consumers are being analysed across 2 years however these can be changed:

If you want to analyse a different number of consumers, line 44 in the file 'Largest_Consumers' must be changed to the desired number. Then in your excel file ensure the number of columns (excluding 'Month' column) is a multiple of the number of consumers.
```python
[44] consumer_no = *your number of consumers here*
```

If you want to analyse a different number of years, the excel data table must have a number of columns (excluding the 'Month' column) that is the multiple of the nuber of years and the number of consumers. 

Do not change any of the first column ('Month').

Ensure to convert your excel file to a CSV file before uploading it to the web app.

## Styling
The CSS file for styling can be edited to your liking. 

## License
[GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/)
