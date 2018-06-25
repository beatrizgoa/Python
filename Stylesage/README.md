# StyleSage.
####  Beatriz Gómez Ayllón

## Project directory structure
The project is formed by the following files and folders:
* requirements.txt
* assest: Where the original csv files are saved.
* src: where the code is, and has the following structure
    * loadSave
        * loadData.py
        * saveSCV.py
    * visualizations
        * visualization.py
    * basicPreprocessing
        * rawDataAnalysis.py
        * utils
            *  analizingDataFunctions.py
    * filterData
        * filterData.py
        * utils
            * categoricalToNumerical.py
            * mergeDatasets.py
            * normalize.py
            * removeOutliers.py
    * estimation
        * estimation.py
    * main.py


## Project approach
The project has been presented as a regression one. The main.py file runs the functions necessaries to execute the whole project. And the steps that follow is:
* The four csv files are loaded (train, test, users and products).

* A basic pre-processing is carried out (delete duplicated rows if exist and analyze nulls cells) for each subset (train, users and products). This process is developed mainly in rawDataAnalysis.py. I decided not to remove null rows because the null values affect (only)the product information and the product description and those two columns are not going to be used in the solution approach.

* For analyzing the data, the code follows in the same rawDataAnalysis.py python file. The click count description is obtained, as well as the click count distribution, the most of the tag_id has 0 or 1 click, and just a few numbers of samples are higher than 1000 clicks. Then, the date is observed, the number of new users increases exponentially in the lasts days. The training and the testing dates are in the same range. 

* The following step starts in the filterData.py, where first: the 'brand_name' from products, 'country' and 'date joined' from users and 'date_tag' from train and test subsets is transformed into numeric values. Then, 'brand name', 'country' and 'users' values are added to the training and test subsets. This part of the code takes some time running.

* In the same function (filterData.py), to visualize the new data, a correlation matrix is plotted and we can see the date of the user joining and the user id are correlated, id_tag and date post are correlated and id_tag and id_post. Also is visualized the number of clicks in function of the brand, country, color and date. 

* After the analysis, the data wich click counts are higher than 1000 is considered outliers and they are removed. The following columns are normalized in order to have normalized values: 'tag_id', 'post_id', 'product_id', 'user_id' and 'product brand'. From this process a warning pops out (the code continue working and running). The filterData function ends here.

* In stimating.py python file, the task continues in the main function trainPredict(), where, first, the importance of each feature is analyzed using random forest regressor. From this analysis and the previous ones, the columns that are going to be used are: 'tag_id', 'post_id',  'product_id' and  'user_id'.

* The selected features are used to train a random forest classifier. It is searched the best number of trees of the estimation task and then, the classifier object is trained again with the best number of trees and test data is predicted and saved as asked.

* The main.py file is the one which has to be executed because the rest of the code id called from that file.


## Executing the code
The code has been programming using python 3.6, the envirnoment and the requiriments.txt are provided.
The code should be run in the main directory, not in the src directory because other python files are imported such as src.subfolder.pythonScript.py. The main file is the one which has to be executed.

