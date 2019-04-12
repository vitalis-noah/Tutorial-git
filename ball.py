#Part.1 スクリプト言語 Pythonの基本

#リスト１(p.010)
print("◆リスト１ ------")
a=4/3
p=3.14
r=15/2
r3=r**3

print(a*p*r3)
print("球体の体積は " + str(a*p*r3) + " です")
print("球体の体積は%fです"%(a*p*r3))

#リスト３(p.011)
print("◆リスト３ ------")
def show(name,val):
  return name + "=" + str(val)

print( show("a ", a) )
print( show("p ", p) )
print( show("r ", r) )
print( show("r3", r3) )

#図14
print("◆図14「リスト」 ------")
varNames = ['ai','pi','ri','r3i']

for i in range(len(varNames)):
  print(varNames[i])

for d in varNames:
  print(d)

#図15 (p.011～012)
print("◆図15「リスト」 ------")
print(varNames)
varNames.remove('ai')
print(varNames)
varNames.insert(0,'ai')
print(varNames)
varNames.append('rEnd')
print(varNames)

print("      「タプル」:変更不可")
varNamesTpl = ('at','pt','rt','r3t')
print(varNamesTpl)

print("      「集合」:重複不可")
varNamesSet = {'as','ps','rs','r3s','r3s'}
print(varNamesSet)

print("「集合」による辞書")
namesVals = {'a':4/3, 'p':3.14, 'r':15/2}
print(namesVals)
print(namesVals['p'])

