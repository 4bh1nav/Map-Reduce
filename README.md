Map-Reduce
==========



Problem 1: To use map reduce to create inverted index Command to run cd inverted-index python inverted_index.py book.py

Problem 2: To implement a relational join as Mapreduce query Command to run cd relation_join python join.py records.json

Problem 3: Consider a simple social network dataset consisting of key-value pairs where each key is a person and each value is a friend of that person. Describe a MapReduce algorithm to count he number of friends each person has. Command to run cd friend_count python friends.py friends.json

Problem 4:The relationship "friend" is often symmetric, meaning that if I am your friend, you are my friend. Implement a MapReduce algorithm to check whether this property holds. Generate a list of all non-symmetric friend relationships. Command to run cd assym python assym.py assym.json

Problem 5:Consider a set of key-value pairs where each key is sequence id and each value is a string of nucleotides, e.g., GCTTCCGAAATGCTCGAA....

Write a MapReduce query to remove the last 10 characters from each string of nucleotides, then remove any duplicates generated. Command to run cd dna python dna.py dna.json

Problem 6:Assume you have two matrices A and B in a sparse matrix format, where each record is of the form i, j, value. Design a MapReduce algorithm to compute matrix multiplication: A x B Command to run cd matrix_mult python matrix_mult.py matrix_mult.json
