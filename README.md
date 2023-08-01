# Individual Project: Beer Dataset

## Project Description

New brewers and mid range brewers face difficult choices when choosing a particular recipe for distribution. They need to create beers that are distinctive, but also have varieties that are more broadly appealing to maximize sales. Determining which beers will appeal to buyers is crucial for marketing beyond the brewery itself as well as for choosing new varieties for distributing to vendors. 
 
The following project is intended to analyze the factors contributing to perception of overall beer quality for use in choosing a type of beer for distribution. The data was downloaded from data.world's BeerAdvocate dataset, containing over 1.5 million ratings of beer from users on the BeerAdvocate website until November, 2011. The dataset provides ratings for overall and individual aspects of beer quality with a rating scale of 1 to 5. It also provides data on beer type and abv. 

## Project Goal

* Discover variables (drivers) contributing to the quality of beer ratings
* Utilize these drivers to predict categories of beer rating based on qualities and sub ratings
* Utilize this final categorization model in predicting perception of quality of beers going forward

## Initial Hypothesis
I hypothesize that lager beers with higher ABV will be rated higher in general. 

## Planning Process

* Acquire data from data.world BeerAdvocate dataset

* Prepare data:
  * Eliminate columns that are not immediately useful to the project
  * Create new column showing if a beer is a lager or ale
  * fill nulls in ABV column with mode of beer ABV (5%) as this matches overall average beer ABV
  * create categorical version of target variable for categorization model
  * split data into train, validate, and test groups in a 60/20/20 split for purposes of in-depth exploration, modeling and evaluation

* Explore data for variables driving beer quality
  * Answer the following initial questions:
      * Is there a difference between quality rating of lagers vs ales?
      * How does ABV contribute to perception of beer quality?
      * Which subratings of beer quality are most highly correlated with overall quality?
      
* Develop a model to predict beer quality
  * Examine variables identified as drivers of quality
  * Evaluate different types of categorization models on train validate data
  * Create regression models using these potential clusters as features
  * Select best model based on highest accuracy
  * Evaluate the best of these models on test data

## Data Dictionary

There were 13 columns in the initial data and 11 columns after preparation; 1,586,614 rows in the intial data and 1,586,614 after preparation. The target variable is Overall Quality Review: 

| Feature | Definition |
|:--------|:-----------|
|Overall Quality Review| Rating from 1 to 5 of overall beer quality from an individual user on BeerAdvocate.com, target variable|
|Review Category| Transformation of target variable into 5 categories: 0-1 = 1, 1-2 = 2, etc.|
|Aroma Review| Rating from 1 to 5 of quality for beer smell|
|Appearance Review| Rating from 1 to 5 of beer's appearance |
|Palate Review| Rating from 1 to 5 of how beer feels in one's mouth|
|Taste Review| Rating from 1 to 5 of how beer tastes|
|Beer Style| string stating the name of the style of beer, 104 unique values|
|Beer Name| String stating name of beer|
|Beer ABV| Float displaying percentage of alcohol in beer|
|Beer ID| Numeric identifier of individual beer|
