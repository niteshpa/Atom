**What is RegEx ?**  
It means Regular Expression. They are set of characters, we use them to match a particular pattern from a string.  
Example :  Regular expression for an email address (Copied from geeksforgeeks)
**_^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$  _**

  
  We can use regex with command line tools like _grep_, which will print the line matching the pattern.  
  e.g. >>> grep ^p.ng /home/user/file.txt 
  
  ### Using RegEx in Python  
  
  We can use RegEx to match patterns in string in Python after Importing the  re Module  
    
 _Syntax_   
 ![image](https://user-images.githubusercontent.com/43354988/135725494-d97f48ca-4abc-4891-a11b-1d011d3259c0.png) 
 
 ![image](https://user-images.githubusercontent.com/43354988/135725503-567eb934-0c3b-49ce-9ac9-6c410ed764a9.png)   
 
 Search function only matches with the first pattern. What if we want to match all the options? Then, re module provides us another function which is findall.    
 
 ![image](https://user-images.githubusercontent.com/43354988/135725921-82679fbb-a8b8-4155-a7fc-40a6959d3226.png)    
 
 ![image](https://user-images.githubusercontent.com/43354988/135726058-b63b939d-5675-4803-b4bb-71012e368145.png)


![image](https://user-images.githubusercontent.com/43354988/135726156-be19ab77-eb8e-4acc-86d2-39ae02d3903f.png)


 
 

 
 
  
  
  
  
  

