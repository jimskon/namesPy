# James Skon, 2020
from sortedcontainers import SortedDict
from nameEntry import nameEntry

class nameMap:
  """
  Class to store information about the 
  Statistics of names.
  For each name type, there is a dict
  for each name, there is a list of name %, cumulative %, rank
  """
  def __init__(self,nameFile : str):
    """
    create a new list of names with data
    given an index within range of 0..num-1
    """
    try:
      names = open(nameFile)
    except IOError:
      print("Error opening file:"+nameFile)
      return
    self.namemap=SortedDict()
    for line in names:
      nameData=nameEntry(line)
      self.namemap[nameData.name]=nameData
    return

  def lookup(self,name):
    """
    lookup name in map
    return nameEntry
    else return none
    """
    results = self.namemap.get(name.upper())
    return results

  def lookup10(self,name):
    """
    lookup name in specified index
    return json list of matches
    else return none
    """
    
    i=self.namemap.bisect_right(name.upper())
    low = max(0,i-5)
    high = min(len(self.namemap),i+5)
    result = "{\"matches\":["
    for j in range(low,high):
      nametuple = self.namemap.peekitem(j)
      result+=nametuple[1].json()+","
    # remove last comma
    result=result[:-1]
    result += "]}"
    return result


