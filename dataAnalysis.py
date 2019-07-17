import pandas as pd
import matplotlib.pyplot as plt


def readFile():
    f = open('movieTop250.csv',encoding='UTF-8')
    df = pd.read_csv(f)
    return df


def analysisYear(moviedf):
    yearList=[]
    result=[['1930s',0],['1940s',0],['1950s',0]
        , ['1960s', 0],['1970s', 0],['1980s', 0]
            ,['1990s', 0],['2000s', 0],['2010s', 0]]
    for s in moviedf['info']:
        s="".join(s.split()).split('/')
        yearList.append(s[0][:4])
    yearl=list(set(yearList))
    for i in yearl:
        n=0
        for j in yearList:
            if i==j:
                n+=1
        if int(i)<1940:
            result[0][1]+=n
        elif int(i)>=1940 and int(i)<1950:
            result[1][1] += n
        elif int(i)>=1950 and int(i)<1960:
            result[2][1] += n
        elif int(i) >= 1960 and int(i) < 1970:
            result[3][1] += n
        elif int(i) >= 1970 and int(i) < 1980:
            result[4][1] += n
        elif int(i) >= 1980 and int(i) < 1990:
            result[5][1] += n
        elif int(i) >= 1990 and int(i) < 2000:
            result[6][1] += n
        elif int(i) >= 2000 and int(i) < 2010:
            result[7][1] += n
        else:
            result[8][1] += n
    return result

def printYear(result):
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.bar([i for i in range(len(result))], [i[1] for i in result], width=0.3)
    for i in range(len(result)):
        plt.text(i - 0.1, result[i][1] + 0.3, result[i][1])
    plt.xticks([i for i in range(len(result))], [i[0] for i in result], rotation=1)
    plt.title('经典电影每个年代电影数量')
    plt.ylabel('数量')
    plt.savefig('year.png')
    plt.show()


if __name__ == '__main__':
    df=readFile()
    result=analysisYear(df)
    printYear(result)
