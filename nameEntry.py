class nameEntry:
  """
  Class to store data for a single name
  """
  def __init__(self, line : str):
    """
    Takes a single line and parses it into
    the fields
    """
    line=line.strip()
    data=line.split()
    self.name=data[0]
    self.percent=data[1]
    self.cumulative=data[2]
    self.rank=data[3]

  def json(self):
    result = "{\"name\":\""+self.name+"\","
    result +="\"percent\":"+self.percent+","
    result +="\"cumulative\":"+self.cumulative+","
    result +="\"rank\":"+self.rank+"}"
    return result

