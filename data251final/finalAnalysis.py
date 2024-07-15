#final project analysis
from os import lstat
from data251final.libTable import LibTable
from time import perf_counter
import pandas
import seaborn as sns
import matplotlib.pyplot as plt
from bst import BST


           

def insert(data, tree, func):
    key = func(data)
    if not key:
        return
    while tree:
        tree = tree[2][key > tree[0]]
    tree.extend([key, data, [[], []]])
    
def contains(key, tree):
    if not key:
        return
    while tree:
        if key == tree[0]:
            return tree[0:2]
        tree = tree[2][key > tree[0]]

# csv to Python, using bst by default
# line to key
def get_key(l):
    # we need the 13th column but quotes mix it up
    views = ""
    title = ""
    duration = ""
    commas = 0
    quotes = False
    for c in l:
        if c == '\"':
            quotes = not quotes
        if commas == 0:
            duration += c
        if commas == 1:
            title += c
        if commas == 2:
            views += c
        if c == ',' and not quotes:
            commas += 1    
    return [title[:-1], views[:-1], duration[:-1]]

def csv_to_p_bst(b):
    tree = BST()
    for line in b:
        tree.insert(line)
    return tree

def csv_to_p_dict(file):
    dic = {}
    for line in range(len(file)):
        if line == len(file) and file[line][0] == file[line+1][0]:
            file[line+1][0] += "_"
        if file[line][0] == "Live Mock DSA" or "Elite Coding Battleground + MENTI war":
            file[line][0] += str(line)
        dic[file[line][0]] = file[line].copy()
    return dic
    

def csv_to_p_hash(file):
    hah = LibTable()
    for line in file:
        hah.insert(line[0], line.copy())
        #print(hah.get(line[0]))
    return hah
# file handling
def main(b):
    # compare two cycles
    test = [csv_to_p_bst,csv_to_p_dict,csv_to_p_hash]
    a = perf_counter()
    impThings = [[i(b), perf_counter()] for i in test]
    impThings[0][1], impThings[1][1],impThings[2][1] = impThings[0][1] - a, impThings[1][1] - impThings[0][1],impThings[2][1] - impThings[1][1]
    return impThings

def toTime(str):
    arr = str.split(" ")
    time = 0.0
    if len(arr) >= 6:
        time += int(arr[0][1:]) * 60
        time += int(arr[2])
    if len(arr) >=4:
        time += int(arr[0][1:])
    if len(arr) >= 2:
        time += int(arr[-2]) / 60
    return time


def accessing(structures,b):
    bst = structures[0][0]
    dict = structures[1][0]
    hasher = structures[2][0]
    a = perf_counter()
    accessTimes = []
    """for key in b:
        bst.find(key)[2] = toTime(bst.find(key)[2])"""
    accessTimes.append(perf_counter()-a)
    a = perf_counter()
    for key in b:
        dict[key[0]][2] = toTime(dict[key[0]][2])
    accessTimes.append(perf_counter()-a)
    a = perf_counter()
    for key in b:
        lst = hasher.get(key[0])
        lst[2] = toTime(hasher.get(key[0])[2])
    accessTimes.append(perf_counter()-a)
    return accessTimes

    
times = []
b = [get_key(line) for line in open("final.csv", "r")]

structures = main(b)
for i in structures:
    times.append(i[1])
accessTimes = accessing(structures,b)
for i in accessTimes:
    times.append(i)
grapher = {}
grapher["structure"] = ["BST", "built-in Dict", "Glesener Dict"]
grapher["build time"] = times[:3]
grapher["access time"] = times[3:]
grapher["total time"] = [times[i]+times[2*i] for i in range(3)]

df = pandas.DataFrame.from_dict(grapher)
rdf = pandas.DataFrame.from_dict(structures[1][0])
print(rdf)
sns.set_theme(style="whitegrid")
plot = sns.catplot(data = df, kind = "bar", x = "structure",y="build time",
    ci="sd", palette="pastel", alpha=.6, height=6)
plot.despine(left=True)
plot.set_axis_labels("", "Time(sec)")
plot.savefig("lm.png")
plot = sns.catplot(data = df, kind = "bar", x = "structure",y="access time",
    ci="sd", palette="pastel", alpha=.6, height=6)
plot.despine(left=True)
plot.set_axis_labels("", "Time(sec)")
plot.savefig("lm2.png")
plot = sns.catplot(data = df, kind = "bar", x = "structure",y="total time",
    ci="sd", palette="pastel", alpha=.6, height=6)
plot.despine(left=True)
plot.set_axis_labels("", "Time(sec)")
plot.savefig("lm3.png")
scat = sns.scatterplot(data = df)
