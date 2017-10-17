<h1> Multidimentional Bloom filter</h1>


<h2> Porject presentation </h2>
<p>
	A Bloom filter is a simple, space-efficient, randomized data structure that allows to answer set membership queries on a set with a small and controlled probability of getting false positive. It is composed of a bit table and hash functions.
</p>
<p>
The aim of the project is to succesfully build a multidimentional Bloom filter distance sensitive that allow to answser to query "Does x belong to V" where x is a vector belong to U and V is a sub-space of U. 
	Other techniques have been thought to solve the probleme but none of them remain privacy preversing while keeping the inital advantages of the bloom filter.
</p>
To resolve the problem we use different methods to discretize the space:
<u>
<li> a square method; We split each dimention and keep only the closest points </li>
<li> a circle method; We suround each point and keep only the intersection </li>
</u>

<h2> Project structure </h2>
<p>
the project have been developed in python.. TODO
</p>


<h2> How to use it</h2>
<p>	
TODO
</p>