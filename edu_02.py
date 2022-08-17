import sys
#-*- coding:utf-8 -*-
fr = open(sys.argv[1],'r')
fr_rm = sys.argv[1].split('.')[0]
fw = open(fr_rm+'_align.txt','w')

dic = {}
sumseq = ''
YN = True


# pseudo ITS는 Internal Transcribed Spacer의 약자로서 ribosomal RNA (rRNA) 유전자 구간에서 large subunit 유전자와 small subunit 유전자 사이에 있는 non-coding DNA이다. 박테리아나 고세균에서는 16s rRNA와 23s rRNA 사이에 위치해 있으며 eukaryote경우에는 18s와 5.8s rRNA 유전자 사이에 ITS1이 존재하며, 5.8s 와 28s (식물에서는 26s) 사이에 ITS2가 존재하여, 총 두 개의 ITS가 존재한다

# pseudo 유전자 구간 보존성

ITS 구간은 rRNA 유전자 구간 상에 존재하는데, 단백질 합성에 반드시 필요한 Ribosome의 유전자는 현 생물에게 있어 없어서는 안 되며, 잘 보전되어야 하는 유전자이다. 따라서 해당 구간 역시 정상적인 ribosome 발현을 위해 잘 보전되고 있으며, ITS 구간 양 쪽의 rRNA 구간은 모든 생물에서 그 염기서열이 잘 보존되어 있다. 따라서 거의 모든 생물 분류군 범위에서 ITS 구간 분석이 가능하며, 염기서열분석을 위한 프라이머가 넓은 생물 범위에서 잘 구축되어 있거나 사용될 수 있다.

염기서열 증폭의 용이성

ITS 구간은 길이가 길지 않아 Sanger sequencing으로도 쉽게 분석이 가능하며, ribosomal gene repeat으로 인해 rRNA cluster의 copy number가 많아 적은 양의 DNA만으로도 쉽게 증폭이 가능하다.

빠른 변이 속도

해당 구간은 ribosomal subunit gene과는 달리 변이 속도가 빨라 계통학적으로 가까운 분류군 사이에서도 사용이 가능하다. 심지어는 한 개체 내에서 ribosomal gene repeat끼리도 변이 타입이 존재하는 경우도 흔히 발견된다.

for line in fr:
  if YN: 
    YN = False
    oldLineStSp = line.strip().split("\t")
    oldTargetName = lineStSp[0]
    oldGeneName = lineStSp[4]
  else:
    lineStSp =line.strip().split("\t")
    targetName = lineStSp[0]
    geneName = lineStSp[2]
    seq = lineStSp[4]
    if oldTargetName == targetName:
      sumseq += seq
      print("sumseq :"+sumseq)
      continue
    else:
      print ("targetName :" + targetName)
      oldTargetName = targetName
      print ("oldTargetName :" + oldTargetName)
      if geneName == "ITS":
        print("ITS :" geneName)
        fw.write(sumseq+ "\n")
        sumseq = ""
      if geneName == "28S":
        print("28S :"+ geneName)
        fw.write(sumseq+"\n")
        sumseq = ""


fw.write(sumseq+"\n")