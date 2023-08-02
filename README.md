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
  * Create new, pre-encoded categorical column showing if a beer is a lager or ale and if beer uses barley or not
  * fill nulls in ABV column with mode of beer ABV (5%) as this matches overall average beer ABV
  * create categorical version of target variable for categorization model
  * split data into train, validate, and test groups in a 60/20/20 split for purposes of in-depth exploration, modeling and evaluation

* Explore data for variables driving beer quality
  * Answer the following initial questions:
      * Which variables are most highly correlated with overall quality?
      * Is there a difference between quality rating of lagers vs ales?
      * Is there a difference between quality rating of barley vs non-barley malt beers?
      * How does ABV contribute to perception of beer quality?

      
* Develop a model to predict beer quality
  * Examine variables identified as drivers of quality
  * Evaluate different types of categorization models on train validate data
  * Create regression models using these potential clusters as features
  * Select best model based on highest accuracy
  * Evaluate the best of these models on test data

## Data Dictionary

There were 13 columns in the initial data and 12 columns after preparation; 1,586,614 rows in the intial data and 1,586,614 after preparation. The target variable is Overall Quality Review: 

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
|Is Lager| Encoded column stating if a beer is a lager or not, derived from Beer Style column|
|Is Barley| Encoded column stating if a beer primarily uses barley as a malt (grain) ingeredient or not, derived from Beer Style column|

## Instructions  to Reproduce the Final Project Notebook
To successfully run/reproduce the final project notebook, please follow these steps:
1. Read this README.md document to familiarize yourself with the project details and key findings.
2. Import separate .csv file from data.world BeerADvocate dataset at https://data.world/socialmediadata/beeradvocate
3. Clone the beer_project repository from GitHub or download the following files: wrangle.py, and final_report.ipynb. 
4. Run compatible notebook or python environment

-------------------------

## Key Findings
* Ales are Rated Higher than Lagers on average, this could be due to perceptions of low quality in American Adjunct lagers
* Traditional barley malt is rated higher than unconventional malts like rye or wheat
* Subcategories of review are not terribly useful in prediction as they are too closely related to overall ratings
* However, scent of beer could be a useful predictor due to its relatively low correlation with overall rating and potentially separate process in brewing
* The final model outperforms baseline by 4-5% and does not seem overfit
* This model seems best at predicting the 4 category of rating, this being the most common rating


## Conclusion
This project set out to identify variables contributing to perception of beer quality for use in choosing a type of beer for distribution. I found that ales and traditional barley beers of higher (6-7%) ABV are rated of higher quality on average. 


## Next Steps
Based on the findings, the following recommendations and next steps are proposed:

1. Conduct linear regression categorization analysis. Trying an additional method may increase performance of the model
2. Create a more detailed malt category column showing which beers are rye, wheat, etc. 
3. Add more variables to the dataset. Data on hops used and dry hopping would add valuable information to identify which ingredients are best percieved by consumers.

   
## Recommendations 
* For a broadly appealing beer, focus first on long fermentation, this will smooth out the beer and increase ABV
* Ales are a good bet for an overall more appealing beer
* Stick to traditional malts to increase sales
