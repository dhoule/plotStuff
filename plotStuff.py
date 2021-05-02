import numpy as np
import pandas as pd
import plotly.graph_objects as go
import glob
# import matplotlib.pyplot as plt

# Starts the arrays to be used
def fillOutArrays(dirty):
  dirty['two'] = []
  dirty['four'] = []
  dirty['eight'] = []
  dirty['dataNc10'] = []
  dirty['dataNc09'] = []
  dirty['dataNc08'] = []
  dirty['dataNc07'] = []
  dirty['dataNc06'] = []
  dirty['dataNc05'] = []
  dirty['dataNc04'] = []
  dirty['dataNc03'] = []
  dirty['dataNc02'] = []
  dirty['dataNc01'] = []

  return dirty

# Actually fills out the arrays used
def fillOutMultiArrays(dirty, func, funcVal1, funcVal2, nOp):
  # fillOutMultiArrays(versions['clusterPercent'][version], 1, shorten, fullSet[fileName][version], 0)
  if func == 1:
    if nOp == 0:
      dirty['two']     = generateDataForClustersFoundPercentage(funcVal1['two']) # node 2 - different percentage
      dirty['four']    = generateDataForClustersFoundPercentage(funcVal1['four']) # node 4 - different percentage
      dirty['eight']   = generateDataForClustersFoundPercentage(funcVal1['eight']) # node 8 - different percentage
      dirty['twoFull']     = generateDataForClustersFoundPercentage(funcVal2['two']) # node 2 - different percentage
      dirty['fourFull']    = generateDataForClustersFoundPercentage(funcVal2['four']) # node 4 - different percentage
      dirty['eightFull']   = generateDataForClustersFoundPercentage(funcVal2['eight']) # node 8 - different percentage
    else:
      dirty['dataNc10'] = generateDataForClustersFoundNodes(funcVal1['dataNc10'])
      dirty['dataNc09'] = generateDataForClustersFoundNodes(funcVal1['dataNc09'])
      dirty['dataNc08'] = generateDataForClustersFoundNodes(funcVal1['dataNc08'])
      dirty['dataNc07'] = generateDataForClustersFoundNodes(funcVal1['dataNc07'])
      dirty['dataNc06'] = generateDataForClustersFoundNodes(funcVal1['dataNc06'])
      dirty['dataNc05'] = generateDataForClustersFoundNodes(funcVal1['dataNc05'])
      dirty['dataNc04'] = generateDataForClustersFoundNodes(funcVal1['dataNc04'])
      dirty['dataNc03'] = generateDataForClustersFoundNodes(funcVal1['dataNc03'])
      dirty['dataNc02'] = generateDataForClustersFoundNodes(funcVal1['dataNc02'])
      dirty['dataNc01'] = generateDataForClustersFoundNodes(funcVal1['dataNc01'])
      dirty['dataNc10Full'] = generateDataForClustersFoundNodes(funcVal2['dataNc10'])
  elif func == 2:
    if nOp == 0:
      dirty['two']     = generateDataForTimeSpentPercentage(funcVal1['two']) # node 2 - different percentage
      dirty['four']    = generateDataForTimeSpentPercentage(funcVal1['four']) # node 4 - different percentage
      dirty['eight']   = generateDataForTimeSpentPercentage(funcVal1['eight']) # node 8 - different percentage
      dirty['twoFull']     = generateDataForTimeSpentPercentage(funcVal2['two']) # node 2 - different percentage
      dirty['fourFull']    = generateDataForTimeSpentPercentage(funcVal2['four']) # node 4 - different percentage
      dirty['eightFull']   = generateDataForTimeSpentPercentage(funcVal2['eight']) # node 8 - different percentage
    else:
      dirty['dataNc10'] = generateDataForTimeSpentNodes(funcVal1['dataNc10'])
      dirty['dataNc09'] = generateDataForTimeSpentNodes(funcVal1['dataNc09'])
      dirty['dataNc08'] = generateDataForTimeSpentNodes(funcVal1['dataNc08'])
      dirty['dataNc07'] = generateDataForTimeSpentNodes(funcVal1['dataNc07'])
      dirty['dataNc06'] = generateDataForTimeSpentNodes(funcVal1['dataNc06'])
      dirty['dataNc05'] = generateDataForTimeSpentNodes(funcVal1['dataNc05'])
      dirty['dataNc04'] = generateDataForTimeSpentNodes(funcVal1['dataNc04'])
      dirty['dataNc03'] = generateDataForTimeSpentNodes(funcVal1['dataNc03'])
      dirty['dataNc02'] = generateDataForTimeSpentNodes(funcVal1['dataNc02'])
      dirty['dataNc01'] = generateDataForTimeSpentNodes(funcVal1['dataNc01'])
      dirty['dataNc10Full'] = generateDataForTimeSpentNodes(funcVal2['dataNc10'])

  return dirty

# # of Clusters found vs % of dataset used
def generateDataForClustersFoundPercentage(dirty):
  data = []
  x = []
  y = []
  p = []
  m = []

  for d in dirty:
    x.append(d[0]) # Percent of dataset
    y.append(float(d[3])) # Mean clusters found
    p.append(format(float(d[2]) - float(d[3]), '.8g')) # Max diff of clusters found
    m.append(format(float(d[3]) - float(d[1]), '.8g')) # Min diff of clusters found
  data.append(x)
  data.append(y)
  data.append(p)
  data.append(m)
  return data

# Time vs % of dataset used
def generateDataForTimeSpentPercentage(dirty):
  data = []
  x = []
  y = []
  p = []
  m = []
  for d in dirty:
    x.append(d[0]) # Percent of dataset
    y.append(float(d[6])) # Mean time spent
    p.append(format(float(d[5]) - float(d[6]), '.8g')) # Max diff of time spent
    m.append(format(float(d[6]) - float(d[4]), '.8g')) # Min diff of time spent
  data.append(x)
  data.append(y)
  data.append(p)
  data.append(m)
  return data

# Time spent vs # # of Nodes used  
def generateDataForTimeSpentNodes(dirty):
  data = []
  x = []
  y = []
  p = []
  m = []
  for d in dirty:
    x.append(d[0]) # Nodes
    y.append(float(d[6])) # Mean time spent
    p.append(format(float(d[5]) - float(d[6]), '.8g')) # Max diff of time spent
    m.append(format(float(d[6]) - float(d[4]), '.8g')) # Min diff of time spent
  data.append(x)
  data.append(y)
  data.append(p)
  data.append(m)
  return data

# # of Clusters found vs # of Nodes used  
def generateDataForClustersFoundNodes(dirty):
  data = []
  x = []
  y = []
  p = []
  m = []

  for d in dirty:
    x.append(d[0]) # Nodes used
    y.append(float(d[3])) # Mean clusters found
    p.append(format(float(d[2]) - float(d[3]), '.8g')) # Max diff of clusters found
    m.append(format(float(d[3]) - float(d[1]), '.8g')) # Min diff of clusters found
  data.append(x)
  data.append(y)
  data.append(p)
  data.append(m)
  return data

# Adds elements to the figure
def addFigureTrace(fig, data, name):
  fig.add_trace(go.Scatter(
      x=data[0],
      y=data[1],
      mode='lines',
      name=name,
      error_y=dict(
        type='data',
        symmetric=False,
        array=data[2],
        arrayminus=data[3]
      )
    ))

# Updates the meta data of the figure
def updateFigureLayout(fig, title, version, postTitle, legend, xaxis_title, yaxis_title):
  fig.update_layout(
    title=title + ': ' + version + ' - ' + postTitle,
    xaxis_title=xaxis_title,
    yaxis_title=yaxis_title,
    legend_title_text=legend
  )

# of Clusters found vs % of dataset used
def doubleAddTrace(fig, name, x, y):
  fig.add_trace(go.Bar(
    name=name,
    x=x,
    y=y
    ))

# Updates the meta data of a different figure 
def doubleUpdateLayout(fig, barmode, title, xaxis_title, yaxis_title, legend):
  fig.update_layout(
    barmode=barmode,
    title=title,
    xaxis_title=xaxis_title,
    yaxis_title=yaxis_title,
    legend_title_text=legend
  )

# Determines the post names for items in the figures
def determinPrenames(version, name):
    
  if version == 'ORG':
    pts = ''
    if name == 'clus50k':
      pts = '50000 - '
    elif name == 'part64':
      pts = '61440 - '
    elif name == 't4.8k' or name == 't5.8k' or name == 't8.8k':
      pts = '8000 - '
    elif name == 't7.10k':
      pts = '10000 - '

    preName1 = pts
    preName2 = pts
    preName3 = pts
    preName4 = pts
    preName5 = pts
    preName6 = pts
    preName7 = pts
    preName8 = pts
    preName9 = pts
    preName10 = pts
  else:
    preName1 = '1000 - '
    preName2 = '900 - '
    preName3 = '800 - '
    preName4 = '700 - '
    preName5 = '600 - '
    preName6 = '500 - '
    preName7 = '400 - '
    preName8 = '300 - '
    preName9 = '200 - '
    preName10 = '100 - '

  return preName1, preName2, preName3, preName4, preName5, preName6, preName7, preName8, preName9, preName10

startPath = '' # Absolute path of the folder the files are in
# Do 1 data set at a time to help yourself not confuse them, and not bog down your system.
# The code is recursive, as the baseline (ORG) is always looked at. 

server = 1 # Just leave this at 1, or remove all of the code that uses it. It was used to determine the difference between loosely coupled and tightly coupled code. It's not needed.
wanted = 'clus50k' # This is the data set you want. You want to limit it to a single set, so not to be over limited
ignore = 'ignore' # This is the meta file you can keep. It's full file name is " ignore_.bin.txt" as of the current coding. This is for data about the results.

datasets = {} # first set of graphs; individual
datasets2 = {} # 2nd set of graphs; combination
fullSet = {} # 3rd set of graphs; combination using all points

for absPath in glob.glob(startPath + '**/*.txt', recursive=True):
  fileName = None
  codeVersion = None
  with open(absPath, mode='rb') as txtFile:
    # Get the code version
    codeVersion = absPath.split('/')[-2]
    # Get the dataset name
    fileName = absPath.split('/')[-1].split('_')[0].split('.bin')[0]

    if fileName == ignore:
      continue

    # Determine the folder name for the version of the code
    if codeVersion not in datasets:
      datasets[codeVersion] = {}
    # Determine the file name for what dataset is used
    if fileName not in datasets[codeVersion]:
      datasets[codeVersion][fileName] = {}

    if fileName not in datasets2:
      datasets2[fileName] = {}
      fullSet[fileName] = {}

    if codeVersion not in datasets2[fileName]:
      datasets2[fileName][codeVersion] = {}
      fullSet[fileName][codeVersion] = {}

    # Setup the individual datasets for graphing
    shortd1 = fillOutArrays(datasets[codeVersion][fileName])
    shortd2 = fillOutArrays(datasets2[fileName][codeVersion])
    shortfs = fillOutArrays(fullSet[fileName][codeVersion])

    # Read all of the lines from the file in question
    fl = txtFile.readlines()
    skip = True
    one = 0
    two = 0
    thr = 0
    fou = 0
    prc = 0
    prc1 = 0
    prc2 = 0
    prc3 = 0
    prc4 = 0
    for l in fl:
      if skip:
        skip = False
        continue
      l = l.strip().decode()
      if l == "":
        continue

      values = l.split(',')
      node = values[0].strip()
      percent = values[1].strip()
      minclus = values[11].strip()
      maxclus = values[12].strip()
      meaclus = values[13].strip()
      mintime = values[15].strip()
      maxtime = values[16].strip()
      meatime = values[17].strip()
      minptInClts = values[5].strip()
      maxptInClts = values[6].strip()
      meaptInClts = values[7].strip()

      percentArray = [percent, minclus, maxclus, meaclus, mintime, maxtime, meatime, minptInClts, maxptInClts, meaptInClts]
      nodeArray = [node, minclus, maxclus, meaclus, mintime, maxtime, meatime, minptInClts, maxptInClts, meaptInClts]

      if node == "2":
        if one < 10:
          one = one + 1
          shortd1['two'].append(percentArray)
          shortd2['two'].append(percentArray)
        else:
          shortfs['two'].append(percentArray)
      elif node == "4":
        if two < 10:
          two = two + 1
          shortd1['four'].append(percentArray)
          shortd2['four'].append(percentArray)
        else:
          shortfs['four'].append(percentArray)
      elif node == "8":
        if thr < 10:
          thr = thr + 1
          shortd1['eight'].append(percentArray)
          shortd2['eight'].append(percentArray)
        else:
          shortfs['eight'].append(percentArray)

      if server == 0:
        if percent == "1.0":
          shortd1['dataNc10'].append(nodeArray)
          shortd2['dataNc10'].append(nodeArray)
        elif percent == "0.9":
          shortd1['dataNc09'].append(nodeArray)
          shortd2['dataNc09'].append(nodeArray)
        elif percent == "0.8":
          shortd1['dataNc08'].append(nodeArray)
          shortd2['dataNc08'].append(nodeArray)
        elif percent == "0.7":
          shortd1['dataNc07'].append(nodeArray)
          shortd2['dataNc07'].append(nodeArray)
        elif percent == "0.6":
          shortd1['dataNc06'].append(nodeArray)
          shortd2['dataNc06'].append(nodeArray)
        elif percent == "0.5":
          shortd1['dataNc05'].append(nodeArray)
          shortd2['dataNc05'].append(nodeArray)
        elif percent == "0.4":
          shortd1['dataNc04'].append(nodeArray)
          shortd2['dataNc04'].append(nodeArray)
        elif percent == "0.3":
          shortd1['dataNc03'].append(nodeArray)
          shortd2['dataNc03'].append(nodeArray)
        elif percent == "0.2":
          shortd1['dataNc02'].append(nodeArray)
          shortd2['dataNc02'].append(nodeArray)
        elif percent == "0.1":
          shortd1['dataNc01'].append(nodeArray)
          shortd2['dataNc01'].append(nodeArray)
      else:
        if percent == "1000":
          shortd1['dataNc10'].append(nodeArray)
          shortd2['dataNc10'].append(nodeArray)
        elif percent == "900":
          shortd1['dataNc09'].append(nodeArray)
          shortd2['dataNc09'].append(nodeArray)
        elif percent == "800":
          shortd1['dataNc08'].append(nodeArray)
          shortd2['dataNc08'].append(nodeArray)
        elif percent == "700":
          shortd1['dataNc07'].append(nodeArray)
          shortd2['dataNc07'].append(nodeArray)
        elif percent == "600":
          shortd1['dataNc06'].append(nodeArray)
          shortd2['dataNc06'].append(nodeArray)
        elif percent == "500":
          shortd1['dataNc05'].append(nodeArray)
          shortd2['dataNc05'].append(nodeArray)
        elif percent == "400":
          shortd1['dataNc04'].append(nodeArray)
          shortd2['dataNc04'].append(nodeArray)
        elif percent == "300":
          shortd1['dataNc03'].append(nodeArray)
          shortd2['dataNc03'].append(nodeArray)
        elif percent == "200":
          shortd1['dataNc02'].append(nodeArray)
          shortd2['dataNc02'].append(nodeArray)
        elif percent == "100":
          shortd1['dataNc01'].append(nodeArray)
          shortd2['dataNc01'].append(nodeArray)
        else:
          if fileName == 'ORG':
            if len(shortd1['dataNc10']) < 4:
              shortd1['dataNc10'].append(nodeArray)
              shortd2['dataNc10'].append(nodeArray)
            else:
              shortfs['dataNc10'].append(nodeArray)
            if len(shortd1['dataNc09']) < 4:
              shortd1['dataNc09'].append(nodeArray)
              shortd2['dataNc09'].append(nodeArray)
            else:
              shortfs['dataNc09'].append(nodeArray)
            if len(shortd1['dataNc08']) < 4:
              shortd1['dataNc08'].append(nodeArray)
              shortd2['dataNc08'].append(nodeArray)
            else:
              shortfs['dataNc08'].append(nodeArray)
            if len(shortd1['dataNc07']) < 4:
              shortd1['dataNc07'].append(nodeArray)
              shortd2['dataNc07'].append(nodeArray)
            else:
              shortfs['dataNc07'].append(nodeArray)
            if len(shortd1['dataNc06']) < 4:
              shortd1['dataNc06'].append(nodeArray)
              shortd2['dataNc06'].append(nodeArray)
            else:
              shortfs['dataNc06'].append(nodeArray)
            if len(shortd1['dataNc05']) < 4:
              shortd1['dataNc05'].append(nodeArray)
              shortd2['dataNc05'].append(nodeArray)
            else:
              shortfs['dataNc05'].append(nodeArray)
            if len(shortd1['dataNc04']) < 4:
              shortd1['dataNc04'].append(nodeArray)
              shortd2['dataNc04'].append(nodeArray)
            else:
              shortfs['dataNc04'].append(nodeArray)
            if len(shortd1['dataNc03']) < 4:
              shortd1['dataNc03'].append(nodeArray)
              shortd2['dataNc03'].append(nodeArray)
            else:
              shortfs['dataNc03'].append(nodeArray)
            if len(shortd1['dataNc02']) < 4:
              shortd1['dataNc02'].append(nodeArray)
              shortd2['dataNc02'].append(nodeArray)
            else:
              shortfs['dataNc02'].append(nodeArray)
            if len(shortd1['dataNc01']) < 4:
              shortd1['dataNc01'].append(nodeArray)
              shortd2['dataNc01'].append(nodeArray)
            else:
              shortfs['dataNc01'].append(nodeArray)
          else:
            if len(shortfs['dataNc10']) < 4:
              shortfs['dataNc10'].append(nodeArray)
            if len(shortfs['dataNc09']) < 4:
              shortfs['dataNc09'].append(nodeArray)
            if len(shortfs['dataNc08']) < 4:
              shortfs['dataNc08'].append(nodeArray)
            if len(shortfs['dataNc07']) < 4:
              shortfs['dataNc07'].append(nodeArray)
            if len(shortfs['dataNc06']) < 4:
              shortfs['dataNc06'].append(nodeArray)
            if len(shortfs['dataNc05']) < 4:
              shortfs['dataNc05'].append(nodeArray)
            if len(shortfs['dataNc04']) < 4:
              shortfs['dataNc04'].append(nodeArray)
            if len(shortfs['dataNc03']) < 4:
              shortfs['dataNc03'].append(nodeArray)
            if len(shortfs['dataNc02']) < 4:
              shortfs['dataNc02'].append(nodeArray)
            if len(shortfs['dataNc01']) < 4:
              shortfs['dataNc01'].append(nodeArray)


for version in datasets:
  # if version != 'SNGS1' or version != 'ORG':
  #   continue

  for name in datasets[version]:

    if name != wanted:
      continue

    shortten = datasets[version][name]

    preName1, preName2, preName3, preName4, preName5, preName6, preName7, preName8, preName9, preName10 = determinPrenames(version, name)

    postPTitle = '% of dataset used' if server == 0 else 'Seeds used'
    axisPTitle = 'Percent of Dataset Used' if server == 0 else 'Seeds Used'
    postNTitle = '# of Nodes used' if server == 0 else '# of Threads used'
    axisNtitle = 'Nodes Used' if server == 0 else 'Threads Used'
    nLegend = 'Nodes' if server == 0 else 'Threads'
    pLegend = '%' if server == 0 else 'Seeds'
      
    # # of Clusters found vs % of dataset used
    data1 = generateDataForClustersFoundPercentage(shortten['two']) # node 2 - different percentage
    data2 = generateDataForClustersFoundPercentage(shortten['four']) # node 4 - different percentage
    data3 = generateDataForClustersFoundPercentage(shortten['eight']) # node 8 - different percentage

    figMulti1 = go.Figure()
    addFigureTrace(figMulti1, data1, '2 ' + nLegend)
    addFigureTrace(figMulti1, data2, '4 ' + nLegend)
    addFigureTrace(figMulti1, data3, '8 ' + nLegend)
    updateFigureLayout(figMulti1, name, version, '# of Clusters found vs ' + postPTitle, nLegend, axisPTitle, 'Clusters Found')
    figMulti1.show()

    # Time vs % of dataset used
    data1 = generateDataForTimeSpentPercentage(shortten['two']) # node 2 - different percentage
    data2 = generateDataForTimeSpentPercentage(shortten['four']) # node 4 - different percentage
    data3 = generateDataForTimeSpentPercentage(shortten['eight']) # node 8 - different percentage

    figMulti2 = go.Figure()
    addFigureTrace(figMulti2, data1, '2 ' + nLegend)
    addFigureTrace(figMulti2, data2, '4 ' + nLegend)
    addFigureTrace(figMulti2, data3, '8 ' + nLegend)
    updateFigureLayout(figMulti2, name, version, 'Time vs ' + postPTitle, nLegend, axisPTitle, 'Time (Sec)')
    figMulti2.show()

    ### Need to do the different Nodes, but same percentage...

    # Time spent vs # # of Nodes used  
    data1 = generateDataForTimeSpentNodes(shortten['dataNc10'])
    data2 = generateDataForTimeSpentNodes(shortten['dataNc09'])
    data3 = generateDataForTimeSpentNodes(shortten['dataNc08'])
    data4 = generateDataForTimeSpentNodes(shortten['dataNc07'])
    data5 = generateDataForTimeSpentNodes(shortten['dataNc06'])
    data6 = generateDataForTimeSpentNodes(shortten['dataNc05'])
    data7 = generateDataForTimeSpentNodes(shortten['dataNc04'])
    data8 = generateDataForTimeSpentNodes(shortten['dataNc03'])
    data9 = generateDataForTimeSpentNodes(shortten['dataNc02'])
    data10 = generateDataForTimeSpentNodes(shortten['dataNc01'])

    figMulti4 = go.Figure()
    addFigureTrace(figMulti4, data1, preName1)
    addFigureTrace(figMulti4, data2, preName2)
    addFigureTrace(figMulti4, data3, preName3)
    addFigureTrace(figMulti4, data4, preName4)
    addFigureTrace(figMulti4, data5, preName5)
    addFigureTrace(figMulti4, data6, preName6)
    addFigureTrace(figMulti4, data7, preName7)
    addFigureTrace(figMulti4, data8, preName8)
    addFigureTrace(figMulti4, data9, preName9)
    addFigureTrace(figMulti4, data10, preName10)
    updateFigureLayout(figMulti4, name, version, 'Time spent vs ' + postNTitle, pLegend, axisNtitle, 'Time (Sec)')
    figMulti4.show()

    # # of Clusters found vs # of Nodes used  
    data1 = generateDataForClustersFoundNodes(shortten['dataNc10'])
    data2 = generateDataForClustersFoundNodes(shortten['dataNc09'])
    data3 = generateDataForClustersFoundNodes(shortten['dataNc08'])
    data4 = generateDataForClustersFoundNodes(shortten['dataNc07'])
    data5 = generateDataForClustersFoundNodes(shortten['dataNc06'])
    data6 = generateDataForClustersFoundNodes(shortten['dataNc05'])
    data7 = generateDataForClustersFoundNodes(shortten['dataNc04'])
    data8 = generateDataForClustersFoundNodes(shortten['dataNc03'])
    data9 = generateDataForClustersFoundNodes(shortten['dataNc02'])
    data10 = generateDataForClustersFoundNodes(shortten['dataNc01'])

    figMulti5 = go.Figure()
    addFigureTrace(figMulti5, data1, preName1)
    addFigureTrace(figMulti5, data2, preName2)
    addFigureTrace(figMulti5, data3, preName3)
    addFigureTrace(figMulti5, data4, preName4)
    addFigureTrace(figMulti5, data5, preName5)
    addFigureTrace(figMulti5, data6, preName6)
    addFigureTrace(figMulti5, data7, preName7)
    addFigureTrace(figMulti5, data8, preName8)
    addFigureTrace(figMulti5, data9, preName9)
    addFigureTrace(figMulti5, data10, preName10)
    updateFigureLayout(figMulti5, name, version, '# of Clusters found vs ' + postNTitle, pLegend, axisNtitle, 'Clusters Found')
    figMulti5.show()




for fileName in datasets2:

  if fileName != wanted:
    continue

  versions = {}
  versions['clusterPercent'] = {}
  versions['timePercent'] = {}
  versions['ptsInClustersPercent'] = {}
  versions['timeNode'] = {}
  versions['clusterNode'] = {}
  versions['ptsInClustersNode'] = {} 

  figa = go.Figure()
  figb = go.Figure()
  figd = go.Figure()
  fige = go.Figure()

  figg = go.Figure()
  figh = go.Figure()
  figi = go.Figure()

  figj = go.Figure()
  figk = go.Figure()
  figl = go.Figure()

  fign = go.Figure()
  figo = go.Figure()
  figp = go.Figure()


  for version in datasets2[fileName]:
    # if version != 'SNGS1':
    #   continue

    shorten = datasets2[fileName][version]

    versions['clusterPercent'][version] = {}
    versions['timePercent'][version] = {}
    versions['ptsInClustersPercent'][version] = {}
    versions['timeNode'][version] = {}
    versions['clusterNode'][version] = {}
    versions['ptsInClustersNode'][version] = {} 

    # # of Clusters found vs % of dataset used
    versions['clusterPercent'][version] = fillOutMultiArrays(versions['clusterPercent'][version], 1, shorten, fullSet[fileName][version], 0)

    # # Time vs % of dataset used
    versions['timePercent'][version] = fillOutMultiArrays(versions['timePercent'][version], 2, shorten, fullSet[fileName][version], 0)

    ### Need to do the different Nodes, but same percentage...

    preName1, preName2, preName3, preName4, preName5, preName6, preName7, preName8, preName9, preName10 = determinPrenames(version, fileName)

    # # of Clusters found vs # of Nodes used 
    versions['clusterNode'][version] = fillOutMultiArrays(versions['clusterNode'][version], 1, shorten, fullSet[fileName][version], 1)

    # Time spent vs # # of Nodes used
    versions['timeNode'][version] = fillOutMultiArrays(versions['timeNode'][version], 2, shorten, fullSet[fileName][version], 1)

    # of Clusters found vs % of dataset used
    doubleAddTrace(figa, 'Two - ' + version, versions['clusterPercent'][version]['two'][0], versions['clusterPercent'][version]['two'][1])
    doubleAddTrace(figa, 'Four - ' + version, versions['clusterPercent'][version]['four'][0], versions['clusterPercent'][version]['four'][1])
    doubleAddTrace(figa, 'Eight - ' + version, versions['clusterPercent'][version]['eight'][0], versions['clusterPercent'][version]['eight'][1])

    # # Time vs % of dataset used
    doubleAddTrace(figb, 'Two - ' + version, versions['timePercent'][version]['two'][0], versions['timePercent'][version]['two'][1])
    doubleAddTrace(figb, 'Four - ' + version, versions['timePercent'][version]['four'][0], versions['timePercent'][version]['four'][1])
    doubleAddTrace(figb, 'Eight - ' + version, versions['timePercent'][version]['eight'][0], versions['timePercent'][version]['eight'][1])

    ### Need to do the different Nodes, but same percentage...

    # Time spent vs # # of Nodes used 
    doubleAddTrace(figd, preName1 + version, versions['timeNode'][version]['dataNc10'][0], versions['timeNode'][version]['dataNc10'][1])
    doubleAddTrace(figd, preName2 + version, versions['timeNode'][version]['dataNc09'][0], versions['timeNode'][version]['dataNc09'][1])
    doubleAddTrace(figd, preName3 + version, versions['timeNode'][version]['dataNc08'][0], versions['timeNode'][version]['dataNc08'][1])
    doubleAddTrace(figd, preName4 + version, versions['timeNode'][version]['dataNc07'][0], versions['timeNode'][version]['dataNc07'][1])
    doubleAddTrace(figd, preName5 + version, versions['timeNode'][version]['dataNc06'][0], versions['timeNode'][version]['dataNc06'][1])
    doubleAddTrace(figd, preName6 + version, versions['timeNode'][version]['dataNc05'][0], versions['timeNode'][version]['dataNc05'][1])
    doubleAddTrace(figd, preName7 + version, versions['timeNode'][version]['dataNc04'][0], versions['timeNode'][version]['dataNc04'][1])
    doubleAddTrace(figd, preName8 + version, versions['timeNode'][version]['dataNc03'][0], versions['timeNode'][version]['dataNc03'][1])
    doubleAddTrace(figd, preName9 + version, versions['timeNode'][version]['dataNc02'][0], versions['timeNode'][version]['dataNc02'][1])
    doubleAddTrace(figd, preName10 + version, versions['timeNode'][version]['dataNc01'][0], versions['timeNode'][version]['dataNc01'][1])
    
    # # of Clusters found vs # of Nodes used 
    doubleAddTrace(fige, preName1 + version, versions['clusterNode'][version]['dataNc10'][0], versions['clusterNode'][version]['dataNc10'][1])
    doubleAddTrace(fige, preName2 + version, versions['clusterNode'][version]['dataNc09'][0], versions['clusterNode'][version]['dataNc09'][1])
    doubleAddTrace(fige, preName3 + version, versions['clusterNode'][version]['dataNc08'][0], versions['clusterNode'][version]['dataNc08'][1])
    doubleAddTrace(fige, preName4 + version, versions['clusterNode'][version]['dataNc07'][0], versions['clusterNode'][version]['dataNc07'][1])
    doubleAddTrace(fige, preName5 + version, versions['clusterNode'][version]['dataNc06'][0], versions['clusterNode'][version]['dataNc06'][1])
    doubleAddTrace(fige, preName6 + version, versions['clusterNode'][version]['dataNc05'][0], versions['clusterNode'][version]['dataNc05'][1])
    doubleAddTrace(fige, preName7 + version, versions['clusterNode'][version]['dataNc04'][0], versions['clusterNode'][version]['dataNc04'][1])
    doubleAddTrace(fige, preName8 + version, versions['clusterNode'][version]['dataNc03'][0], versions['clusterNode'][version]['dataNc03'][1])
    doubleAddTrace(fige, preName9 + version, versions['clusterNode'][version]['dataNc02'][0], versions['clusterNode'][version]['dataNc02'][1])
    doubleAddTrace(fige, preName10 + version, versions['clusterNode'][version]['dataNc01'][0], versions['clusterNode'][version]['dataNc01'][1])

    # Single attribute values spread across multiple datasets

    # Time spent vs # # of Nodes used 
    doubleAddTrace(figg, version, versions['timeNode'][version]['dataNc10Full'][0], versions['timeNode'][version]['dataNc10Full'][1])
    # # of Clusters found vs # of Nodes used 
    doubleAddTrace(figh, version, versions['clusterNode'][version]['dataNc10Full'][0], versions['clusterNode'][version]['dataNc10Full'][1])
    # # of Clusters found vs % of dataset used
    doubleAddTrace(figj, version, versions['clusterPercent'][version]['twoFull'][0], versions['clusterPercent'][version]['twoFull'][1])
    doubleAddTrace(figk, version, versions['clusterPercent'][version]['fourFull'][0], versions['clusterPercent'][version]['fourFull'][1])
    doubleAddTrace(figl, version, versions['clusterPercent'][version]['eightFull'][0], versions['clusterPercent'][version]['eightFull'][1])
    # Time vs % of dataset used
    doubleAddTrace(fign, version, versions['timePercent'][version]['twoFull'][0], versions['timePercent'][version]['twoFull'][1])
    doubleAddTrace(figo, version, versions['timePercent'][version]['fourFull'][0], versions['timePercent'][version]['fourFull'][1])
    doubleAddTrace(figp, version, versions['timePercent'][version]['eightFull'][0], versions['timePercent'][version]['eightFull'][1])


  pts = ''
  if fileName == 'clus50k':
    pts = '50000'
  elif fileName == 'part64':
    pts = '61440'
  elif fileName == 't4.8k':
    pts = '8000'
  elif fileName == 't5.8k':
    pts = '8000'
  elif fileName == 't7.10k':
    pts = '10000'
  elif fileName == 't8.8k':
    pts = '8000'

  postPTitle = '% of dataset used' if server == 0 else 'Seeds used'
  axisPTitle = 'Percent of Dataset Used' if server == 0 else 'Seeds Used'
  postNTitle = '# of Nodes used' if server == 0 else '# of Threads used'
  axisNtitle = 'Nodes Used' if server == 0 else 'Threads Used'
  nLegend = 'Nodes' if server == 0 else 'Threads'
  pLegend = '%' if server == 0 else 'Seeds'

  doubleUpdateLayout(figa, 'group', fileName + ': # of Clusters found vs ' + postPTitle, axisPTitle, 'Clusters Found', nLegend + ' - Dataset')
  figa.show()

  doubleUpdateLayout(figb, 'group', fileName + ': Time spent vs ' + postPTitle, axisPTitle, 'Time (Sec)', nLegend + ' - Dataset')
  figb.show()

  doubleUpdateLayout(figd, 'group', fileName + ': Time spent vs ' + postNTitle, axisNtitle, 'Time spent (Sec)', pLegend + ' - Dataset')
  figd.show()

  doubleUpdateLayout(fige, 'group', fileName + ': # of Clusters found vs ' + postNTitle, axisNtitle, '# of Clusters found', pLegend + ' - Dataset')
  fige.show()

  doubleUpdateLayout(figg, 'group', fileName + ': Time spent vs ' + postNTitle + ' - All points are used (' + pts + ')', axisNtitle, 'Time spent (Sec)', pLegend + ' - Dataset')
  figg.show()

  doubleUpdateLayout(figh, 'group', fileName + ': # of Clusters found vs ' + postNTitle + ' - All points are used (' + pts + ')', axisNtitle, '# of Clusters found', pLegend + ' - Dataset')
  figh.show()

  # # of Clusters found vs % of dataset used
  doubleUpdateLayout(figj, 'group', fileName + ': # of Clusters found vs 2 ' + nLegend + ' used - All points are used (' + pts + ')', 'Total Points of Dataset', '# of Clusters found', 'Dataset')
  figj.show()
  doubleUpdateLayout(figk, 'group', fileName + ': # of Clusters found vs 4 ' + nLegend + ' used - All points are used (' + pts + ')', 'Total Points of Dataset', '# of Clusters found', 'Dataset')
  figk.show()
  doubleUpdateLayout(figl, 'group', fileName + ': # of Clusters found vs 8 ' + nLegend + ' used - All points are used (' + pts + ')', 'Total Points of Dataset', '# of Clusters found', 'Dataset')
  figl.show()


  # Time vs % of dataset used
  doubleUpdateLayout(fign, 'group', fileName + ': Time spent vs 2 ' + nLegend + ' used - All points are used (' + pts + ')', 'Total Points of Dataset', 'Time spent (Sec)', 'Dataset')
  fign.show()
  doubleUpdateLayout(figo, 'group', fileName + ': Time spent vs 4 ' + nLegend + ' used - All points are used (' + pts + ')', 'Total Points of Dataset', 'Time spent (Sec)', 'Dataset')
  figo.show()
  doubleUpdateLayout(figp, 'group', fileName + ': Time spent vs 8 ' + nLegend + ' used - All points are used (' + pts + ')', 'Total Points of Dataset', 'Time spent (Sec)', 'Dataset')
  figp.show()




exit()