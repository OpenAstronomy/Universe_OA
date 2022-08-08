.. title: GSoC Blog #1
.. slug:
.. date: 2022-07-02 06:31:49 
.. tags: stingray
.. author: AMAN PANDEY
.. link: https://medium.com/@aman_p/gsoc-blog-1-cc0c0995d56e?source=rss-1bafed5b4c37------2
.. description:
.. category: gsoc2022


.. raw:: html

    <figure><img alt="" src="https://cdn-images-1.medium.com/max/680/0*kmysU0LzpIzm8qV4.jpeg" /></figure><p>Its time for my first blog during the coding period! We are into our 3rd week in the coding period, and already the journey is getting exciting, a little challenging, of course, but I am enjoying it. As I had mentioned in the earlier blog, I started the initial week with implementing the helper functions, Fourier analysis, and tests related to them from Python to Julia. By god, it was not an easy way through.</p>
    <p><strong>Dealing with tests</strong></p>
    <p>I started by understanding what the functions inside fourier.py did and quickly realized that without running tests, I would have a hard time working out the insides of some of the methods. I thus, started writing functions is Julia, understanding the parameters and their types and using external packages like ResumableFunctions or Statistics wherever necessary. After implementing normalizations for arrays, I worked on tests where the problems began. Out of Index errors, types not supported, and the same functionality implemented differently in Julia and Python started to take most of my time.</p>
    <!-- TEASER_END -->
    <p>For example, to create a histogram, we use <em>NumPy.histogram, </em>pass it an array and number of bins, and it returns the required histogram in a tuple. For Julia, I had to use the package StatsBase, then call fit(Histogram, array, bins), which generates an object whose weight property is my result. But that is the fun. I’m slowly adjusting to handling such codes without class methods, which will be very necessary for this and the next week, as I look forward to implementing LightCurves and EventLists classes of the python package.</p>
    <p>Data handling, which I thought initially to be challenging, was although a smooth experience. Using the DataFrame package with the MetaData package turned out to be a very flexible approach while working with tables. I quickly implemented a large sample data using the HDF5 format suggested by my mentor.</p>
    <p><strong>Making the PR</strong></p>
    <p>I was about to complete this work when the government made the internet in my area inaccessible due to local protests. I couldn’t work that efficiently for three days and definitely couldn’t communicate with my mentor. After the internet was back, I quickly sorted out some issues and made a PR, but it wasn’t too good to be merged due to a few reasons. I didn’t provide type-annotations on the functions as many arguments were nothing (null in Julia), and providing types on them would cause the function to produce an error. My code also had some memory allocation and performance issues. The most encouraging thing was how my mentor Mosè cooperated with these issues. He advised me on many things, provided me with quick fixes, and commented on learning from these mistakes. I am certainly looking to fix these problems as soon as possible, learning along to write practical and high-performance Julia code.</p>
    <p><strong>The problem now</strong></p>
    <p>I quickly changed the code to be type annotated as I already knew about the types while understanding the codebase. There were not many type instabilities as I already had checked my functions with @code_warntype macro, and it was mostly clean. The main problem I’m facing now is unlike Python, Julia doesn’t have a tradition of defaulting values with null and checking if it’s null to provide more functionality ahead in code. This is the result of one of my @code_warntype runs:</p>
    <figure><img alt="" src="https://cdn-images-1.medium.com/max/1024/1*nVtVLI6OIUyMQ9TqlIbqtQ.png" /><figcaption>The Yellow Colour Indicates a type-instability, though it maybe important to use Unions of Nothing and a Concrete Datatype, thus it is only a warning (not red)</figcaption></figure><p>The code is not entirely Julian, and the tests take slightly longer to run compared to Python.</p>
    <figure><img alt="" src="https://cdn-images-1.medium.com/max/840/1*dJ7COYI3hPgd-O3OYiv65w.png" /><figcaption>Python tests run in 3.9s on avg</figcaption></figure><p><strong>Next two weeks</strong></p>
    <p>I intend to implement creating and working with LightCurves and then move on to EventLists and implement related helper functions and filters. My approach now will be to understand and sketch the functioning with a thorough working of tests and then implement it from scratch in a Julian way. Alongside, I will be improving the fourier.jl functions with what I learn and hope to get the PR merged by the start of the following week. I will be back with some more accounts of this exciting journey!</p>
    <img alt="" height="1" src="https://medium.com/_/stat?event=post.clientViewed&amp;referrerSource=full_rss&amp;postId=cc0c0995d56e" width="1" />

