[comment]: # (a)

# ghetto.Color
[comment]: # (rewrite ^)
### 1. What is a ghetto [in the US]?

> "American ghetto" usually denotes an urban neighborhood with crime, gang violence, and extreme poverty, with a significant number of minority citizens living in it. -- [American ghettos](https://en.wikipedia.org/wiki/American_ghettos#Description), _Wikipedia_

### 2. Can you find ghettos through data?

To answer that question, we'll use the following criteria: 

[comment]: # (rewrite ^)

1. Crime
2. Poverty
3. Minorities

#### Crime

> In the FBI’s Uniform Crime Reporting (UCR) Program, violent crime is composed of four offenses: murder and nonnegligent manslaughter, rape, robbery, and aggravated assault. Violent crimes are defined in the UCR Program as those offenses that involve force or threat of force. -- [US Dept of Justice]([https://en.wikipedia.org/wiki/American_ghettos#Description](https://ucr.fbi.gov/crime-in-the-u.s/2019/crime-in-the-u.s.-2019/topic-pages/violent-crime))

[comment]: # (dataset: https://ucr.fbi.gov/crime-in-the-u.s/2019/crime-in-the-u.s.-2019/topic-pages/tables/table-6)
[comment]: # (data processing steps:)
[comment]: # (1. geolocation / metropolitan geocords according to fbi)
[comment]: # (a. city geocoords)
[comment]: # (b. county geocoords [if any] )
[comment]: # (2. crime data = row 3)

#### Poverty
[comment]: # (https://www.census.gov/data/datasets/2020/demo/saipe/2020-state-and-county.html)
[comment]: # (gather county geocords)
[comment]: # (poverty estimate all ages)
[comment]: # (median income)

#### Minorities
[comment]: # (2020 Census Redistricting Data (P.L. 94-171))
[comment]: # (https://data.census.gov/cedsci/table?g=0100000US%240500000&y=2020&d=DEC%20Redistricting%20Data%20%28PL%2094-171%29&tid=DECENNIALPL2020.P1)
[comment]: # (gather county geocords)
[comment]: # (refer to column metadata to gather the correct columns for racial data)


[comment]: # (4 layered map [color coded])

[comment]: # (layer 1: high crime areas)
[comment]: # (layer 2: poverty stricken areas)
[comment]: # (layer 3: high % of non-white)

[comment]: # (layer opacity is dimmed by switches)
[comment]: # (the idea is to mix the colors in such a way that it highlights areas)
[comment]: # (suffering from all these afflictions simultaneously)
[comment]: # (for the documentation:)
[comment]: # (the idea is to step the reader through the story of the data)
[comment]: # (whilst revealing the color of the ghetto)
