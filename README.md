# Automata Mini-Project

This program accepts either a *Computer Science Department faculty netID* or an html file from https://cs.txstate.edu/accounts/profiles/*

Some sample .html files are located in the */html* directory. The results of the query will be sent to the */results* directory.

###Walkthrough example:

Running the following:

    python main.py
         
    
will produce: 
         
     ****** CS Faculty Lookup ******
    
    Enter either: 
    
        - a CS Faculty netID, or
    
        - a path to a *.html file downloaded from http://www.cs.txstate.edu/Personnel/Faculty
    
    ---> 

At the prompt, you may enter one of two things:

1) a netID

        ---> jg66

2) a .html file

        ---> html/bg.html
        
The console and file output, in either case, will look something like this:

    Name:                   Dr. Byron Gao
    
    Education:              BS, PhD, Simon Fraser University
    
    Research Interests:     Data mining, databases, information retrieval
    
    Email:                  jg66@txstate.edu
    
    Webpage:                http://cs.txstate.edu/~jg66
    

