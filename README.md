# Economics_UrbanBeauty

An attempt to measure **Urban Beauty** using a **Gravitational Index**.

The idea is to assign *weights* to each neighborhood in a city based on the amount of beauty it possesses. A proxy for beauty is determined by the quantity of historical, cultural, and recreational attractions (scenic sites) near the center of each neighborhood.

It is expected that neighborhoods with a higher *weight* will have higher average housing prices and higher average wages.

To accomplish this, the steps bellow must be followed:

## Step 1 - Obtaining Centers

The city under study can be divided into various entities, notably 'Bairros' (Neighborhoods) and 'Macrozonas' (Macrozones), which will be central to our analysis. We have the option to utilize either the geometric center or the population center of this subdivisions. In this project, we'll explore all possibilities and determine which yields the most promising results.

#### Geometric Center
By acquiring the shapefiles of the Neighborhoods and Macrozones, we gain access to their polygons and consequently their respective vertices.

With this information, it's possible to compute the Area and the Center of these forms using the expressions bellow

$$
A = \frac{1}{2} \sum_{i=1}^{n-1} (x_{i}y_{i+1} - x_{i+1}y_{i})
$$

$$
C_{x} = \frac{1}{6A} \sum_{i=1}^{n-1} (x_{i}+x_{i+1})(x_{i}y_{i+1} - x_{i+1}y_{i})
$$

$$
C_{y} = \frac{1}{6A} \sum_{i=1}^{n-1} (y_{i}+y_{i+1})(x_{i}y_{i+1} - x_{i+1}y_{i})
$$

where:
- \( A \) is the area of the polygon,
- \( x \) is the Longitude of the vertex,
- \( y \) is the Latitude of the vertex,
- \( Cx \) is the Longitude of the center,
- \( Cy \) is the Latitude of the center.
  

#### Populacional Center
The data for populacional density was taken from 2020 NASA GPW on [https://sedac.ciesin.columbia.edu/data/collection/gpw-v4 ] and the center of each Neighborhood and Macrozone was obtained via QGIS and then exported do a .xlsx file.

## Step 2 - Obtaining coordinates of Scenic Locations 

In this work, the following urban spaces will be defined as Scenic Locations:
Parks, Museums, Memorials, and Historical-Cultural Heritage sites, as designated by the Porto Alegre City Hall. Parks and squares are considered Recreational Locations, while museums, memorials, and historical-cultural heritage sites are considered Historical Locations. The coordinates were obtained by manually pinning the locations on Google Maps.

## Step 3 - Computing the Gravitacional Index

This index was based on Carlino & Saiz paper https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1293550. 
The index express how much historicity or beauty is near the center of the division selected, higer the value, the more concentrated is the beaty of the division, so it's expected that beautiful neighborhoods have a high index.

The index is constructed as bellow:

$$
GI = \sum_{i=1}^{n} \frac{1}{d^2_i}
$$

where:
- \( GI \) is the gravitational index,
- \( d \) is the distance beetween the center and the specific attraction.

The index as it is above does not adress the quality of the diferent interest sites (a park can be better than another parl, for example) so we utilized the index below to try to adress this issue.

$$
GI = \sum_{i=1}^{n} \frac{s_{i}}{d^2_i}
$$

where:
- \( s \) is the score of the park i,

The score is based on diferentt itens:

- Proximity of the park in relationship to the 'Orla do Guaíba' wich is the main Scenic Location of Porto Alegre,
- Quality of Infraestructure of the park,
- Size of the park.

All these items were normalized using the max-min method, so the score is always between 0 and 1. 
The distance between the park and "Orla do Guaíba" was determined by the script "Dist Orla." The area and the center of the parks were determined manually (clear room for improvement) by setting the vertices along the boundaries of the park and pinning the center manually. 
The quality was determined by the quality of infrastructure.

## Step 4 - Visualizing Data

On the 'Streamlit' repository it's possible to visualize the Dataframes, Map and a Correlation Matrix were we can see, compare an get some insights about the Data obtained.

The Streamlit app can be accessed on the link bellow:
https://economicsurbanbeauty-rvgejj7wd9luepcjwnlpcv.streamlit.app/

(Gnerate the webscraping for housing prices)

## Step 5 - Correlation Analysis

At the end of the data Visualisation link there's a correlations analysis where it's possible to identify that some variables have a relevant correlation, (mention the model and it's implications and the relationship between the variables.)

Here's the corrected version of your text with grammar and clarity improvements:

## Objectives ##

- Obtain the Geometrical and Population Centers of Neighborhoods and Macrozones :ballot_box_with_check: :o:
- List historic places and parks with information about their location, area, quality, and distance in relation to the main body of water in Porto Alegre (Lake Guaíba) :ballot_box_with_check:
- Calculate the Recreational and Historical Indices for each subdivision of the city :ballot_box_with_check:
- Obtain socioeconomic data about wages and education levels in Porto Alegre :ballot_box_with_check:
- Web scrape the average rent prices for housing in each subdivision of Porto Alegre :o:
- Correlate the indices with the socioeconomic data to verify the relationships among variables :ballot_box_with_check:
- Present the data on Streamlit :ballot_box_with_check:
