# Web Search and Information Retrieval
## Course Summary

[TOC]

# Intro

## What is Information Retrieval?
Information retrieval is the research field that deals with the design, implementation, evaluation, and analysis of systems that help users find useful portions of data
stored on computers.

## Historical Background
### 5-minute exercise

- What are problems when sorting by author?
	- Ambiguous names, same names

- What is necessary to organize library cards by subject?
	- Some kind of topology
	- Some cards will fit into different categories

- Librarians can now dig up books for you by author, by title, by subject. What is still missing?
	- Term search/Full text search

# Architecture of a Search Engine

## Requirements for search engines

- Effectiveness
	- Quality / Most relevant set of documents for a query
		Needs: Sophisticated text statistics

- Efficiency
 	- Speed / Process queries as quickly as possible
 		Needs: Special data structures

## Two processes
- Indexing: Build structures that enable searching
- Query: Use structures + query for ranking

## High-level building blocks

![Indexing building blocks](images/building_blocks.png)

---

## Indexing

### Text acquisition
Task: Identify and make available documents to be searched

Components:

- Crawler
- Feed Reader
- Converter
- Document Store

### Crawler
Task: Responsible to identify and acquire documents

Web Crawler: Follows links to discover new web pages

### 2-minute Exercise: What are challenges for web crawling?

- Don't fall into loops
- Keeping freshness / When to recrawl?
- Manage huge volume

### Feed reader
Task: Similar to crawling; identify and acquire documents

### Converter
Task: Create plain text from crawls and feeds

Problems: Variety of formats, text encoding

### Document store
Task: Manage large document collection and metadata

Why? Documents are available on the web?

- Fast access
- Orignal not always accessible

### 2-minute Exercise: Why redundant local mirroring of the documents?

- Keep data close to the user
- Fallback in case of node fallout

### Text transformation
Task: Create index terms and features from the text

- Parts of the document are getting stored in the index and are used for searching
- Index terms can be: words, phrases, named entities, dates, links, etc.

Components:

- Parser
- Stopping
- Stemmer / Lemmatizer
- Link Extraction
- Information Extraction
- Classifier

#### Parser
Task: Process token sequence and recognize document structure (title, body, . . . )

- Tokenizing the text
- Important: Query has to be tokenized the same way!
- Keeping important information about document (e.g. words in heading more important than in body)

### 2-minute exercise: What might be problems with alphanumeric tokens?

- Special chars
- Uppercase/Lowercase
- Apostrophe: O'Connor - Owner's

#### Stopping
Task: Remove common words from token stream
- Problem: "to be or not to be"

#### Stemmer / Lemmatizer
Task: Group words from a common stem

- Idea: "statistics" should also match “statistic” and “statistical”

Stemming can produce non-word terms. Lemmatizing keeps terms readable.

### 2-minute exercise: What are problems related to aggressive stemming?

- Can cause false postives.

#### Link extraction
Task: Extract links and anchor texts

- Anchor text often describes the page the link points to
- Link analysis like PageRank makes extensive use of link structure
- Anchors enhance text content of the linked document
- Links and anchors can significantly improve effectiveness

#### Information extraction
Task: Identify more complex index terms

- Words in bold or headings
- Noun phrase detection through POS (part-of-speech) tagging
- Named entity recognition (names, companies, locations, dates, phone numbers, ...)

#### Classifier
Task: Identify and assign class-related metadata

- Assign labels (categories) to documents
- Spam classification
- Non-content part identification (Ads)
- Clustering used to group without predefined categories: Importand for ranking and user interaction

### Index creation
Task: Create data structures from transformed text

- Must be efficient with respect to time and space
- Efficient updates
- Common form: Inverted Index
- Particular form is very important

Components:

- Document statistics
- Weighting
- Inversion
- Distribution

#### Document statistics
Task: Gather and record statistical information about words, features, documents

- Frequencies of index terms
- Position of index terms in documents
- Frequencies over document groups
- Document lengths
- Statistics stored in lookup tables

- Reieval model and ranking determine the required statistics!

#### Weighting
Task: Calculate weights for words in documents

- Index term weights reflect relative importance in documents: Needed for ranking
- Pre-computed due to efficiency
- tf-idf:
	- Idea: High weights for terms that occur in few documents
	- tf: term frequency - occurences in document
	- idf: inverse document frequency - occurences in collection

#### Inversion
Task: Change document-term information to term-document information

#### Distribution
Task: Distribute index over multiple computers and network sites

- Either document or term distribution
- Replication

### 2-minute exercise: What are arguments for sharding by documents, by terms, and replication?

- documents: smaller indexes are faster.
- term: based on query terms, only a few machines need to be accessed
- replication: faster access to closer machine, fallback in case of fallouts

---

## Query Process

![Query building blocks](images/query_building_blocks.png)

### User interaction
Task: Interface between the user and the search engine

- Accept user query and transform into index tersm
- Take ranked list from se and organize into results
- Offer query refinements

Components:

- Query input
- Query transformation
- Results output

#### Query input
Task: Provide interface and parser for query language

- In state-of-art web search mostly simple query languages but variety of operators possible

#### Query transformation
Task: Improve initial query

- Tokenizing, stopping, stemming as with documents
- Spell checking and query suggestion
- Query expansion
	- Suggest or add additional terms. Usually from analyzing term occurrences in documents
	- Relevance feedback expands by terms from user-identified relevant documents or simply terms from the top search results

### 2-minute exercise: What problems do you see with relevance feedback?

- Might be difficult to identify what is relevant to a user
- Using top ranked documents might lead to topic drift

#### Results output
Task: Constructing the display of ranked documents

- Snippet generation
- Highlighting important words
- Clustering the output to show groups of related documents
- Find and display ads
- Even translation of results from other languages

### Ranking
Task: Generate ranked list of documents

- Core of a search engine
- Must be efficient (many queries in short time) and effective (relevant results)
- Efficiency depends on indexes, effectiveness on retrieval model

Components:

- Scoring
- Optimization
- Distribution

#### Scoring
Task: Calculate scores for documents

- Based on the ranking algorithm (which is based on the retrieval model)
- Features and weights used must be related to topical and user relevance
- Basic form: q_i * d_i

### 2-minute exercise: Can you imagine what the difference between topical and user relevance is?

TODO

#### Optimization
Task: Design ranking algorithms and indexes to decrease response time and increase throughput

- Term-at-a-time scoring
	- Access index for a query term
	- Compute contribution of that term for a document’s score
	- Add contribution to an accumulator (score for a document is only available at the end)
	- Access next index

- Document-at-a-time scoring
	- Access all query term indexes in parallel
	- Compute scores by moving pointers through the indexes to find documents with all the terms
	- Final document score calculated immediately

#### Distribution
Task: Decide how to allocate queries to processors and assemble final ranked list

- Query broker depends on form of index distribution
- Which shards/replicated copy to access?
- Caching

### Evaluation
Task: Measure and monitor effectiveness and efficiency

- Record and analyze log data (user + system logs)
- Results used to tune ranking
- Offline activity (apart from logging)
- Critical part of any search application

Components:

- Logging
- Ranking analysis
- Performance analysis

#### Logging
Task: Log users’ queries and interactions

- Most valuable source of information for tuning effectiveness and efficiency
- Query logs useful for spell checking, query suggestion, query caching, match ads, etc.
- Clicked documents tend to be relevant
- Clickthrough data is important
- Also dwell time (time spent reading a document)
- Click-through often used to train ranking algorithms (learning-to-rank framework)

#### Ranking analysis
Task: Measure and compare effectiveness via logs and relevance judgments

- Explicit relevance judgments for (query, document) pairs
- Costly but extremely valuable source for parameter tuning
- Often crowdsourcing is applied to gather judgments
- Variety of evaluation measures available
- In web search measures that emphasize the quality of the top results are common

#### Performance analysis
Task: Monitoring and improving system performance

- Typical measures are response time and throughput
- In distributed environments network congestion also important
- Controlled environment via test collections
- Also simulation as a possibility

## Summary

- Two main processes: indexing and query process
- Indexing process: text acquisition, text transformation, index creation
- Query process: user interaction, ranking, evaluation
- Document store and index as the connections
- Logs as important means for parameter tuning

---