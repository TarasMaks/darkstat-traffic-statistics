# darkstat traffic extraction
This Python script extracts the darkstat real-time traffic statistics and transforms and exports the data into a csv-file.
Plotly is used to graph the data.

## Overview

This Python code extracts the darkstat real-time traffic statistic and transforms and exports the data into a csv-file using Python Pandas.
Plotly is used to graph the data. If this code is run every day around midnight it gives a good representation of in and out traffic of the Synology diskstation.

[darkstat](https://unix4lyfe.org/darkstat/) can be installed through the Synology software Package which can be found at [Synocommunity](https://synocommunity.com/packages).

## Dependencies

* Pandas
* Requests
* Plotly
* Synology Diskstation 6.x
* darkstat (https://unix4lyfe.org/darkstat/)


## Usage

Adjust your path variables `csv_folder` and `csv_file` first.
Once you have your dependencies installed via pip, run the Python script in terminal via

```
python scrap_display.py
```
