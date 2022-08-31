## Audi Dealer Model Search
Quick and dirty python tool to bulk search Audi dealers **new inventory** for a model.  
Outputs vehicle data and URL to dealers with available models.

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

## Arguments
`--model '<model name>'`  
Model name of vehicle  

`--diff`  
Indicates if output should only show new vehicles since last search

## Examples
**Input**  
```
python audi_model_search.py --model 'RS 3'
```
**Output**  
```
Beginning Search
----------------------------------
Audi Albany
2022 - RS 3 - Turbo Blue
Options:
['PSS', 'C02', '79H', 'RMR', 'S0D', '9RT']
https://www.audialbany.com/new/Audi/2022-Audi-RS+3-2e9319100a0e0a926948a22d12a279f9.htm
----------------------------------
Audi Cicero
2022 - RS 3 - Mythos Black
Options:
['6FA', 'C02', 'RMR', 'S0D']
https://www.audicicero.com/new/Audi/2022-Audi-RS+3-52a1dc1f0a0e0a936e131237552208a9.htm
----------------------------------
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
----------------------------------
Audi Albany
2022 - Q8 - Carrara White
Options:
['PHX', 'PQD', 'C02', 'AFK', 'QWL', 'RBF', 'U03', 'CRJ', 'WPS', 'QEP']
https://www.audialbany.com/new/Audi/2022-Audi-Q8-8fcfd44c0a0e0a993cac6f92ea8b5417.htm
----------------------------------
Audi Albuquerque
2022 - Q8 - Glacier White Metallic
Options:
['PHX', 'CRA', 'C02', 'RBF', 'CRJ', 'WPD', 'QEP', 'PAO']
https://www.audiabq.com/new/Audi/2022-Audi-Q8-albuquerque-d89079b40a0e0a9074095e371ec5b367.htm
----------------------------------
Audi Allentown
2022 - Q8 - Glacier White
Options:
['PC4', 'PHX', 'PQD', 'C02', '98P', 'PPS', '6NQ', 'CRJ', 'WPS', 'CX2']
https://www.audiallentown.com/new/Audi/2022-Audi-Q8-Allentown-PA-da1a732b0a0e0a9352ec73f33770c2b7.htm
----------------------------------
Audi Flemington
2022 - Q8 - Mythos Black Metallic
Options:
['CRA', 'QWL', 'RBF', 'CRJ', 'WPD', '0E0E', 'QEP']
https://www.audiallentown.com/new/Audi/2022-Audi-Q8-Allentown-PA-884b5b080a0e0a915fd7cc29023c70cb.htm
----------------------------------
...
Search Complete
```