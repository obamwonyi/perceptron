# Development of a perceptron learning model for Iris Setosa, Veriscolor, Sepal length and Petal length

## Full project structure
```shell
.
├── documentation.md
├── main.py
├── __perceptron.py
├── run.sh
└── src
    ├── data_loader.py
    ├── __init__.py
    ├── model_trainer.py
    ├── perceptron.py
    └── visualizer.py

```


*   main.py 
    >  The main.py file is the programs entry point, this is where all the other features of the 
    > project are pooled and utilized as modules
    > 
*   src
    > The folder holds all the modules that would be pooled to the main file
    > 
*  src/perceptron.py
    > This is the class implementation of the perceptron to be trained and utilized.


## Run code 
Use the shell command below to run the code from your terminal. <br>
If you use windows, use powershell or Gitbash in place of a terminal, or preferably use WSL
```shell
./run.sh
```

<b> The first output is that of Epoch  while the second is that of Setosa and Versicolor</b>