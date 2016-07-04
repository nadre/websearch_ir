#Web Search and Information Retrieval
###June 17, 2016
#Problem set 3

###Exercise 1 :  Abstract Ranking Model
We introduced an abstract model of ranking, where documents and queries are represented by features. What are some advantages of representing documents and queries by features? What are some disadvantages?

---

##### Advantages
- Fast. (Document-)Features  can be precomputed.
- Easy. Score is calculated by the dot product of two feature vectors.

##### Disadvantages
- Grammar, word order and proximity are not being regarded. (Document is a Bag-of-words)

###Exercise 2 :  Abstract Ranking Model
Our model of ranking contains a ranking function R(Q, D), which compares each document with the query and computes a score. Those scores are then used to determine the final ranked list.

An alternate ranking model might contain a different kind of ranking function f(A, B, Q), where A and B are two different documents in the collection and Q is the query. When A should be ranked higher than B, f(A, B, Q) evaluates to 1. When A should be ranked below B, f(A, B, Q) evaluates to −1.

If you have a ranking function R(Q, D), show how you can use it in a system that requires one of the form f(A, B, Q). Why can you not go the other way (i.e., use f(A, B, Q) in a system that requires R(Q, D))?

---

We can simply compare the ranking of the documents:

    x = R(Q, A) - R(Q, B)
    if (x > 0) return 1
    else return -1

The other way around doesn't work since we need a ratio value to sort, which can't be obtained by f(A, B, Q).

###Exercise 3 :  Abstract Ranking Model
Suppose you build a search engine that uses one hundred computers with ten million documents stored on each one, so that you can search a collection of one billion documents. Would you prefer a ranking function like R(Q, D) or one like f(A, B, Q) (from the previous problem)? Why?

---

Ranking R(Q, D) is preferred. This way the we don't need to transfer the documents (or at least their features between the machines). Every computer would calculate the ranking of their documents and send the results together with the document id to lets say a major machine which would then sort all the results. Network traffic as well as computational effort would be highly reduced.

###Exercise 4 :  Abstract Ranking Model
Documents can easily contain thousands of non-zero features. Why is it important that queries have only a few non-zero features?

---

- Speeds up the scoring
- The higher the number of non-zero features of the query, the more similar the scoring of the documents will be.

###Exercise 5 :  Abstract Ranking Model
Suppose your search engine has just retrieved the top 50 documents from your collection based on scores from a ranking function R(Q, D). Your user interface can show only 10 results, but you can pick any of the top 50 documents to show. Why might you choose to show the user something other than the top 10 documents from the retrieved document set?

---

If I know anything about the users context it would be good to pick those documents which are related. For example, based on query logs I know the user wants to buy a new car and he now queries "jaguar". Based on this information, it would be good to show the top 10 documents out of the 50 which are related to cars and not to animals.

###Exercise 6 :  Inverted Index
Indexes are not necessary to search documents. Your web browser, for instance, has a “Find” function in it that searches text without using an index. Also the UNIX tool grep does not use an index. When should you use an inverted index for text search? What are some advantages of using an inverted index? What are some disadvantages?

---

Indexing usually shifts the computing effort of finding an expression in a document or a collection of documents towards a storing effort by restructuring the corpus into a more search friendly form (index).

Indexing should be considered if:

- Offline precomputing is an option
- Search is used frequently (Search Engine)
- Search should be very fast
- Collection is huge
- Collection doesn't change very frequently
- Data storage is not an issue

###Exercise 7 :  Inverted Index
We have seen many different ways to store document information in inverted lists of different kinds. What kind of inverted lists might you build if you needed a very small index? What kind would you build if you needed to find mentions of cities, like Los Angeles or São Paulo?

---

???

###Exercise 8 :  Compression
We created an unambiguous compression scheme for 2-bit binary numbers (cf. Slide 290). Find a sequence of numbers that takes up more space when it is “compressed” using our scheme than when it is “uncompressed.”

---

    1, 1, 1, 1, 1 -> 101, 101, 101, 101, 101

###Exercise 9 : Compression
Suppose a company develops a new unambiguous lossless compression scheme for 2-bit numbers called SuperShrink. Its developers claim that it will reduce the size of any sequence of 2-bit numbers by at least 1 bit. Prove that the developers are lying. More specifically, prove that either:

- SuperShrink never uses less space than an uncompressed encoding, or
- There is an input to SuperShrink such that the compressed version is larger than the uncompressed input.


You can assume that each 2-bit input number is encoded separately.

---

???


###Exercise 10 : Compression
Why do we need to know something about the kind of data we will compress before choosing a compression algorithm? Focus specifically on the result from the previous exercise.

---

Information about the data makes the compression most effective. For example if we know about the most frequent words in the collection, we can encode them with the shortest available bit-strings like in [Huffman-encoding](https://en.wikipedia.org/wiki/Huffman_coding).

Or if we know that our documents are very long, we can decide to use Delta-encoding in order to lower the number that are used to save the position of the word in the document.

###Exercise 11 : Skipping
Identify the optimal skip distance k when performing a two-term Boolean AND query where one term occurs 1 million times and the other term appears 100 million times. Assume that a linear search will be used once an appropriate region is found to search in.

---

    jaguar = [doc0, doc5, doc10, doc15, doc20]
    animal = [doc0, doc1, doc2, ... , doc19, doc20]

    k = 75 ?

###Exercise 12 : Skipping
In general, the optimal skip distance c (in bytes) can be determined by minimizing the quantity kn/c + pc/2, where k is the skip pointer length (in bytes), n is the total inverted list size (in bytes), and p is the number of postings to find. Explain why the expression holds.

Plot the function using k = 4, n = 1, 000, 000, and p = 1000, but varying c. Then, plot the same function, but set p = 10, 000. Notice how the optimal value for c changes.

Finally, take the derivative of the function kn/c + pc/2 in terms of c to find the optimum value for c for a given set of other parameters (k, n, and p).

---

???


