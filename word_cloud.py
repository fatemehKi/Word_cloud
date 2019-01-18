# author fatemeh

import collections

file="""" 
bands which have connected them with another, and to assume among the
powers of the earth, the separate and equal station to which the Laws
of Nature and of Nature's God entitle them, a decent respect to the
opinions of mankind requires that they should declare the causes which
impel them to the separation.  We hold these truths to be
self-evident, that all men are created equal, that they are endowed by
their Creator with certain unalienable Rights, that among these are
Life, Liberty and the pursuit of Happiness.--That to secure these
rights, Governments are instituted among Men, deriving their just
powers from the consent of the governed, --That whenever any Form of
Government becomes destructive of these ends, it is the Right of the
People to alter or to abolish it, and to institute new Government,
laying its foundation on such principles and organizing its powers in
such form, as to them shall seem most likely to effect their Safety
and Happiness. """

# Cleaning text and lower casing all words
for char in '-.,\n':
    file=file.replace(char,' ')
file = file.lower()

#splitting the file into the words
f_wordlist = file.split()

# initializing/creating a dictionary to keep record of the words and the number of those
dic = {}
for i in f_wordlist:    
    dic[i] =dic.get(i,0)+1
    
#sorting the list based on the number of repeatation
sorted_list = []
for wo, fre in dic.items():
    sorted_list.append((fre,wo))
sorted_list.sort(reverse=True)
