
data_dir = r'E:\msc\semIII\NLP project\Language_Identifier\data_dir'
# Select to articles from file
num_of_articles = 10000
# Maximum sequence length
sentense_len = 150
# shingle configs
shingles_range = (70, 100, 130)
# how many shingles generate per line
shingle_per_line = 10 
# out of vocabulary token
oov_str = 'oov'

lang_code_dict = {
    'en':'english', 'de':'german', 
    'fr':'french', 'it':'italian', 
    'es':'spanish'
}

data_info = {
    'en' : data_dir + '/wiki.en.text',
    'de' : data_dir + '/wiki.de.text',
    'fr' : data_dir + '/wiki.fr.text',
    'it' : data_dir + '/wiki.it.text',
    'es' : data_dir + '/wiki.es.text',
}

for lang_code, file_path in data_info.items():
    print(lang_code, lang_code_dict[lang_code], file_path)
	
# data loading
data_dict = {}
for lang_code, file_path in data_info.items():
    with open(file_path, encoding='ISO-8859-1') as file:
        lines = file.readlines()
        lines = lines[:num_of_articles]
        # convert to lower case
        lines = [l.lower().strip() for l in lines]
        data_dict[lang_code] = lines
        print(lang_code, len(lines))
