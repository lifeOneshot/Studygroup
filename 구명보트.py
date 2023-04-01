def solution(people, limit):
    people.sort(reverse = True)
    count = 0
    for i in people:
        if(i + people[-1] <= limit): #두 명 태우고 작은 인원 삭제
            people.pop(-1)
                       
        count += 1
    
        
    return count
