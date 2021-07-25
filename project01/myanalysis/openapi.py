import bs4
import pandas as pd
import requests
import datetime

def decide():
    now = datetime.datetime.now()
    endDt = now.strftime('%Y%m%d')
    now7 = now - datetime.timedelta(days=7)
    startDt = now7.strftime('%Y%m%d')

    url='http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19InfStateJson?serviceKey=23S7ZYj%2BtnwtbEN09iKFg%2B4O9%2Fw2AtdiXKey2plFT%2BcbFUhh065aLcPqpnkgeoPfK58B11wEi25a4%2Fg1c7M98A%3D%3D&pageNo=1&numOfRows=10&startCreateDt='+startDt+'&endCreateDt='+endDt;
    result = requests.get(url);
    response = result.text.encode('utf-8');
    xml_obj = bs4.BeautifulSoup(response, 'lxml-xml');
    rows = xml_obj.find_all('item');

    result = []         # 최종 리스트
    nameList = []       # 컬럼 명

    rowsLen = len(rows);    # item의 개수
    for i in range(rowsLen) :
        item = rows[i].find_all();
        itemData = []  # 아이템의 데이터
        for j in range(len(item)) :
            if i == 0 :
                nameList.append(item[j].name);
            text = item[j].text;
            itemData.append(text);
        result.append(itemData);

    data = pd.DataFrame(result, columns=nameList);
        # Index(['accDefRate', 'accExamCnt', 'accExamCompCnt', 'careCnt', 'clearCnt',
        #        'createDt', 'deathCnt', 'decideCnt', 'examCnt', 'resutlNegCnt', 'seq',
        #        'stateDt', 'stateTime', 'updateDt'],
        #       dtype='object')
    data = data.astype({'decideCnt':int});
    results = data['decideCnt'].to_list();
    print(results);
    return results

def clear():
    now = datetime.datetime.now()
    endDt = now.strftime('%Y%m%d')
    now7 = now - datetime.timedelta(days=7)
    startDt = now7.strftime('%Y%m%d')

    url='http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19InfStateJson?serviceKey=23S7ZYj%2BtnwtbEN09iKFg%2B4O9%2Fw2AtdiXKey2plFT%2BcbFUhh065aLcPqpnkgeoPfK58B11wEi25a4%2Fg1c7M98A%3D%3D&pageNo=1&numOfRows=10&startCreateDt='+startDt+'&endCreateDt='+endDt;
    result = requests.get(url);
    response = result.text.encode('utf-8');
    xml_obj = bs4.BeautifulSoup(response, 'lxml-xml');
    rows = xml_obj.find_all('item');

    result = []         # 최종 리스트
    nameList = []       # 컬럼 명

    rowsLen = len(rows);    # item의 개수
    for i in range(rowsLen) :
        item = rows[i].find_all();
        itemData = []  # 아이템의 데이터
        for j in range(len(item)) :
            if i == 0 :
                nameList.append(item[j].name);
            text = item[j].text;
            itemData.append(text);
        result.append(itemData);

    data = pd.DataFrame(result, columns=nameList);
    data = data.astype({'clearCnt':int});
    results = data['clearCnt'].to_list();
    print(results);
    return results

def death():
    now = datetime.datetime.now()
    endDt = now.strftime('%Y%m%d')
    now7 = now - datetime.timedelta(days=7)
    startDt = now7.strftime('%Y%m%d')

    url='http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19InfStateJson?serviceKey=23S7ZYj%2BtnwtbEN09iKFg%2B4O9%2Fw2AtdiXKey2plFT%2BcbFUhh065aLcPqpnkgeoPfK58B11wEi25a4%2Fg1c7M98A%3D%3D&pageNo=1&numOfRows=10&startCreateDt='+startDt+'&endCreateDt='+endDt;
    result = requests.get(url);
    response = result.text.encode('utf-8');
    xml_obj = bs4.BeautifulSoup(response, 'lxml-xml');
    rows = xml_obj.find_all('item');

    result = []         # 최종 리스트
    nameList = []       # 컬럼 명

    rowsLen = len(rows);    # item의 개수
    for i in range(rowsLen) :
        item = rows[i].find_all();
        itemData = []  # 아이템의 데이터
        for j in range(len(item)) :
            if i == 0 :
                nameList.append(item[j].name);
            text = item[j].text;
            itemData.append(text);
        result.append(itemData);

    data = pd.DataFrame(result, columns=nameList);
    data = data.astype({'deathCnt':int});
    results = data['deathCnt'].to_list();
    print(results);
    return results

if __name__ == '__main__' :
    open();