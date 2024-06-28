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
  

#### Populational Center
The data for populational density was taken from [2020 NASA GPW](https://sedac.ciesin.columbia.edu/data/collection/gpw-v4) and the center of each Neighborhood and Macrozone was obtained via QGIS and then exported to a _xlsx_ file.

## Step 2 - Obtaining coordinates of Scenic Locations 

In this work, the following urban spaces will be defined as Scenic Locations:
Parks, Museums, Memorials, and Historical-Cultural Heritage sites, as designated by the Porto Alegre City Hall. Parks and squares are considered Recreational Locations, while museums, memorials, and historical-cultural heritage sites are considered Historical Locations. The coordinates were obtained by manually pinning the locations on Google Maps.

## Step 3 - Computing the Gravitacional Index

This index was based on Carlino & Saiz [paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1293550). 
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

In the 'Streamlit' folder, you'll find the script for the app. We can view the complete DataFrames for Macrozones and Neighborhoods, an interactive map of Porto Alegre showing city subdivisions along with their geometric and population centers, and the correlation matrix.

Access the Streamlit app using the link below:
[Visualize Data](https://economicsurbanbeauty-rvgejj7wd9luepcjwnlpcv.streamlit.app/)

## Step 5 - Correlation Analysis

At the end of the data visualization link, there is a correlation analysis revealing that certain variables exhibit notable correlations. In the top right corner of the matrix, we observe a correlation of 0.59 between the Historical Geometrical Center Index and the Price/m² of neighborhoods, suggesting that the index may explain variations in housing prices across the city. Similarly, a correlation of 0.6 is evident between the Recreational Geometrical Center Index and housing prices. Although correlations with population center indices are significant, they are comparatively lower than those with geometrical indices.

Furthermore, an inverse relationship appears between the School Dropout rate and the Historical Geometrical Center Index, evidenced by a correlation of -0.33.


## Objectives ##

- Obtain the geometrical and population centers of neighborhoods and macrozones :ballot_box_with_check:
- List historic places and parks with information about their location, area, quality, and distance in relation to the main body of water in Porto Alegre (Lake Guaíba) :ballot_box_with_check:
- Calculate the recreational and historical indices for each subdivision of the city :ballot_box_with_check:
- Obtain socioeconomic data about wages and education levels in Porto Alegre :ballot_box_with_check:
- Web scrape the average prices for housing in each subdivision of Porto Alegre :ballot_box_with_check:
- Correlate the indices with the socioeconomic data to verify the relationships among variables :ballot_box_with_check:
- Present the data on Streamlit :ballot_box_with_check:
