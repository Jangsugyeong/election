# -*- coding: utf-8 -*-
import lxml
import requests
from bs4 import BeautifulSoup
import pandas as pd

def code_load_data(servicekey, pageNo, numOfRows):
    """
    코드 정보 조회 데이터
    --------------------

    parameters
    --------------------
    servicekey : api 키
    pageNo : 페이지 번호
    numOfRows : 한 페이지 결과 수
    """

    # 데이터 불러오기
    url = 'http://apis.data.go.kr/9760000/CommonCodeService/getCommonSgCodeList'
    params = {'serviceKey' : servicekey, 'pageNo' : pageNo, 'numOfRows' : numOfRows}
    response = requests.get(url, params = params)
    soup = BeautifulSoup(response.content, 'lxml')

    resultcode = soup.find_all('resultcode') # 결과 코드
    resultmsg = soup.find_all('resultmsg')   # 결과 메세지
    numofrows = soup.find_all('numofrows')   # 한 페이지 결과 수
    pageno = soup.find_all('pageno')         # 페이지 번호
    totalcount = soup.find_all('totalcount') # 전체 결과 수
    sgid = soup.find_all('sgid')             # 선거 ID
    sgtypecode = soup.find_all('sgtypecode') # 선거 종류 코드
    sgname = soup.find_all('sgname')         # 선거명
    sgvotedate = soup.find_all('sgvotedate') # 선거일자
    num = soup.find_all('num')               # 결과순서

    return resultcode, resultmsg, numofrows, pageno, totalcount, sgid, sgtypecode, sgname, sgvotedate, num

def hubo_load_data(servicekey, pageNo, numOfRows, sgId, sgTypecode, sggName, sdName):
    """
    후보자 정보
    --------------------

    parameters
    --------------------
    servicekey : api 키
    pageNo : 페이지 번호
    numOfRows : 한 페이지 결과 수
    sgId : 선거 ID
    sgTypecode : 선거종류코드
    sggName : 선거구명
    sdName : 시도명
    """

    # 데이터 불러오기
    url = 'http://apis.data.go.kr/9760000/PofelcddInfoInqireService/getPoelpcddRegistSttusInfoInqire'
    params = {'serviceKey' : servicekey, 'pageNo' : pageNo, 'numOfRows' : numOfRows, 'sgId' : sgId, 'sgTypecode' : sgTypecode, 'sggName' : sggName, 'sdName' : sdName}
    response = requests.get(url, params = params)
    soup = BeautifulSoup(response.content, "lxml")

    resultcode = soup.find_all('resultcode') # 결과 코드
    resultmsg = soup.find_all('resultmsg')   # 결과 메세지
    numofrows = soup.find_all('numofrows')   # 한 페이지 결과 수
    pageno = soup.find_all('pageno')         # 페이지 번호
    totalcount = soup.find_all('totalcount') # 전체 결과 수
    sgid = soup.find_all('sgid')             # 선거 ID
    sgtypecode = soup.find_all('sgtypecode') # 선거 종류 코드
    huboid = soup.find_all('huboid')         # 후보자 ID
    sggname = soup.find_all('sggname')       # 선거구명
    sdname = soup.find_all('시도명')         # 시도명
    wiwname = soup.find_all('wiwname')       # 구시군명
    jdname = soup.find_all('jdname')         # 정당명
    name = soup.find_all('name')             # 성명
    hanjaname = soup.find_all('hanjaname')   # 한자성명
    gender = soup.find_all('gender')         # 성별
    birthday = soup.find_all('birthday')     # 생년월일
    age = soup.find_all('age')               # 연령
    addr = soup.find_all('addr')             # 주소
    jobid = soup.find_all('jobid')           # 직업 ID
    job = soup.find_all('job')               # 직업
    eduid = soup.find_all('eduid')           # 학력 ID
    edu = soup.find_all('edu')               # 학력
    career1 = soup.find_all('career1')       # 경력1
    career2 = soup.find_all('career2')       # 경력2
    regdate = soup.find_all('regdate')       # 등록일
    status = soup.find_all('status')         # 등록상태
    num = soup.find_all('num')               # 결과순서

    return resultcode, resultmsg, numofrows, pageno, totalcount, sgid, sgtypecode, huboid, sggname, sdname, wiwname, jdname, name, hanjaname, gender, birthday, age, addr, jobid, job, eduid, edu, career1, career2, regdate, status, num

def polls_load_data(servicekey, pageNo, numOfRows, sgId, sdName, wiwname):
    """
    사전 및 선거일 투표소 정보
    --------------------

    parameters
    --------------------
    servicekey : api 키
    pageNo : 페이지 번호
    numOfRows : 한 페이지 결과 수
    sgId : 선거 ID
    sdName : 시도명
    wiwName : 위원회명
    """

    # 데이터 불러오기
    url = 'http://apis.data.go.kr/9760000/PolplcInfoInqireService2/getPrePolplcOtlnmapTrnsportInfoInqire'
    params = {'serviceKey' : servicekey, 'pageNo' : pageNo, 'numOfRows' : numOfRows, 'sgId' : sgId, 'sdName' : sdName, 'wiwName' : wiwname}
    response = requests.get(url, params = params)
    soup = BeautifulSoup(response.content, "lxml")

    resultcode = soup.find_all('resultcode') # 결과 코드
    resultmsg = soup.find_all('resultmsg')   # 결과 메세지
    numofrows = soup.find_all('numofrows')   # 한 페이지 결과 수
    pageno = soup.find_all('pageno')         # 페이지 번호
    totalcount = soup.find_all('totalcount') # 전체 결과 수
    sgid = soup.find_all('sgid')             # 선거 ID
    evpsname = soup.find_all('evpsname')     # 사전투표소명
    sdname = soup.find_all('sdname')         # 시도명
    wiwname = soup.find_all('wiwname')       # 위원회명
    emdname = soup.find_all('emdname')       # 읍면동명
    evorder = soup.find_all('evorder')       # 순서
    placename = soup.find_all('placename')   # 건물명
    addr = soup.find_all('addr')             # 주소
    floor = soup.find_all('floor')           # 층
    num = soup.find_all('num')               # 결과순서

    return resultcode, resultmsg, numofrows, pageno, totalcount, sgid, evpsname, sdname, wiwname, emdname, evorder, placename, addr, floor, num

def vote_load_data(servicekey, pageNo, numOfRows, sgId, sgTypecode, sdName, wiwName):
    """
    투개표 정보
    --------------------

    parameters
    --------------------
    servicekey : api 키
    pageNo : 페이지 번호
    numOfRows : 한 페이지 결과 수
    sgId : 선거 ID
    sgTypecode : 선거종류코드
    sdName : 시도명
    wiwName : 구시군명
    """

    # 데이터 불러오기
    url = 'http://apis.data.go.kr/9760000/VoteXmntckInfoInqireService2/getVoteSttusInfoInqire'
    params = {'serviceKey' : servicekey, 'pageNo' : pageNo, 'numOfRows' : numOfRows, 'sgId' : sgId, 'sgTypecode' : sgTypecode, 'sdName' : sdName, 'wiwName' : wiwName}
    response = requests.get(url, params = params)
    soup = BeautifulSoup(response.content, 'lxml')

    resultcode = soup.find_all('resultcode') # 결과 코드
    resultmsg = soup.find_all('resultmsg')   # 결과 메세지
    numofrows = soup.find_all('numofrows')   # 한 페이지 결과 수
    pageno = soup.find_all('pageno')         # 페이지 번호
    totalcount = soup.find_all('totalcount') # 전체 결과 수
    sgid = soup.find_all('sgid')             # 선거 ID
    sgtypecode = soup.find_all('sgtypecode') # 선거 종류 코드
    sdname = soup.find_all('sdname')         # 시도명
    wiwname = soup.find_all('wiwname')       # 구시군명
    totsunsu = soup.find_all('totsunsu')     # 총선거인수
    pssunsu = soup.find_all('pssunsu')       # 선거일투표 선거인수
    psetcsunsu = soup.find_all('psetcsunsu') # 거소·사전·선상·재외 선거인수
    tottusu = soup.find_all('tottusu')       # 총 투표자수
    pstusu = soup.find_all('pstusu')         # 선거일 투표자수
    psetctusu = soup.find_all('psetctusu')   # 거소·사전·선상·재외 투표자수
    turnout = soup.find_all('turnout')       # 투표율
    vrorder = soup.find_all('vrorder')       # 정렬 순서
    num = soup.find_all('num')               # 결과 순서

    return resultcode, resultmsg, numofrows, pageno, totalcount, sgid, sgtypecode, sdname, wiwname, totsunsu, pssunsu, psetcsunsu, tottusu, pstusu, psetctusu, turnout, vrorder, num

def winner_load_data(servicekey, pageNo, numOfRows, sgId, sgTypecode, sdName, sggName):
    """
    당선인 정보
    --------------------

    parameters
    --------------------
    servicekey : api 키
    pageNo : 페이지 번호
    numOfRows : 한 페이지 결과 수
    sgId : 선거 ID
    sgTypecode : 선거 종류
    sdName : 시도명
    sggName : 선거구명
    """

    # 데이터 불러오기
    url = 'http://apis.data.go.kr/9760000/WinnerInfoInqireService2/getWinnerInfoInqire'
    params = {'serviceKey' : servicekey, 'pageNo' : pageNo, 'numOfRows' : numOfRows, 'sgId' : sgId, 'sgTypecode' : sgTypecode, 'sdName' : sdName, 'sggName' : sggName}
    response = requests.get(url, params = params)
    soup = BeautifulSoup(response.content, "lxml")

    resultcode = soup.find_all('resultcode') # 결과 코드
    resultmsg = soup.find_all('resultmsg')   # 결과 메세지
    numofrows = soup.find_all('numofrows')   # 한 페이지 결과 수
    pageno = soup.find_all('pageno')         # 페이지 번호
    totalcount = soup.find_all('totalcount') # 전체 결과 수
    sgid = soup.find_all('sgid')             # 선거 ID
    sgtypecode = soup.find_all('sgtypecode') # 선거 종류 코드
    huboid = soup.find_all('huboid')         # 후보자 ID
    sggname = soup.find_all('sggname')       # 선거구명
    sdname = soup.find_all('sdname')         # 시도명
    wiwname = soup.find_all('wiwname')       # 구시군명
    giho = soup.find_all('giho')             # 기호
    gihosangse = soup.find_all('gihosangse') # 기호상세
    jdname = soup.find_all('jdname')         # 정당명
    name = soup.find_all('name')             # 한글성명
    hanjaname = soup.find_all('hanjaname')   # 한자성명
    gender = soup.find_all('gender')         # 성별
    birthday = soup.find_all('birthday')     # 생년월일
    age = soup.find_all('age')               # 연령
    addr = soup.find_all('addr')             # 주소
    jobid = soup.find_all('jobid')           # 직업 ID
    job = soup.find_all('job')               # 직업
    eduid = soup.find_all('eduid')           # 학력 ID
    edu = soup.find_all('edu')               # 학력
    career1 = soup.find_all('career1')       # 경력1
    career2 = soup.find_all('career2')       # 경력2
    dugsu = soup.find_all('dugsu')           # 득표수
    dugyul = soup.find_all('dugyul')         # 득표율
    num = soup.find_all('num')               # 결과순서

    return resultcode, resultmsg, numofrows, pageno, totalcount, sgid, sgtypecode, huboid, sggname, sdname, wiwname, giho, gihosangse, jdname, name, hanjaname, gender, birthday, age, addr, jobid, job, eduid, edu, career1, career2, dugsu, dugyul, num

def counting_place_load_data(servicekey, pageNo, numOfRows, sgId, sdName, wiwName):
    """
    개표소 정보
    --------------------

    parameters
    --------------------
    servicekey : api 키
    pageNo : 페이지 번호
    numOfRows : 한 페이지 결과 수
    sgId : 선거 ID
    sdName : 시도명
    wiwName : 위원회명
    """

    # 데이터 불러오기
    url = 'http://apis.data.go.kr/9760000/CountingSttnInfoInqireService/getCountingSttnInfoInqire'
    params = {'serviceKey' : servicekey, 'pageNo' : pageNo, 'numOfRows' : numOfRows, 'sgId' : sgId, 'sdName' : sdName, 'wiwName' : wiwName}
    response = requests.get(url, params = params)
    soup = BeautifulSoup(response.content, "lxml")

    resultcode = soup.find_all('resultcode')             # 결과 코드
    resultmsg = soup.find_all('resultmsg')               # 결과 메세지
    numofrows = soup.find_all('numofrows')               # 한 페이지 결과 수
    pageno = soup.find_all('pageno')                     # 페이지 번호
    totalcount = soup.find_all('totalcount')             # 전체 결과 수
    num = soup.find_all('num')                           # 결과순서
    sgid = soup.find_all('sgid')                         # 선거 ID
    countingsttnname = soup.find_all('countingsttnname') # 개표소명
    sdname = soup.find_all('sdname')                     # 시도명
    wiwname = soup.find_all('wiwname')                   # 위원회명
    countingsttnseq = soup.find_all('countingsttnseq')   # 개표소순번
    placename = soup.find_all('placename')               # 장소명
    placeaddr = soup.find_all('placeaddr')               # 장소주소
    placefloor = soup.find_all('placefloor')             # 장소층수

    return resultcode, resultmsg, numofrows, pageno, totalcount, num, sgid, countingsttnname, sdname, wiwname, countingsttnseq, placename, placeaddr, placefloor

def early_voting_load_data(servicekey, pageNo, numOfRows, sgId, erVotingDiv, sdName, wiwName):
    """
    사전 투표 정보
    --------------------

    parameters
    --------------------
    servicekey : api 키
    pageNo : 페이지 번호
    numOfRows : 한 페이지 결과 수
    sgId : 선거 ID
    erVotingDiv : 사전 투표 구분
    sdName : 시도명
    wiwName : 위원회명
    """

    # 데이터 불러오기
    url = 'http://apis.data.go.kr/9760000/ErVotingSttusInfoInqireService/getErVotingSttusInfoInqire'
    params = {'serviceKey' : servicekey, 'pageNo' : pageNo, 'numOfRows' : numOfRows, 'sgId' : sgId, 'erVotingDiv' : erVotingDiv, 'sdName' : sdName, 'wiwName' : wiwName}
    response = requests.get(url, params = params)
    soup = BeautifulSoup(response.content, "lxml")

    resultcode = soup.find_all('resultcode')             # 결과 코드
    resultmsg = soup.find_all('resultmsg')               # 결과 메세지
    numofrows = soup.find_all('numofrows')               # 한 페이지 결과 수
    pageno = soup.find_all('pageno')                     # 페이지 번호
    totalcount = soup.find_all('totalcount')             # 전체 결과 수
    num = soup.find_all('num')                           # 결과순서
    sgid = soup.find_all('sgid')                         # 선거 ID
    ervotingdiv = soup.find_all('ervotingdiv')           # 사전투표구분
    sdname = soup.find_all('sdname')                     # 시도명
    wiwname = soup.find_all('wiwname')                   # 위원회명
    voterscnt = soup.find_all('voterscnt')               # 선거인수
    ervotingcnt = soup.find_all('ervotingcnt')           # 사전투표자수
    erturnout = soup.find_all('erturnout')               # 사전투표율
    sortord = soup.find_all('sortord')                   # 정렬순서

    return resultcode, resultmsg, numofrows, pageno, totalcount, num, sgid, ervotingdiv, sdname, wiwname, voterscnt, ervotingcnt, erturnout, sortord

def election_promises_load_data(servicekey, pageNo, numOfRows, sgId, sgTypecode, cnddtId):
    """
    선거 공약 정보
    --------------------

    parameters
    --------------------
    servicekey : api 키
    pageNo : 페이지 번호
    numOfRows : 목록 건수
    sgId : 선거 ID
    sgTypecode : 선거종류코드
    cnddtld : 후보자 ID
    """

    # 데이터 불러오기
    url = 'http://apis.data.go.kr/9760000/ElecPrmsInfoInqireService/getCnddtElecPrmsInfoInqire'
    params = {'serviceKey' : servicekey, 'pageNo' : pageNo, 'numOfRows' : numOfRows, 'sgId' : sgId, 'sgTypecode' : sgTypecode, 'cnddtId' : cnddtId}
    response = requests.get(url, params = params)
    soup = BeautifulSoup(response.content, "lxml")

    resultcode = soup.find_all('resultcode')             # 결과 코드
    resultmsg = soup.find_all('resultmsg')               # 결과 메세지
    numofrows = soup.find_all('numofrows')               # 한 페이지 결과 수
    pageno = soup.find_all('pageno')                     # 페이지 번호
    totalcount = soup.find_all('totalcount')             # 전체 결과 수
    num = soup.find_all('num')                           # 결과순서
    sgid = soup.find_all('sgid')                         # 선거 ID
    sgtypecode = soup.find_all('sgtypecode')             # 선거종류코드
    cnddtid = soup.find_all('cnddtid')                   # 후보자 ID
    sggname = soup.find_all('sggname')                   # 선거구명
    sidoname = soup.find_all('sidoname')                 # 시도명
    wiwname = soup.find_all('wiwname')                   # 구시군명
    partyname = soup.find_all('partyname')               # 정당명
    krname = soup.find_all('partyname')                  # 한글명
    cnname = soup.find_all('cnname')                     # 한자명
    prmscnt = soup.find_all('prmscnt')                   # 공약개수
    prmsord1 = soup.find_all('prmsord1')                 # 공약순번1
    prmsrealmname1 = soup.find_all('prmsrealmname1')     # 공약분야명1
    prmstitle1 = soup.find_all('prmstitle1')             # 공약제목명1
    prmscont1 = soup.find_all('prmscont1')               # 공약내용1
    prmsord10 = soup.find_all('prmsord10')               # 공약순번10
    prmsrealmname10 = soup.find_all('prmsrealmname10')   # 공약분야명10
    prmstitle10 = soup.find_all('prmstitle10')           # 공약제목명10
    prmscont10 = soup.find_all('prmscont10')             # 공약내용10

    return resultcode, resultmsg, numofrows, pageno, totalcount, num, sgid, sgtypecode, cnddtid, sggname, sidoname, wiwname, partyname, krname, cnname, prmscnt, prmsord1, prmsrealmname1, prmstitle1, prmscont1, prmsord10, prmsrealmname10, prmstitle10, prmscont10

def party_policies_load_data(servicekey, pageNo, numOfRows, sgId, partyName):
    """
    정당 정책 정보
    --------------------

    parameters
    --------------------
    servicekey : api 키
    pageNo : 페이지 번호
    numOfRows : 목록 건수
    sgId : 선거 ID
    partyName : 정당명
    """

    url = 'http://apis.data.go.kr/9760000/PartyPlcInfoInqireService/getPartyPlcInfoInqire'
    params = {'serviceKey' : servicekey, 'pageNo' : pageNo, 'numOfRows' : numOfRows, 'sgId' : sgId, 'partyName' : partyName}
    response = requests.get(url, params = params)
    soup = BeautifulSoup(response.content, "lxml")

    resultcode = soup.find_all('resultcode')             # 결과 코드
    resultmsg = soup.find_all('resultmsg')               # 결과 메세지
    numofrows = soup.find_all('numofrows')               # 한 페이지 결과 수
    pageno = soup.find_all('pageno')                     # 페이지 번호
    totalcount = soup.find_all('totalcount')             # 전체 결과 수
    num = soup.find_all('num')                           # 결과순서
    sgid = soup.find_all('sgid')                         # 선거 ID
    partyname = soup.find_all('partyname')               # 정당명
    prmscnt = soup.find_all('prmscnt')                   # 공약개수
    prmsord1 = soup.find_all('prmsord1')                 # 공약순번1
    prmsrealmname1 = soup.find_all('prmsrealmname1')     # 공약분야명1
    prmstitle1 = soup.find_all('prmstitle1')             # 공약제목명1
    prmscont1 = soup.find_all('prmscont1')               # 공약내용1
    prmsord10 = soup.find_all('prmsord10')               # 공약순번10
    prmsrealmname10 = soup.find_all('prmsrealmname10')   # 공약분야명10
    prmstitle10 = soup.find_all('prmstitle10')           # 공약제목명10
    prmscont10 = soup.find_all('prmscont10')             # 공약내용10

    return resultcode, resultmsg, numofrows, pageno, totalcount, num, sgid, partyname, prmscnt, prmsord1, prmsrealmname1, prmstitle1, prmscont1, prmsord10, prmsrealmname10, prmstitle10, prmscont10

def non_voting_load_data(servicekey, pageNo, numOfRows, sgId, sgTypecode, sdName, resultType = 'xml'):
    """
    무투표선거구 정보
    --------------------

    parameters
    --------------------
    servicekey : api 키
    pageNo : 페이지 번호
    numOfRows : 한 페이지 결과 수
    sgId : 선거 ID
    sgTypecode : 선거종류코드
    sdName : 시도명
    resultType : 데이터포맷('xml', 'json')
    """

    url = 'http://apis.data.go.kr/9760000/WtvtelpcInfoInqireService/getWtvtelpccndaInfoInqire'
    params = {'serviceKey' : servicekey, 'pageNo' : pageNo, 'numOfRows' : numOfRows, 'resultType' : resultType, 'sgId' : sgId, 'sgTypecode' : sgTypecode, 'sdName' : sdName}
    response = requests.get(url, params = params)
    soup = BeautifulSoup(response.content, "lxml")

    resultcode = soup.find_all('resultcode')             # 결과 코드
    resultmsg = soup.find_all('resultmsg')               # 결과 메세지
    numofrows = soup.find_all('numofrows')               # 한 페이지 결과 수
    pageno = soup.find_all('pageno')                     # 페이지 번호
    totalcount = soup.find_all('totalcount')             # 전체 결과 수
    num = soup.find_all('num')                           # 결과순서
    sgid = soup.find_all('sgid')                         # 선거 ID
    sgtypecode = soup.find_all('sgtypecode')             # 선거종류코드
    sdname = soup.find_all('sdname')                     # 시도명
    sggname = soup.find_all('sggname')                   # 선거구명
    jdname = soup.find_all('jdname')                     # 정당명
    name = soup.find_all('name')                         # 한글성명
    hanjaname = soup.find_all('hanjaname')               # 한자성명
    gender = soup.find_all('gender')                     # 성별
    birthday = soup.find_all('birthday')                 # 생년월일
    age = soup.find_all('age')                           # 연령
    jobid = soup.find_all('jobid')                       # 직업코드
    job = soup.find_all('job')                           # 직업
    eduid = soup.find_all('eduid')                       # 학력코드
    edu = soup.find_all('edu')                           # 학력
    career1 = soup.find_all('career1')                   # 경력1
    career2 = soup.find_all('career2')                   # 경력2

    return resultcode, resultmsg, numofrows, pageno, totalcount, num, sgid, sgtypecode, sdname, sggname, jdname, name, hanjaname, gender, birthday, age, jobid, job, eduid, edu, career1, career2

def number_of_electors_load_data(servicekey, pageNo, numOfRows, sgId, sgTypecode, sdName, wiwName, resultType = 'xml'):
    """
    선거인 수 현황
    --------------------

    parameters
    --------------------
    servicekey : api 키
    pageNo : 페이지 번호
    numOfRows : 한 페이지 결과 수
    sgId : 선거 ID
    sgTypecode : 선거종류코드
    sdName : 시도명
    wiwName : 구시군명
    resultType : 데이터포맷('xml', 'json')
    """

    # 데이터 불러오기
    url = 'http://apis.data.go.kr/9760000/ElcntInfoInqireService/getElpcElcntInfoInqire'
    params = {'serviceKey' : servicekey, 'pageNo' : pageNo, 'numOfRows' : numOfRows, 'resultType' : resultType, 'sgId' : sgId, 'sgTypecode' : sgTypecode, 'sdName' : sdName, 'wiwName' : wiwName}
    response = requests.get(url, params = params)
    soup = BeautifulSoup(response.content, "lxml")

    resultcode = soup.find_all('resultcode')                        # 결과 코드
    resultmsg = soup.find_all('resultmsg')                          # 결과 메세지
    numofrows = soup.find_all('numofrows')                          # 한 페이지 결과 수
    pageno = soup.find_all('pageno')                                # 페이지 번호
    otalcount = soup.find_all('totalcount')                         # 전체 결과 수
    num = soup.find_all('num')                                      # 결과순서
    sgid = soup.find_all('sgid')                                    # 선거 ID
    sdname = soup.find_all('sdname')                                # 시도명
    wiwname = soup.find_all('wiwname')                              # 구시군명
    sggname = soup.find_all('sggname')                              # 선거구명
    wiwcount = soup.find_all('wiwcount')                            # 구시군수
    emdcount = soup.find_all('emdcount')                            # 읍면동수
    tpgcount = soup.find_all('tpgcount')                            # 투표구수
    ppltcnt = soup.find_all('ppltcnt')                              # 인구수
    ntabppltcnt = soup.find_all('ntabppltcnt')                      # 인구수(재외국민)
    frgnrppltcnt = soup.find_all('frgnrppltcnt')                    # 인구수(외국인)
    cfmtnelcnt = soup.find_all('cfmtnelcnt')                        # 확정선거인수(계)
    cfmtnracnt = soup.find_all('cfmtnracnt')                        # 확정선거인수(계_재외국민)
    cfmtnfrgnrcnt = soup.find_all('cfmtnfrgnrcnt')                  # 확정선거인수(계_외국인)
    cfmtnmanelcnt = soup.find_all('cfmtnmanelcnt')                  # 확정선거인수(남)
    cfmtnmanracnt = soup.find_all('cfmtnmanracnt')                  # 확정선거인수(남_재외국민)
    cfmtnmanfrgnrcnt = soup.find_all('cfmtnmanfrgnrcnt')            # 확정선거인수(남_외국인)
    cfmtnfmlelcnt = soup.find_all('cfmtnfmlelcnt')                  # 확정선거인수(여)
    fmtnfmlracnt = soup.find_all('cfmtnfmlracnt')                   # 확정선거인수(여_재외국민)
    cfmtnfmlfrgnrcnt = soup.find_all('cfmtnfmlfrgnrcnt')            # 확정선거인수(여_외국인)
    cfmtnrdvtdccnt = soup.find_all('cfmtnrdvtdccnt')                # 거소투표 신고인명부 등재자수(계)
    cfmtnntabrdvtdccnt = soup.find_all('cfmtnntabrdvtdccnt')        # 거소투표 신고인명부 등재자수(계_재외국민)
    cfmtnrdvtmandccnt = soup.find_all('cfmtnrdvtmandccnt')          # 거소투표 신고인명부 등재자수(남)
    cfmtnntabrdvtmandccnt = soup.find_all('cfmtnntabrdvtmandccnt')  # 거소투표 신고인명부 등재자수(남_재외국민)
    cfmtnrdvtfmldccnt = soup.find_all('cfmtnrdvtfmldccnt')          # 거소투표 신고인명부 등재자수(여)
    cfmtnntabrdvtfmldccnt = soup.find_all('cfmtnntabrdvtfmldccnt')  # 거소투표 신고인명부 등재자수(여_재외국민)

    return resultcode, resultmsg, numofrows, pageno, otalcount, num, sgid, sdname, wiwname, sggname, wiwcount, emdcount, tpgcount, ppltcnt, ntabppltcnt, frgnrppltcnt, cfmtnelcnt, cfmtnracnt, cfmtnfrgnrcnt, cfmtnmanelcnt, cfmtnmanracnt, cfmtnmanfrgnrcnt, cfmtnfmlelcnt, fmtnfmlracnt, cfmtnfmlfrgnrcnt, cfmtnrdvtdccnt, cfmtnntabrdvtdccnt, cfmtnrdvtmandccnt, cfmtnntabrdvtmandccnt, cfmtnrdvtfmldccnt, cfmtnntabrdvtfmldccnt
