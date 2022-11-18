array=[ ]

if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        lst=[ ]
        lst.append(name)
        lst.append(score)
        array.append(lst)

    min_value=min(array, key=lambda x: x[1])
    #print(min_value)
    array.remove(min_value)
    #print(min_value)
    
    for m in array:
        print(m)
        if min_value[1]==m[1]:
            print(m)
            array.remove(m)
            print(array)

    #print(array)
    min_value=min(array, key=lambda x: x[1])
    #print(min_value)
    sorted_array=sorted(array)


    for n in sorted_array:
        if n[1]==min_value[1]:
            print(n[0])
        else:
            pass
    
