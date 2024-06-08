# Economics_UrbanBeauty

An attempt to measure **Urban Beauty** using a **Gravitational Index**.

The idea is to assign *weights* to each neighborhood in a city based on the amount of beauty it possesses. A proxy for beauty is determined by the quantity of historical, cultural, and recreational attractions near the center of each neighborhood.

It is expected that neighborhoods with a higher *weight* will have higher average housing prices and higher average wages.

To accomplish this, the steps bellow must be followed:

## Step 1 - Obtaining Centers

The city under study can be divided into various entities, notably 'Bairros' (Neighborhoods) and 'Macrozonas' (Macrozones), which will be central to our analysis. We have the option to utilize either the geometric center or the population center of this subdivisions. In this project, we'll explore all possibilities and determine which yields the most promising results.

#### Geometric Center
By acquiring the shapefiles of the Neighborhoods and Macrozones, we gain access to their polygons and consequently their respective vertices.

With this information, it's possible to compute the Area and the Center of these forms using the expressions bellow:


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
- \( Cy \) is the Latitude of the center,
  

#### Populacional Center

## Step 2 - Obtaining coordinates of historical and recreational sites

## Step 3 - Compute the Gravitacional Index

$$
GI = \sum_{i=1}^{n} \frac{1}{d^2_i}
$$

where:
- \( GI \) is the gravitational index,
- \( d \) is the distance beetween the center and the specific attraction


## Step 4 - Review Data

## Step 5 - Correlation Analysis
