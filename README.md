# next_word_prediction_streamlit
A web app that is capable of predicting next word on it's own.


## Table of Content
  * [Demo](#demo)
  * [Overview](#overview)
  * [Installation](#installation)
  * [Run](#run)
  * [Bug / Feature Request](#bug---feature-request)
  * [Contribution](#contribution)
  * [Technologies Used](#technologies-used)
  * [Team](#team)


## Demo




## Overview
A web application that has two pretained model BERT and XLNET that will be loaded when they will be selected only once . After that they will serve fast as they are cached. You can select n number of next words that should come after given text.

## Installation
1. Windows user can double click on activation.bat file to install required package
2. Linux User type following command in commnand line
a) First create a virtual environment 
```bash
python3.7 -m virtualenv venv
```
b) Move to venv directory and activate environment
```bash
cd venv
. bin/activate
```
c) Clone this project 
```bash
git clone https://github.com/pandeynandancse/next_word_prediction_streamlit.git
```

d) Move into cloned directory
```bash
cd next_word_prediction_streamlit
```
e) Now install all requirements
```bash
pip install -r requirements.txt
```
## Run
1. After successfull installation windows user can directly open the link that will be appeared
2. After successful installation open type
```bash
streamlit run next_word.py
 ```
and then open link 

## To Do
1. Add More Architecture Options
2. Trigger prediction on each time when space is pressed






## Bug / Feature Request
If you find a bug (the website couldn't handle the query and / or gave undesired results), kindly open an issue [here](https://github.com/pandeynandancse/next_word_prediction_streamlit/issues/new) by including your search query and the expected result.

If you'd like to request a new function, feel free to do so by opening an issue [here](https://github.com/pandeynandancse/next_word_prediction_streamlit/issues/new). Please include sample queries and their corresponding results.


## Contribution
If you'd like to do some contribution, feel free to do so by opening a pull request [here](https://github.com/pandeynandancse/next_word_prediction_streamlit/pulls). Please include sample queries and their corresponding results.




## Technologies Used

![](https://forthebadge.com/images/badges/made-with-python.svg)

[<img target="_blank" src="https://i.imgur.com/jAyHARm.png" width=170>](https://www.streamlit.io/)
[<img target="_blank" src="https://i.imgur.com/TDYScZd.png" width=170>](https://pytorch.org/) 



## Contributor
[![Nandan Pandey](https://qph.fs.quoracdn.net/main-thumb-189737418-200-jmwzsixdznlgemnejuecomukeluqkgzd.jpeg)](https://pandeynandancse.github.io) |
-|
[Nandan Pandey](https://pandeynandancse.github.io) |)



 
