# h-index Research
## Overview
Check out the code for both simulated citation networks via Price's model and arXiv citation networks. 
These notebooks also contain the analysis comparing our theoretical results to both simmulated and real h-indices.
Please refer to [my Honors Thesis](https://scholar.colorado.edu/honr_theses/1906/) for information regarding the project. 
## The Data 
All of the necessary data was obtained from arXiv.org by Damien P. George and Robert Knegjens and can be found on their [github](https://github.com/paperscape/paperscape-data).
They also have a really cool visualization of their data at http://paperscape.org.
## Implementation
There are two .ipynb files each with a supplementary .txt file which supplements the narrative of each notebook. The code in the 
notebooks is constructive with each section building on the previous one. 
[Simulations.py](Simulations.py) is a .py file with some of the functions in [Simulations.ipynb](Simulations.ipynb) so that some of its necessary functions can be used in [PaperScape_Data.ipynb](PaperScape_Data.ipynb).
### Simulated Citation Networks and Theory Implemenation
[Simulations.ipynb](Simulations.ipynb) is the notebook which all the simulated citation networks following Price's model were 
created. The visualization functions are spread throughout the notebook, usually following the functions that develop the data
to be visualized. 

### arXiv Citation Networks and Comparison with Theory
[PaperScape_Data.ipynb](PaperScape_Data.ipynb) is the notebook where all the arXiv citation networks are created and analyzed. The [PaperScape data](https://github.com/paperscape/paperscape-data) needs to be downloaded from The order of the code is: 

1. collect all the information regarding individual papers

2. collect all of the unique authors' information

3. build citation networks

4. fit Price's model parameters from the citation networks

5. compare the real citation networks to the theory

Again the visualization functions are spread through the code, primarily within their relevant sections.

## Dependencies 
All of the code is implemented in [Python3](https://www.python.org/download/releases/3.0/). If you are just starting out with python I would recommend [Anaconda](https://www.anaconda.com/distribution/) as a package manager. The packages I use are:

- matplotlib
- numpy
- scipy
- pandas
- csv
- copy
- progressbar
- sklearn
- math
- random

If the package is not in the Anaconda base it can be installed using [conda install](https://docs.anaconda.com/anaconda/user-guide/tasks/install-packages/).

## Acknowledgements
It is likely if you are looking at this github you were refered here by Professor Manuel Lladser, regardless I would like to thank him for all the help, encouragement and insight on this research.

## Contact
Tyler Schuessler

Contact: tysc7535@colorado.edu or schuesslertyler@gmail.com or ask Professor Manuel Lladser for my current email address
