# scrape-BBC-news-India  
Scrape today's headlines for India from BBC.com and store in a HTML file  

in command prompt, navigate to file location  
```
cd <full file location>
```

to install required libraries  
```
pip install -r requirements.txt
```

to run script  
```
python code.py
```


the HTML file created can be opened from command prompt.  
to run the program and open the HTML page consequently, create a batch file as per below process.  

open notepad as empty file  
write:  
```  
"<your python.exe location>" "<your code.py location>"  
start "" "file:///<HTML file location>"  
pause
```  

save the notepad file with .bat extension.  

double click on the batch file to run.
