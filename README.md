
<h1>Language_Identifier</h1>

<li>In Natural Language Processing, language identification is a task of predicting the language present in a document based on the contents of the document.</li>
<li>We often encounter chrome showing a popup to translate a webpage when it detects that the content is not in English.</li>
<li>It is important to know which language the text is in, so that the other actions(i.e. text  generation, translation, text summarization) can be performed better.</li>
<li>Language Identification is the prerequisite for the text analysis. It identifies language in the content & improves the search results.</li>

### We have implemented a Convolutional Neural Networks model:=

## Dataset

For that, we first collect the data for 5 different Latin languages.

<ol type="1">
<li>English</li>
<li>French</li>
<li>Italian</li>
<li>German</li>
<li>Spanish</li>
</ol>

We have gathered the required dataset from 3 different sources.

### [1] Wikipedia database backup dumps:

Wikipedia is taking a backup of all of it's content at https://dumps.wikimedia.org/ so it is our main data source. It contains a complete copy of all Wikimedia wikis, in the form of wiki text source and metadata embedded in XML. Files are provided in bzipped(bz2) xml format. It has already punctuations removed.

For the dataset from Wikipedia dumps we need not preprocess the data,we extract the data from .XML files using the 
#### process_wiki.py file.


### [2] European Parliament Proceedings Parallel Corpus 1996-2011: 

It is extracted from the proceedings of the European Parliament. It includes versions in 21 European language. We preprocessed the data to remove punctuations. All the files are provided in .tgz format.

### [3] Cross-Language-Dataset: 

This dataset is a multilingual, multi-style and multi-granularity dataset for cross-language textual similarity detection. More precisely, the characteristics of this dataset are the following:

it is multilingual: French, English and Spanish. it proposes cross-language alignment information at different granularities: document-level, sentence-level and chunk-level. it is based on both parallel and comparable corpora.it contains both human and machine translated text. part of it has been altered (to make the cross-language similarity detection more complicated) while the rest remains without noise. documents were written by multiple types of authors: from average to professionals.From this we have used document-level data and pre processed it to remove punctuations.

we have removed punctuation from the European Parliament Proceedings Parallel Corpus & Cross-language dataset using
#### punct.py file

Use length.py file to check the length of text files.


### Download the dataset from here:=

https://drive.google.com/drive/folders/1Yn49FGTnYU16KHsqZbbEQDNCYlk8IdLG?usp=sharing

## Implimentation

### The main libraries which we have used are as follows:

<li> gensim == 3.8.3 </li>
<li> keras == 2.4.3 </li>
<li> numpy == 1.18.5 </li>
<li> scikit == 0.22.2 </li>


We gave a language code to each of the 5 languages we are using, i.e. ‘en’ for English, ‘de’ for German, ‘fr’ for French, ‘it’ for Italian and ‘es’ for Spanish.
Then we mapped each language code to their respective training data.

### References

<li> https://dumps.wikimedia.org/backup-index.html </li>
<li> http://www.statmt.org/europarl/ Europarl: A Parallel Corpus for Statistical Machine Translation. Conference Proceedings: the tenth Machine Translation Summit </li>
<li> https://github.com/FerreroJeremy/Cross-Language-Dataset CrossLanguageDatasetLREC2016,A Multilingual, Multi-Style and Multi-Granularity Dataset for Cross-Language Textual Similarity Detection, my Ferrero and Frederic Agnes and Laurent Besacier and Didier Schwab, The 10th edition of the Language Resources and Evaluation Conference (LREC 2016) </li>
<li> https://javadeveloperzone.com/machine-learning/language-detection-neural-network/</li>


