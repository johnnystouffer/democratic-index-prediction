# Democratic Index: Analysis and Prediction

# TO VIEW DEMO CLICK HERE

## Results

- In summary, it was found that overall democracy is decreasing across the world and it is not tied to a region or how developed a country is.
- Although as can be seen in the stacked plot Liberal Democracies (which are the most democratic) are actually increasing in numbers, and what this shows is although on AVERAGE democracy is going down, in reality, countries are becoming more EXTREME and not in between Authoritarian and Democratic
- We can also see that developed countries with little change compared to developing countries have a more extreme change in their democracies.
- Lastly, we can see from the line plot, we are currently in the longest trend of democracy falling since they recorded the Democratic INdex, and with our predictions that trend is likely to continue.

## Project Inspiration

- I have always been interested in politics, but not on the side of debating and the policies, but on how it has shaped our society. I have been researching the history of politics, elections, wars, and nations, my whole life and recently getting into the Data Science field I knew I wanted to make a project involving politics, however, I did not know how to quantify a field that is so unpredictable and so reliant on peoples emotions instead of numbers and reasoning.

- But then doing my own research I remembered the Democratic Index which is a quantification of the politics of a country, and I knew the EIU (Economic Intelligence Unit) always had yearly reports updating them, so all I had to do was find a dataset that included all the years or web scrape the reports from a reliable source.

- Luckily I found a dataset from OurWorldInData about the Democratic Index and from there I immediately started working on the Dashboard.

## Usage

- The usage of my dashboard is simply insight. See what Democratic Index is and how it changes and what when it changed, and it is changing, and of course, the prediction part to show the current global trend in our politics.

## Project Structure

### Original Data

 - I have two original datasets from OurWorldInData, which can be found in this folder. One of them ('democracy.csv') is the actual index for every country from every year since 1789, and the other ('democracy_index.csv') is the number of countries fitting each type of government.

 ### Fixed Data

 - This folder consists of all the datasets I made from editing, cleaning, and manipulating the data, there are many since in Plotly your dataset has to be formatted in certain ways for each visualization, therefore needing different datasets for each type of visual.
 
 - A short rundown on the important data
    - 'all.csv' is a list of the top 10 most influential countries and top 10 fastest developing countries. This was used to compare the Democratic Index change of already developing countries and developed countries. This visual is the **Bar Chart** in the dashboard.
    - 'difference.csv' is a dataset that takes the average index for every year and compares it to the year before. I did this to see what years and decades had the biggest increase and decreases in Democracy. This data is found in the **Line Plot**.
    - 'final_pivot.csv' is a pivoted table of the 'democracy.csv' in which the years column is now a column per year, this way I was able to make the **Chlorgraph Map** work properly.
    - 'world_data.csv' is a dataset that is used to see the proportion of each type of democracy throughout every year, this dataset was used in the **Stacked Area Plot** and the **Pie Chart**.

### IPyhton Notebooks

- These files, were what I used to clean, visualize, and manipulate the data into the new datasets.
    - 'analysis.ipynb' is the first file I used to see how the data was formatted and used every so basic visual to see what I could do with the data.
    - 'predicting.ipynb' is what I used to create all the new datasets and to create all the predictions using Linear Regression over the past 10 years to predict the trends of the next 8 until **2030**
    - 'visualizing.ioynb' instead of trying to create the visuals in the dashboard I decided to make them all in this notebook to refine them first then send them over. Also to finalize all datasets.

### dashboard.py

- The file has all the necessary data and visuals to run the dashboard Using Plotly Dash and Plotly Go along with all other Python packages to make it work, like NumPy and Pandas

## Acknowledgements

- https://ourworldindata.org/democracy - for the datasets
- https://www.eiu.com/n/campaigns/democracy-index-2022/ - for the reports

## Struggles with the Project

### Data
- The data had to be rearranged in many different ways to get the visualizations to work.
- The struggled with Plotly as I wanted to use it since it was highly customizable, however, to customize I needed to know CSS and some HTML which I was unfamiliar with so I had to do some work to learn about HTML and CSS to make it look the way I wanted it to.
- I was unaware of how many datasets I would need, and I was also unaware of the different assets I was going to need to make it look nice, so I ended up being very unorganized and cluttered for a while, making the project unnecessarily harder.

### Project by John Stouffer
#### _Incoming Sophomore - Data Science_
#### _4/22/2023 - 6/23/2023_

### Socials
- LinkedIn - https://www.linkedin.com/in/johnny-stouffer/
- Handshake - https://app.joinhandshake.com/stu/users/42021195
- Email - johnstouffer21@gmail.com
