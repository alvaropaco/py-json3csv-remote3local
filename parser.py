import csv
import json
import re
import requests

from sys import argv
from pprint import pprint
from collections import OrderedDict

def readCSVfromLocal(file): 
  with open(file) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
      if line_count == 0:
        res = []
        line_count += 1
      else:
        res.append({ 'estado': row[2] })
        line_count += 1
    
  return res

def readCSVfromRemote(url): 
  
  path = '/tmp/temp_csv.txt' 
  temp = open(path, 'w')
  
  request = requests.get(url)
  
  temp.write(request.text)

  temp.close()

  with open(path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
      if line_count == 0:
        res = []
        line_count += 1
      else:
        res.append({ 'estado': row[2] })
        line_count += 1
      
  return res
    

def readJSONfromLocal(file):
  with open(file) as f:
    data = json.load(f)
  return data

def readJSONfromRemote(url): 
  request = requests.get(url)

  return request.json()

def checkContentTypeFromLocal(file):
  try:
    with open(file) as f:
      json_object = json.load(f)
  except ValueError:
    return 'CSV'
  return 'JSON'

def checkContentTypeFromRemote(url):
  try:
    request = requests.get(url)

    content = request.text

    json_object = json.loads(content)

    return 'JSON'
  except ValueError:
    return 'CSV'

def main():
  script, filePath = argv
  
  match = re.match(r'(https|http)\W', filePath)

  if match is None:
    dataType = checkContentTypeFromLocal(filePath)
    if dataType is 'JSON':
      data = readJSONfromLocal(filePath)
    else: 
      data = readCSVfromLocal(filePath)
  else:
    dataType = checkContentTypeFromRemote(filePath)
    if dataType is 'JSON':
      data = readJSONfromRemote(filePath)
    else: 
      data = readCSVfromRemote(filePath)

  res = OrderedDict()
  
  for record in data:
    if record['estado'] in res: 
      count = res[record['estado']] + 1
      res[record['estado']] = count
    else: 
      res[record['estado']] = 1
  
  ordered = OrderedDict(sorted(res.items(), key=lambda t: t[0]))
  
  for key in sorted(ordered.keys()):
    print("%s: %s" % (key, ordered[key]))

if __name__== "__main__":
  main()