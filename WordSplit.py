def WordSplit(strArr):

  # code goes here
  word = strArr[0]
  lis = strArr[1]
  strArr = "not possible"
  for i in range(len(word)):
    f = word[:i]
    r = word[i:]
    if f in lis and r in lis:
      strArr = [f, r]
      break
  return strArr

# keep this function call here 
print(WordSplit(input())) #["baseball", "a,all,b,ball,bas,base,cat,code,d,e,quit,z"]