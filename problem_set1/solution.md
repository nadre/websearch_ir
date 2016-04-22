#Webir - Problem set 1
Jula McGibbon & Erdan Genc

[TOC]

##Exercise 1 : IR basics

_Google - DuckDuckGo_

(a) How many of the documents are relevant for each query?
(b) What is the overlap of results between the engines for each query?
(c) Is one engine clearly better than the other? If so, by how much?
(d) How do short queries perform compared to longer ones?

1. "beatles top ten hits" - Goal: "Beatles top ten list"
    (a) G: 10/10 D: 10/10
    (b) 5/10
    (c) Nope.
    (d) Google gives more hits, results still similar.

2. "nazi demo jena 2016" - Goal: "News about demo"
    (a) G: 4/10 D: 2/10
    (b) 4/10
    (c) Google gives a news section.
    (d) Results decrease.

##Exercise 2 : IR basics
List three web services or sites that you use that appear to use search, not including web search engines.
Describe the role of search for that service. Also describe whether the search is based on a database or grep-style of matching, or if the search is using some type of ranking.

1. Dropbox - Finding files which have the same chars (grep-style).
2. Uni-Weimar.de - Finding article which have the same chars (grep-style).
3. BISON Portal - Finding events, database based.

##Exercise 3 : IR basics
Use the web to find as many examples as you can of open source search engines, information retrieval systems, or related technology. Give a brief description of each search engine and summarize the similarities and differences between them.

* ASPSeek
* BBDBot
* Datapark
* ebhath
* Eureka
* ht://Dig
* Indri
* ISearch
* IXE
* Lucene
* Managing Gigabytes (MG)
* MG4J
* mnoGoSearch
* MPS Information Server
* Namazu
* Nutch
* Omega
* OmniFind IBM Yahoo! Ed.
* OpenFTS
* PLWeb
* SWISH-E
* SWISH++
* Terrier
* WAIS/ freeWAIS
* WebGlimpse
* XML Query Engine
* XMLSearch
* Zebra
* Zettair


__Storage Indicates__ the way the indexer stores the index, either using a
database engine or simple file structure (e.g. an inverted index).

__Incremental Index__ Indicates if the indexer is capable of adding files to an
existent index without the need of regenerating the whole index.

__Results Excerpt__ If the engine gives an excerpt (“snippet”) with the results.

__Results Template__ Some engines give the possibility to use a template for
parsing the results of a query.

__Stop words__ Indicates if the indexer can use a list of words used as stop
words in order to discard too frequent terms.

__Filetype__ The types of files the indexer is capable of parsing. The common
filetype of the engines analyzed was HTML.

__Stemming__ If the indexer/searcher is capable of doing stemming operations
over the words.

__Fuzzy Search__ Ability of solving queries in a fuzzy way, i.e. not necessarily matching the query exactly.

__Sort Ability__ to sort the results by several criteria.

__Ranking__ Indicates if the engine gives the results based on a ranking func-
tion.

__Search Type__ The type of searches it is capable of doing, and whether it
accepts query operators.

__Indexer Language__ The programming language used to implement the
indexer. This information is useful in order to extend the functionalities or
integrate it into an existent platform.

__License__ Determines the conditions for using and modifying the indexer
and/or search engine.

(wrg.upf.edu/WRG/dctos/Middleton-Baeza.pdf)

##Exercise 4 : Search engine architecture
A more-like-this query occurs when the user can click on a particular document in the result list and tell the search engine to find documents that are similar to this one. Describe which low-level search engine architecture components are used to answer this type of query and the sequence in which they are used.

We basically have four ideas to do this:
1. Do a new query with the title of the hit result
2. Get the keyphrases or any other descriptive words of the document and do a query with them
3. If there's already a similarity measure between documents, when can just use this
4. Use the index log to find similar documents that other users have choosen

Depending on the implementation the SE would have to get information from the index, feature store or has to analyze the document from document store.

##Exercise 5 : Crawling
###What are some reasons for building a search engine for only the small collection?
* Small indexes are much faster.

###What are some reasons for building a search engine that covers both collections?
* Every indexed document at least answers the question: "Where is this document?"
* Every document indexed increases number of answerable questions
* The task of seperating good from bad documents is the job of the ranking algorithm