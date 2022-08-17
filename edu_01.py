import sys 
# pseudo sys라는 module import 
#* sys.argv에서 sys는 파이썬 인터프리터와 관련된 정보와 기능을 제공하는 모듈 혹은 라이브러리이며, argv는 위에 적은 것처럼 argument를 의미한다. 

f = open(sys.argv[1],'r')
# pseudo commend를 실행할 때 첫번째 인자로 넣은 파일을 읽기 모드로 읽어들임

fw = open(sys.argv[1].split('.')[0]+'.txt','w')
# pseudo sys.argv[1].split('.')[0]의 코드를 쓰기 모드로 오픈
# pseudo 아마 sys.argv[1]로 넣은 제목의 텍스트 파일을 생성?
lines = f.readlines()


s = True #pseudo 핸들러 변수 
a = '' #pseudo a 변수 선언
i = 0 


for b in lines:
# pseudo b라는 변수에 lines를 반복해서 넣고
    if b.startswith('>'): # pseudo 만약에 문자열이 ">"로 시작한다면
    
        if s: # pseudo 그게 true라면
            fw.write(b.split('>')[1].strip('\n')+'\t')
            # pseudo fw파일에 >로 시작하는 문자열에서 >빼고 엔터랑 공백하나 추가
            s = False
            # pseudo 핸들러 변수 적용
        else: #pseudo 아니면
            fw.write(str(i)+'\n'+b.split('>')[1].strip('\n')+'\t')
            # pseudo 숫자 0을 문자 "0"으로 변환 + 엔터 + >로 시작하는 문자열에서 엔터랑 공백하나 추가
            a = '' # pseudo a 리셋

    else: # pseudo >로 시작하지 않으면 
        a = a.replace('\n','') # pseudo a는 a에서 엔터 제거 
        a += b #pseudo a에 b를 더한 것을 a라고 선언
        i = len(a) #pseudo i는 a 문자의 개수

# pseudo test.fasta 파일을 인수로 넣으면
# pseudo test.txt 파일이 나옴
# pseudo 크로모솜당 염기의 개수를 세서 아이디 옆에 문자인 숫자로 출력하는 파일



fw.write(str(i))
fw.close()
f.close()