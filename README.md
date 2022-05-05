# Project of Data Visualization (COM-480) - Team MuggleData

| Student's name    | SCIPER | Email |
| ------------------| ------ |-------|
| Antoine Daeniker  | 287913 |antoine.daeniker@epfl.ch|
| David Desboeufs   | 287441 |david.desboeufs@epfl.ch|
| Jérémie Frei      | 247316 |jeremie.frei@epfl.ch|

**[Website](#https://com-480-data-visualization.github.io/datavis-project-2022-muggledata/index.html)**

[Milestone 1](#milestone-1-friday-8th-april-5pm) • [Milestone 2](#milestone-2-friday-6th-may-5pm) • [Milestone 3]

# Milestone 1 (Friday 8th April, 5pm)

The Harry Potter universe is a reference in the modern literature. Indeed, it is without a doubt one of the most famous saga ever written. After seven bestseller novels and eight blockbusters in the span of 15 years, its roots in pop culture are still very much alive. 

Its rich narratives and elaborated plots makes the whole universe difficult to grasp. This is why we came with the idea of clarifying some key properties of this masterpieces.

## Dataset

We found many datasets related to Harry Potter. Those are the main ones which we explored for now :

- <b>Characters dataset</b> : Name | Birth Date | Death Date  | Gender | House | Loyalty | Wand | Patronus | etc. 

- <b>Potions dataset</b> : Name | Known ingredients | Effect | Characteristics | Difficulty level

- <b>Spells dataset</b> : Name | Incantation | Type | Effect | Light

- <b>Books</b> : We also found all books of the saga in .txt files 


### Data quality
The data are mostly strings. For example, birth and death dates are written in string and not the conventional data type <em>datetime64</em>. Since there's only string, sometimes the information are compact into a single string and are not seperate, which add difficulties to extract the required informations. For example, we have in our character's file, a column name <em>wand</em> where the information about the size and the material of the wand are compact into a single string. This would need to be pre-process before using it (if we decide to use it).


## Problematic
Our principal topic is to create an interactive genealogy tree which represent family's link between all characters in our character dataset.

The second one is to create a visualization using the <em>Potion</em> dataset. The goal is to create links betweens the potions, the difficulties and the ingredients uses.

For the third one, we were thinking about building an interactive bubble graph using the <em>Spell</em> dataset, grouping them by spell types.


## Exploratory Data Analysis
Below, you can see some of the graphs we generated during eploratory data analysis ([Figs](Figs)) just to have an insight of our data.

![houses](./Figs/houses.png)
![loyalty](./Figs/loyalty.png)
![words](./Figs/words_counter.png)


## Related Work
We found a few works related to Harry Potter, the first one[4] studies the evolution of characters during the series of books by using dynamic graph network. The second one[5] concerns the words occurences toward the novel, they used Harry Potter has an example to demonstrate how MapReduce works. 

Our goal is to make data interactive, not just static images that are sometimes difficult to grasp. We want to select three topics that we will develop in depth. For example we can take the genealogy of characters, the user will be able to select a specific character to explore all his genealogical links.

The dataset choice was inspired by a visualization project done in COM-480 on The Lord of the rings[6].

## References

#### Datasets
* [1] https://data.world/harishkgarg/harry-potter-universe
* [2] https://www.kaggle.com/datasets/gulsahdemiryurek/harry-potter-dataset
* [3] https://www.kaggle.com/datasets/balabaskar/harry-potter-books-corpora-part-1-7

#### Related work
* [4] https://github.com/AlexDuvalinho/Dynamic-Graph-Networks/blob/master/report/NSA_Project_Report.pdf
* [5] https://towardsdatascience.com/understanding-mapreduce-with-the-help-of-harry-potter-5b0ae89cc88
* [6] https://com-480-data-visualization.github.io/com-480-project-bkh/


# Milestone 2 (Friday 6th May, 5pm)


## Muggle data website

Click [here](https://com-480-data-visualization.github.io/datavis-project-2022-muggledata/) to see our project prototype.

## Sketches
###
Y'a des 

## Tools

### Javascript framework


## Goals

