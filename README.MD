## Audi Dealer Model Search
Python tool to bulk search Audi dealers for specific model.  
Outputs URL to dealers with available models.

## Requirements
```
beautifulsoup4==4.9.3
certifi==2022.5.18.1
chardet==4.0.0
charset-normalizer==2.0.12
googlesearch-python==1.1.0
idna==2.10
numpy==1.22.3
requests==2.25.1
soupsieve==2.3.2.post1
urllib3==1.26.9
```

## Developed For
`Python 3.10.4`

## Usage
`python audi_model_search.py --model '<model name>'`

## Examples
**Input**  
```
python audi_model_search.py --model 'RS 3'
```
**Output**  
```
Beginning Search
https://www.audialbany.com/new-inventory/index.htm?model=RS%203
...
Search Complete
```
---
**Input**  
```
python audi_model_search.py --model 'Q8'
```
**Output**  
```
Beginning Search
https://www.audialbany.com/new-inventory/index.htm?model=Q8
https://www.audiabq.com/new-inventory/index.htm?model=Q8
https://www.audiallentown.com/new-inventory/index.htm?model=Q8
https://www.audiofanchorage.com/new-inventory/index.htm?model=Q8
https://www.audiannarbor.com/new-inventory/index.htm?model=Q8
https://www.audiannapolis.com/new-inventory/index.htm?model=Q8
https://www.appletonaudi.com/new-inventory/index.htm?model=Q8
https://www.audiarlington.com/new-inventory/index.htm?model=Q8
https://www.audiasheville.com/new-inventory/index.htm?model=Q8
...
Search Complete
```