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
[comment]: # (1. geolocation)
[comment]: # (a. city geocoords)
[comment]: # (b. county geocoords [if any] )
[comment]: # (2. crime data = row 3)

[comment]: # (x)

#### Poverty

[comment]: # (4 layered map [color coded])

[comment]: # (layer 1: colloquial ghettos)
[comment]: # (layer 2: high crime areas)
[comment]: # (layer 3: gang violence)
[comment]: # (layer 4: poverty stricken areas)
[comment]: # (layer 5: high % of non-white)
[comment]: # (layer opacity is dimmed by switches)
[comment]: # (the idea is to mix the colors in such a way that it highlights areas)
[comment]: # (suffering from all these afflictions simultaneously)
[comment]: # (for the documentation:)
[comment]: # (the idea is to step the reader through the story of the data)
[comment]: # (whilst revealing the color of the ghetto)
