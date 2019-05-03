# h-index-Research
## Overview
Check out the code for both simulated citation networks via Price's model and arXiv citation networks. 
These notebooks also contain the analysis comparing our theoretical results to both simmulated and real h-indices.
Please refer to https://scholar.colorado.edu/honr_theses/1906/ for information regarding the project. 
## The Data 
All of the necessary data was obtained from arXiv.org by Damien P. George and Robert Knegjens and can be found on their github:https://github.com/paperscape/paperscape-data.
They also have a really cool visualization of their data at http://paperscape.org.
## Implementation
There are two .ipynb files each with a supplementary .txt file which supplements the narrative of each notebook. The code in the 
notebooks is constructive with each section building on the previous one.
[Simulations.py](Simulations.py) is the .py version of [Simulations.ipynb](Simulations.ipynb) so that some of its functions can be used in [PaperScape_Data.ipynb](PaperScape_Data.ipynb).
### Simulated Citation Networks and Theory Implemenation
[Simulations.ipynb](Simulations.ipynb) is the notebook which all the simulated citation networks following Price's model were 
created. The visualization functions are spread throughout the notebook, usually following the functions that develop the data
to be visualized. 

### arXiv Citation Networks and Comparison with Theory
[PaperScape_Data.ipynb](PaperScape_Data.ipynb) is the notebook where all the arXiv citation networks are created and analyzed 
