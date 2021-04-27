data = [10,20,30,30,40,50,50,60,60,70,40,80,90]
def remove_duplicates(duplist):
    noduplist = []
    for element in duplist:
        if element not in noduplist:
            noduplist.append(element)
    return noduplist
print(remove_duplicates(data))
    