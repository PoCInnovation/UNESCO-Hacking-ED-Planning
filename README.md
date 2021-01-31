# Athena

## What is Athena
**TODO**


## How to use it ?
1. Need to have ```dependencies``` installed
```bash
pip3 install -r requirements.txt
pip3 install jupyterlab
pip3 install notebook
```

## How to test our NLP process ?
You can access to notebook exemple in `exemples/` folder.\
To run our exemple just type: `jupyter notebook <path_to_file>`.\
All the files of the jupyter notebook are in the directory ```examples/```.\
In particular, you can find two jupyter notebook ```multiples_predictions.ipynb``` and ```single_analysis.ipynb```.

For example if you are in root of repo:
```bash
jupyter notebook exemples/multiples_predictions.ipynb
# or
jupyter notebook exemples/single_analysis.ipynb 
```

Please note that you need to have installed jupyter to run our notebooks.\
For more inforlations please refer to: [jupyter.org/install](https://jupyter.org/install)

# How's does it work ?
## NLP:
Going over the whole NLP process and how does it work is out of the scope of this document but we will see the main parts and why whe choosed Transformers rather than RNNs.\

Back to few years ago, most of the people who wanted to work with NLP was using RNNs but in 2017 a new deep learning model has been introduced: the Transformers\
We will not go into the deep why are Transformers so much better than RNNs but if there is one thing to remember: [Attention is all you need](https://arxiv.org/abs/1706.03762)...\
The Transformer model is able to look at every position in the sequence, at the same time, in one operation resulting in a huge improuvement over RNNs.

### Our process:

The first step in every project, NLP included is to analyse the probleme to better solve it.\
The second challend is parse and fetch needed information from raw data to build our solution, for this part we worked with text analysys and regex.\

Finally the data in hand we could set and use our Transformer model, we decided to work with [Hugging face's Tranfomers library](https://huggingface.co/transformers/) for it convienient and it low ressources cost.\
(Regarding to the subject, it's important to build a solution usable by most contry including with low IT ressources countrys.)\
Once our Transformers in hand, you just add to process our analysis (Question Answering & Sentence Classification)

## Data visualisation:

# Our recommendations:
**TODO**

## Authors

 - [Valentin De Matos](https://www.linkedin.com/in/valentin-de-matos/)
 - [Tom Chauveau](https://github.com/TomChv)
 - [Roman Gascoin](https://www.linkedin.com/in/rgascoin/)
 - [Killian Clette](https://www.linkedin.com/in/killian-clette-06014b182/)
 - [Luca Georges francois](https://github.com/TomChv)
 - [Paul Cochet](https://github.com/Paul-Cochet)
 - [Coline Seguret](https://fr.linkedin.com/in/coline-seguret)
 - [Nefeli Paparisteidi](https://www.linkedin.com/in/nefeli-paparisteidi-2b479a78/)

 Made with **<3** by [PoC](https://www.poc-innovation.fr/)