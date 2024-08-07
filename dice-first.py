a = [1,2,3,4,5,6]
b = [1,2,3,4,5,6]

# possible combinations

def possible_comb(a,b):
    counter = 0
    for i in a:
        for j in b:
            counter = counter + 1
            print("combination no:", counter)
            print("a=",i,"b=",j)
            
    print("Total Possible combinations:",counter)

def sum(a,b):
    sum = []
    counter = 0
    for i in a:
        for j in b:
            k = i + j
            if k in sum:
                continue
            else:
                counter = counter + 1
                print("combination no:", counter, ",value:",k )
                sum.append(k)
    print("possible combinations: ",sum)
    print("no of combinations: ", counter)
    return sum
#possible_comb(a,b)

c = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
def new_comb(a,b,c):
    series = []
    series2 = []
    for i in a:
        for j in b:
            k = i +j
            series.append(k)
            #print(k)
    for l in c:
        count = series.count(l)
        print("possibility of:",l,"is",series.count(l),"/36")
        print(count)
        series.append(count)
    print(series2[:])
new_comb(a,b,c)