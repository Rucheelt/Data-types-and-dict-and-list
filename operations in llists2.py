def harg(lst):
    result={}
    for item in lst:
        result[item[0]]=item[1:]
    return result

student=[[1,'RAM',17],[2,'SHAM',18],[3,'SUNG',16]]
print("original list:",student)
print("\n \n converted list",harg(student))