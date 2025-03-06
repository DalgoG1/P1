def p1(arr: list[int], n:int, j:int, m:int, i:int) -> int:
    arrTemp = arr
    if i > m-2:
        return sum(arrTemp[:j])
    if i <= m-2:
        if arrTemp[i+2] < arrTemp[i] and  arrTemp[i+2] < arrTemp[i+1]:
            arrTemp[i], arrTemp[i+1], arrTemp[i+2] = arrTemp[i+2], arrTemp[i], arrTemp[i+1]
            return p1(arr, n, j, m-1, i+1)

        if arrTemp[i+1] < arrTemp[i]:
            arrTemp[i], arrTemp[i+1] = arrTemp[i+1], arrTemp[i]
            return p1(arr, n, j, m-1, i+1)
        
        return p1(arr, n, j, m-1, i+1)
            
print(p1([5,2,13,91,73,1,13,1,43,21,31,3,7], 13, 7, 20, 0)) # 0