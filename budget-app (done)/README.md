# Budget App

built at freeCodeCamp

One Category class which tracks a category of spending mainly with 'deposit' 'withdraw' and 'transfer' functions.
And a function 'create_spend_chart' which takes a 'list[Categories]' object and returns the percentage 
spending per category as a bar chart

## Sample output

*************Food*************
initial deposit        1000.00
groceries               -10.15
Transfer to Clothing    -50.00
restaurant and more foo -15.89
Total: 923.96

***********Clothing***********
Transfer from Food       50.00
shirt                   -13.00
Total: 37.00

Percentage spent by category
100|          
 90|          
 80|          
 70|          
 60| o        
 50| o        
 40| o        
 30| o        
 20| o     o  
 10| o  o  o  
  0| o  o  o  
    ----------
     F  C  E  
     o  l  n  
     o  o  t  
     d  t  e  
        h  r  
        i  t  
        n  a  
        g  i  
           n  
           m  
           e  
           n  
           t  


## Run it

```bash
python budget.py
```

## Tests

```bash
pytest test_budget.py
```
