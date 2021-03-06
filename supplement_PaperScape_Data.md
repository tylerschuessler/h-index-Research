####################################################################################\
DOCUMENT 1: The following is pertinent to the .ipynb for real arXiv citation networks\
####################################################################################\

For the real citation networks I would advocate for using the .ipynb file, it has nice flow. Most of the functions have comments describing their functionality, but hopefully this guide can help step whoever has to pick their way through an entire years worth of code.

1. Make sure you have all the imports installed. I recommend the anaconda package manager, you can very easily install packages that are not in the base install.

2. You will likely need to change the file path/directory in return_filenames(), depending on where the data is located.

3. There are a few different dictionaries I implemented to organize the papers and authors depending on what I needed to do with them. All the dictionaries do though is reference the papers or authors in different ways; they all modify the same object.

4. The Primary approach Section just sets up the citation network. All functions are defined above, then calls to those functions are made later. If a function is not called it is unnecessary for building the actual network.

5. I implement objects representing papers. Note that the first field listed in the data is assumed to be the field the paper is in. This is slightly different in the Second approach.

6. All the necessary functions are implemented and dic_by_field is a dictionary containing all the papers associated to a field. The keys of the dictionary are just the string names of the field.

7. Secondary approach isn\'92t implemented, by choice. The difference between the two methods is that in Secondary approach a paper can be part of multiple fields, but the same assumptions still hold. A papers only obtains citations from within its field. What this means is in the Secondary approach, papers which are technically the same are is different fields and have different citations depending on the field.

8. The next Section is Begin Analysis. In this section, we assign order to the papers. Specifically we organize the papers based on their index of publication and then assign a numeric ordering \{1,...,n\}.

9. moving_avg and gt_avg are some functions developed to display the citation count of the jth paper, by taking a moving average to smooth out some of the variability present in a single field. Neither of these functions is necessary for the implementation of the actual networks

10. Throughout this document, there are a number of functions for visualization. They all produce output in the .ipynb so implementation of them is all commented out. Since plots are made for every field they can take a long time to produce and slow down the running time of the code, and the notebook becomes really cumbersome when they are all displayed. None of them are necessary for constructing the networks.

11. collect_important_fields resets the global variable fields used throughout the document to be a subset of all the fields. Fields must have at least 1000 papers to be considered important.

12. In the next section, I move on to analyzing authors. The first thing to note is the author object similar to the paper object is accessed and modified in a variety of way. However, all author operations take place on the same author objects, with one for each unique author.

13. I assign each unique author all of their relevant papers and the list of when these publications were made. Then I calculate the h-index of each author and assign it to that author. I also tabulate all the h-indices for all authors with m publications for all possible m in each field.  

14. The next section deals with fitting the c and a parameters for Prices model. In this section, I tried many different methods to fit a with desired results. The final method that is used it the only that remains uncommented. It may be worthwhile to try to fit the in-degree distribution. I fit only the tail distribution.

15. In regress_a originally, I was attempting to find a from the in-degree distribution, which has a lot of non-linearity. I later found this infeasible, thus, regress_a is just used to store the in-degree distribution which is used to find the tail distribution and can be plotted with plot_min_mse.

16. The next section is for comparing the theory we developed with the real citation networks. It requires importing some functions from Simulations.py. 

17. Throughout this section I refer to the h-index distribution for all m, which is the probability distribution found using the law of total conditional probability. Whereas the h-index distribution for a given m is the conditional probability of the h-index given m.

18. m is always the number of papers an author has published

19. The next section is mostly plotting functions, to compare theoretical results with the actual citation networks.

20. The next section is for creating the "synthetic" authors.

21. the final section deals with modifying our distribution to account for the window size of an author. This section is not in the paper and was implemented at the very end of the research.

Good Luck!
