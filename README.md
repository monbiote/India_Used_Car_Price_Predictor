# Final Project-Used Car Predicton

This project evaluates multiple machine learning models and finds the best one to predict the prices of second hand cars in India. 

### Installation instructions

To install our library:

( create a virtual environment (conda: conda create --name name_of_environment python 3.12) and activate the environment (conda: conda activate name_of_environment)
- locate your work directory to the library folder "folder_lib" (using terminal: cd path)
- run in terminal "pip install -e." when located in the main library folder.

You should then be able to import the functions from within the library (example: used_car_prediction_lib.data_read.reader, used_car_prediction_lib.data_process.deleteProcessor).


### Library Structure "folder_lib"
```
project
│   README.md
│   file001.txt    
│
└───folder1
│   │   file011.txt
│   │   file012.txt
│   │
│   └───subfolder1
│       │   file111.txt
│       │   file112.txt
│       │   ...
│   
└───folder2
    │   file021.txt
    │   file022.txt
```

.
+-- _config.yml
+-- _drafts
|   +-- begin-with-the-crazy-ideas.textile
|   +-- on-simplicity-in-technology.markdown
+-- _includes
|   +-- footer.html
|   +-- header.html
+-- _layouts
|   +-- default.html
|   +-- post.html
+-- _posts
|   +-- 2007-10-29-why-every-programmer-should-play-nethack.textile
|   +-- 2009-04-26-barcamp-boston-4-roundup.textile
+-- _data
|   +-- members.yml
+-- _site
+-- index.html

We constructed our whole project using classes that were placed in library structure that made the most sense to us. The objective of this was to create a clear library structure that would allow new collaborators to quickly understand our project and then be able to improve it simply.

This README file birefly summarizes our methodology and motivates the library structure we have build so far, while also showcasing the resul we obtained. 
Finally and most importantly, we also present several suggestion and improvements that could be brought to our project.




we first started by exploring the d



This project is predction of used car

Our project is preparing data, cleaning data and computing data in the end.

We first build function to each operation blocks and remove dupilcation. 
After that, we refactory functions to classes 
and then build entire unittest to make sure the desired behavior.
