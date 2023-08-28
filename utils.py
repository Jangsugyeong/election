# -*- coding: utf-8 -*-
import lxml
import requests
from bs4 import BeautifulSoup
import pandas as pd

def save_excel(df):
    '''
    데이터 프레임을 엑셀로 저장
    --------------------

    parameters
    --------------------
    df : 엑셀로 저장할 데이터 프레임
    '''
    df.to_excel(f'{df}.xlsx', index = False, engine = 'openpyxl')


def load_code(sgids, sgtypecodes, sgnames, sgvotedates):
    '''
    선거 코드 정보 불러오기
    '''
    # 빈 리스트 생성
    sgid_list, sgtypecode_list, sgname_list, sgvotedate_list = []
    
    for sgid, sgtypecode, sgname, sgvotedate in zip(sgids, sgtypecodes, sgnames, sgvotedates):
        sgid_list.append(sgid.get_text())
        sgtypecode_list.append(sgtypecode.get_text())
        sgname_list.append(sgname.get_text())
        sgvotedate_list.append(sgvotedate.get_text())

    df = pd.DataFrame({
        "선거 ID" : sgid_list,
        "선거종류코드" : sgtypecode_list,
        "선거명" : sgname_list,
    })

    return df