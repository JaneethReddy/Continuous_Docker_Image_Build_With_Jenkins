> Note: Though in the task I was asked to print date of successful-execution only once I actually printed twice seperately for CO2 cycle and FX Rate as the successful-execution dates are different for them(Also the FX Rate website is giving the rate till 10-March,2022 even though I worked on it on 18-Feb,2022) 

<h3>What I have done: </h3>
<p> First I have added <br>

```python
if __name__ == "__main__":
    print(getCO2("2022-02-13"))
```
to both job1, and job2 python files so that the print part won't be executed when I import and use them.
 Then I have written all the required code in my **script.py** file where I have imported the given python files, 
 used datetime module to get today's date and declared the required output as false at the begining itself. Now 
  I have used the while loop to decrease the date by 1 day as long as we didn't get the data for our output. Once 
  the required execution is successful I would simply come out of the loop and print the required output.
 </p>
 
 <h4>Final Output:</h4>
 
 >The cycle CO2 is 418.61, trend CO2 is 416.76 as on date 2022-02-15 and 
  Foreign Exchange rates for GBP to USD is 1.3616186923 as on date 2022-02-18
