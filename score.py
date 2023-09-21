## import pickle
student = dict()

while True:
    select = int(input('1. 입력 2.검색 3.수정 4.삭제 5.출력 6.종료\n'))
    
    if select == 1:
        id=input('학번 : ')
            
        if ( id not in student) == True:
            name = input('이름 : ')
            kor = int(input('국어 : '))
            eng = int(input('영어 : '))
            math = int(input('수학 : '))
            print('입력 완료')
            total = kor+eng+math
            avg = round(total/3,3)
            
            student[id] = [name,kor,eng,math,total,avg]
                       
            continue
        else:
            print('학생이 이미 존재')
            
    if select == 2:
        search = input('학번 : ')
        
        if(search in student) == True:
            info = student[id]
            print('이름\t국어\t영어\t수학\t총점\t평균\t')
            for i in range(len(info)):
                print(info[i:i+1],end='\t')
            print()
            continue
        else:
            print('학생 존재 X ')
    
    if select == 3:
        update = input('수정할 학생의 학번을 입력 : ')
            
        if(update in student) == True:
            name = input('이름 입력 : ')
            kor =  int(input('국어 성적: '))
            eng =  int(input('영어 성적: '))
            math = int(input('수학 성적: '))
            print('성적 입력 완료.')

            score = kor+eng+math
            avg = round(score/3, 3)
            
            student[update] = [name,kor,eng,math,score,avg]
            continue
        else:
            print('학생이 존재하지 않음')
            continue
    

    
    if select == 4:
        delete = input('삭제할 학번 : ')
        
        if(delete in student) == True:
            student.pop(delete)
            print('삭제 완료')
            continue
        else:
            print('학생 정보 X')
            continue
    
    
    if select == 5:
        for id in student:
            print('학번: ', id,'이름: ', name)
            print('[이름]\t\t[국어]\t[영어]\t[수학]\t[총점]\t[평균]')
            
            info = student[id]
            for i in range(len(info)):
                print(info[i:i+1],end='\t')
            
            print()
            continue
    if select == 6:
        break