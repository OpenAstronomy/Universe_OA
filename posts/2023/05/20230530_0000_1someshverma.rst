.. title: Utilising community bonding period Effectively!
.. slug:
.. date: 2023-05-30 00:00:00 
.. tags: radis
.. author: 
.. link: https://1someshverma.github.io/UtilisingCommunityPeriod/
.. description:
.. category: gsoc2023


.. raw:: html

    <p>I started to contribute to RADIS from January’23 and whenever i needed help in some issue , mentors were quite helpful in providing revelant information to resolve that issue . And this thing helped me , to develop good bonding and understanding with the mentors .</p>
    
    <p>So,I thought, i should use community bonding period more productively thus, i decided to work on project from 15 May .</p>
    <!-- TEASER_END -->
    
    <p>In community bonding period i have done following things -</p>
    
    <ul>
    <li>Read the RADIS and HITRAN Paper (selected parts)</li>
    <li>Worked on Loading the dataframe in Vaex format (task of first week)</li>
    </ul>
    
    <h5 id="loading-dataframe-in-vaex-format">Loading Dataframe in Vaex format</h5>
    <p>There are two main functions which are used load databank in RADIS
    These are :</p>
    <ul>
    <li>fetch_databank()</li>
    <li>load_databank()</li>
    </ul>
    
    <p>fetch_databank() : It is used to load databank from standard databank like HITRAN,HITEMP,EXOMOL,GEISA by fetching it from their respective APIs, then parsing and processing them.</p>
    
    <p>load_databank() : It is used to load databank from the local file or to load databank from user defined databank .</p>
    
    <p>Upto now, i have worked on fetch_databank() function to load dataframe in Vaex format , some of the things were already implemented while at other points i needed to write code specifically for vaex dataframe format.</p>
    
    <p>Similarly, for load_databank() function , the hurdle was to parse it in vaex dataframe format as virual columns which are used in vaex dataframe to reduce memory use , it was throwing error . After trying many i finally found a fix for it .</p>
    
    <p>Now, I have made necessary changes to these two functions to load dataframe in Vaex format. Next week i will be working on writing test cases for these.</p>

