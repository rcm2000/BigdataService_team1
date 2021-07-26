import bs4
import pandas as pd
import requests
import datetime
import sys

class OpenAPI:
    def high(self):
        now = datetime.datetime.now()
        now1 = now.strftime('%Y%m%d')

        now2 = now - datetime.timedelta(days=1)
        now2 = now2.strftime('%Y%m%d')

        for n in [now1, now2]:
            url = 'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19InfStateJson?serviceKey=23S7ZYj%2BtnwtbEN09iKFg%2B4O9%2Fw2AtdiXKey2plFT%2BcbFUhh065aLcPqpnkgeoPfK58B11wEi25a4%2Fg1c7M98A%3D%3D&pageNo=1&numOfRows=10&startCreateDt=' + n + '&endCreateDt=' + n;
            result = requests.get(url);
            response = result.text.encode('utf-8');
            xml_obj = bs4.BeautifulSoup(response, 'lxml-xml');
            rows = xml_obj.find_all('item');

            if len(rows) != 0:
                continue;

        item = rows[0].find_all();
        itemData = []  # 아이템의 데이터
        for j in range(len(item)):
            text = item[j].text;
            itemData.append(text);

        # nameIndx = ['accDefRate', 'accExamCnt', 'accExamCompCnt', 'careCnt', 'clearCnt',
        #            'createDt', 'deathCnt', 'decideCnt', 'examCnt', 'resutlNegCnt', 'seq',
        #            'stateDt', 'stateTime', 'updateDt'];
        nameIndx = ['누적 확진률', '누적 검사 수', '누적 검사 완료 수', '치료중 환자 수', '격리해제 수',
                    '등록일시분초', '사망자 수', '확진자 수', '검사진행 수', '결과 음성 수', '게시글번호',
                    '기준일', '기준시간', '수정일시분초']
        colIndx = ['', '#BE3075', '', '#EB001F', '#64A12D', '', '#FFED00', '#000000', '#008AC5', '#009EE0']

        data = [];
        for i in [7,4,8,3]:
            data.append([nameIndx[i], round(int(itemData[i])/10000)])

        results = {'d1':data[0], 'd2':data[1], 'd3':data[2], 'd4':data[3]}
        print(results)
        return results

if __name__ == '__main__' :
    OpenAPI().high()
