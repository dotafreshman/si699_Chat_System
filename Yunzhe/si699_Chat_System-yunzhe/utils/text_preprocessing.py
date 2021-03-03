## 
# description: This function removes url links of a corpus.
# params: 
#      - corpus_list: a list of all texts to remove url links inside them.
# return: 
#      - result_corpus_list: a list of all texts where url links are removed.

def remove_urls(corpus_list):
    import re
    urls = re.compile(r'[http|https]*://[a-zA-Z0-9.?/&=:]*', re.S)
    
    result_corpus_list = []
    for uncleaned_text in corpus_list:
        cleaned_text = re.sub(urls, '', uncleaned_text)
        result_corpus_list.append(cleaned_text)
    
    return result_corpus_list




