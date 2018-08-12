import re  #library for regular expressions
import collections  #ibrary that allows us to count the occurrences of words

text = open('book.txt').read().lower()
words = re.findall('\w+', text)
print(collections.Counter(words).most_common(10))