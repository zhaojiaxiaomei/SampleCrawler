import matplotlib.pyplot as plt
from BookType import run as tyrun
from BookTop import run as torun


def typePie(typedf):
    '''
    查找每个分类的分类数量并生成分类数量饼状图
    :param typedf:
    :return:
    '''
    typel=list(set(typedf['type0']))
    typelist=[]
    for t in typel:
        newdf=typedf[typedf.type0==t]
        num=sum(newdf['num'])
        typelist.append([t,num])
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.pie([i[1] for i in typelist],labels=[i[0]+':'+str(i[1]) for i in typelist],startangle=90,autopct='%1.1f%%')
    plt.title('豆瓣不同分类图书数量饼状图')
    plt.savefig('分类饼状图.png')
    plt.show()


def takeSecond(elem):
    '''
    选取排序的key
    :param elem:
    :return:
    '''
    return elem[1]


def topBar(topdf):
    '''
    豆瓣Top250经典图书的国家出处柱状图
    :param topdf:
    :return:
    '''
    topl = list(set(topdf['nation']))
    topList=[]
    print(topl)
    for t in topl:
        newdf = topdf[topdf.nation == t]
        num=newdf.shape[0]
        topList.append([t,num])
    topList.sort(key=takeSecond)
    plt.rcParams['font.sans-serif'] = ['SimHei']
    yhname = [i[0] for i in topList]
    yhcolleges = [i[1] for i in topList]
    fig, ax = plt.subplots()
    fig.tight_layout()
    b = ax.barh(range(len(yhname)), yhcolleges, color='#5F9EA0')
    for rect in b:
        w = rect.get_width()
        ax.text(w, rect.get_y() + rect.get_height() / 2, w, ha='left', va='center', color='#008B8B')
    ax = plt.gca()
    ax.set_yticks(range(len(yhname)))
    ax.set_yticklabels(yhname)
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    plt.title('豆瓣Top250经典图书的国家出处柱状图')
    plt.xlabel('数量')
    plt.ylabel('国家')
    plt.show()


def topBarYear(topdf):
    '''
    豆瓣Top250经典图书出版年份柱状图
    :param topdf:
    :return:
    '''
    topl = list(set(topdf['year']))
    topList=[]
    for t in topl:
        newdf = topdf[topdf.year == t]
        num=newdf.shape[0]
        topList.append([t,num])
    topList.sort(key=takeSecond)
    plt.rcParams['font.sans-serif'] = ['SimHei']
    yhname = [i[0] for i in topList]
    yhcolleges = [i[1] for i in topList]
    fig, ax = plt.subplots()
    fig.tight_layout()
    b = ax.barh(range(len(yhname)), yhcolleges, color='#5F9EA0')
    for rect in b:
        w = rect.get_width()
        ax.text(w, rect.get_y() + rect.get_height() / 2, w, ha='left', va='center', color='#008B8B')
    ax = plt.gca()
    ax.set_yticks(range(len(yhname)))
    ax.set_yticklabels(yhname)
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    plt.title('豆瓣Top250经典图书出版年份柱状图')
    plt.xlabel('数量')
    plt.ylabel('年份')
    plt.show()


if __name__ == '__main__':
    typedf=tyrun()
    topdf=torun()
    topBarYear(topdf)
    topBar(topdf)
    typePie(typedf)