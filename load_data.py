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

    resultcodes = soup.find_all('resultcode') # 결과 코드
    resultmsgs = soup.find_all('resultmsg')   # 결과 메세지
    numofrowss = soup.find_all('numofrows')   # 한 페이지 결과 수
    pagenos = soup.find_all('pageno')         # 페이지 번호
    totalcounts = soup.find_all('totalcount') # 전체 결과 수
    sgids = soup.find_all('sgid')             # 선거 ID
    sgtypecodes = soup.find_all('sgtypecode') # 선거 종류 코드
    sgnames = soup.find_all('sgname')         # 선거명
    sgvotedates = soup.find_all('sgvotedate') # 선거일자
    nums = soup.find_all('num')               # 결과순서

    return resultcodes, resultmsgs, numofrowss, pagenos, totalcounts, sgids, sgtypecodes, sgnames, sgvotedates, nums

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

    resultcodes = soup.find_all('resultcode') # 결과 코드
    resultmsgs = soup.find_all('resultmsg')   # 결과 메세지
    numofrowss = soup.find_all('numofrows')   # 한 페이지 결과 수
    pagenos = soup.find_all('pageno')         # 페이지 번호
    totalcounts = soup.find_all('totalcount') # 전체 결과 수
    sgids = soup.find_all('sgid')             # 선거 ID
    sgtypecodes = soup.find_all('sgtypecode') # 선거 종류 코드
    huboids = soup.find_all('huboid')         # 후보자 ID
    sggnames = soup.find_all('sggname')       # 선거구명
    sdnames = soup.find_all('시도명')         # 시도명
    wiwnames = soup.find_all('wiwname')       # 구시군명
    jdnames = soup.find_all('jdname')         # 정당명
    names = soup.find_all('name')             # 성명
    hanjanames = soup.find_all('hanjaname')   # 한자성명
    genders = soup.find_all('gender')         # 성별
    birthdays = soup.find_all('birthday')     # 생년월일
    ages = soup.find_all('age')               # 연령
    addrs = soup.find_all('addr')             # 주소
    jobids = soup.find_all('jobid')           # 직업 ID
    jobs = soup.find_all('job')               # 직업
    eduids = soup.find_all('eduid')           # 학력 ID
    edus = soup.find_all('edu')               # 학력
    career1s = soup.find_all('career1')       # 경력1
    career2s = soup.find_all('career2')       # 경력2
    regdates = soup.find_all('regdate')       # 등록일
    statuss = soup.find_all('status')         # 등록상태
    nums = soup.find_all('num')               # 결과순서

    return resultcodes, resultmsgs, numofrowss, pagenos, totalcounts, sgids, sgtypecodes, huboids, sggnames, sdnames, wiwnames, jdnames, names, hanjanames, genders, birthdays, ages, addrs, jobids, jobs, eduids, edus, career1s, career2s, regdates, statuss, nums

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

    resultcodes = soup.find_all('resultcode') # 결과 코드
    resultmsgs = soup.find_all('resultmsg')   # 결과 메세지
    numofrowss = soup.find_all('numofrows')   # 한 페이지 결과 수
    pagenos = soup.find_all('pageno')         # 페이지 번호
    totalcounts = soup.find_all('totalcount') # 전체 결과 수
    sgids = soup.find_all('sgid')             # 선거 ID
    evpsnames = soup.find_all('evpsname')     # 사전투표소명
    sdnames = soup.find_all('sdname')         # 시도명
    wiwnames = soup.find_all('wiwname')       # 위원회명
    emdnames = soup.find_all('emdname')       # 읍면동명
    evorders = soup.find_all('evorder')       # 순서
    placenames = soup.find_all('placename')   # 건물명
    addrs = soup.find_all('addr')             # 주소
    floors = soup.find_all('floor')           # 층
    nums = soup.find_all('num')               # 결과순서

    return resultcodes, resultmsgs, numofrowss, pagenos, totalcounts, sgids, evpsnames, sdnames, wiwnames, emdnames, evorders, placenames, addrs, floors, nums

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

    resultcodes = soup.find_all('resultcode') # 결과 코드
    resultmsgs = soup.find_all('resultmsg')   # 결과 메세지
    numofrowss = soup.find_all('numofrows')   # 한 페이지 결과 수
    pagenos = soup.find_all('pageno')         # 페이지 번호
    totalcounts = soup.find_all('totalcount') # 전체 결과 수
    sgids = soup.find_all('sgid')             # 선거 ID
    sgtypecodes = soup.find_all('sgtypecode') # 선거 종류 코드
    sdnames = soup.find_all('sdname')         # 시도명
    wiwnames = soup.find_all('wiwname')       # 구시군명
    totsunsus = soup.find_all('totsunsu')     # 총선거인수
    pssunsus = soup.find_all('pssunsu')       # 선거일투표 선거인수
    psetcsunsus = soup.find_all('psetcsunsu') # 거소·사전·선상·재외 선거인수
    tottusus = soup.find_all('tottusu')       # 총 투표자수
    pstusus = soup.find_all('pstusu')         # 선거일 투표자수
    psetctusus = soup.find_all('psetctusu')   # 거소·사전·선상·재외 투표자수
    turnouts = soup.find_all('turnout')       # 투표율
    vrorders = soup.find_all('vrorder')       # 정렬 순서
    nums = soup.find_all('num')               # 결과 순서

    return resultcodes, resultmsgs, numofrowss, pagenos, totalcounts, sgids, sgtypecodes, sdnames, wiwnames, totsunsus, pssunsus, psetcsunsus, tottusus, pstusus, psetctusus, turnouts, vrorders, nums

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

    resultcodes = soup.find_all('resultcode') # 결과 코드
    resultmsgs = soup.find_all('resultmsg')   # 결과 메세지
    numofrowss = soup.find_all('numofrows')   # 한 페이지 결과 수
    pagenos = soup.find_all('pageno')         # 페이지 번호
    totalcounts = soup.find_all('totalcount') # 전체 결과 수
    sgids = soup.find_all('sgid')             # 선거 ID
    sgtypecodes = soup.find_all('sgtypecode') # 선거 종류 코드
    huboids = soup.find_all('huboid')         # 후보자 ID
    sggnames = soup.find_all('sggname')       # 선거구명
    sdnames = soup.find_all('sdname')         # 시도명
    wiwnames = soup.find_all('wiwname')       # 구시군명
    gihos = soup.find_all('giho')             # 기호
    gihosangses = soup.find_all('gihosangse') # 기호상세
    jdnames = soup.find_all('jdname')         # 정당명
    names = soup.find_all('name')             # 한글성명
    hanjanames = soup.find_all('hanjaname')   # 한자성명
    genders = soup.find_all('gender')         # 성별
    birthdays = soup.find_all('birthday')     # 생년월일
    ages = soup.find_all('age')               # 연령
    addrs = soup.find_all('addr')             # 주소
    jobids = soup.find_all('jobid')           # 직업 ID
    jobs = soup.find_all('job')               # 직업
    eduids = soup.find_all('eduid')           # 학력 ID
    edus = soup.find_all('edu')               # 학력
    career1s = soup.find_all('career1')       # 경력1
    career2s = soup.find_all('career2')       # 경력2
    dugsus = soup.find_all('dugsu')           # 득표수
    dugyuls = soup.find_all('dugyul')         # 득표율
    nums = soup.find_all('num')               # 결과순서

    return resultcodes, resultmsgs, numofrowss, pagenos, totalcounts, sgids, sgtypecodes, huboids, sggnames, sdnames, wiwnames, gihos, gihosangses, jdnames, names, hanjanames, genders, birthdays, ages, addrs, jobids, jobs, eduids, edus, career1s, career2s, dugsus, dugyuls, nums

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

    resultcodes = soup.find_all('resultcode')             # 결과 코드
    resultmsgs = soup.find_all('resultmsg')               # 결과 메세지
    numofrowss = soup.find_all('numofrows')               # 한 페이지 결과 수
    pagenos = soup.find_all('pageno')                     # 페이지 번호
    totalcounts = soup.find_all('totalcount')             # 전체 결과 수
    nums = soup.find_all('num')                           # 결과순서
    sgids = soup.find_all('sgid')                         # 선거 ID
    countingsttnnames = soup.find_all('countingsttnname') # 개표소명
    sdnames = soup.find_all('sdname')                     # 시도명
    wiwnames = soup.find_all('wiwname')                   # 위원회명
    countingsttnseqs = soup.find_all('countingsttnseq')   # 개표소순번
    placenames = soup.find_all('placename')               # 장소명
    placeaddrs = soup.find_all('placeaddr')               # 장소주소
    placefloors = soup.find_all('placefloor')             # 장소층수

    return resultcodes, resultmsgs, numofrowss, pagenos, totalcounts, nums, sgids, countingsttnnames, sdnames, wiwnames, countingsttnseqs, placenames, placeaddrs, placefloors

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

    resultcodes = soup.find_all('resultcode')             # 결과 코드
    resultmsgs = soup.find_all('resultmsg')               # 결과 메세지
    numofrowss = soup.find_all('numofrows')               # 한 페이지 결과 수
    pagenos = soup.find_all('pageno')                     # 페이지 번호
    totalcounts = soup.find_all('totalcount')             # 전체 결과 수
    nums = soup.find_all('num')                           # 결과순서
    sgids = soup.find_all('sgid')                         # 선거 ID
    ervotingdivs = soup.find_all('ervotingdiv')           # 사전투표구분
    sdnames = soup.find_all('sdname')                     # 시도명
    wiwnames = soup.find_all('wiwname')                   # 위원회명
    voterscnts = soup.find_all('voterscnt')               # 선거인수
    ervotingcnts = soup.find_all('ervotingcnt')           # 사전투표자수
    erturnouts = soup.find_all('erturnout')               # 사전투표율
    sortords = soup.find_all('sortord')                   # 정렬순서

    return resultcodes, resultmsgs, numofrowss, pagenos, totalcounts, nums, sgids, ervotingdivs, sdnames, wiwnames, voterscnts, ervotingcnts, erturnouts, sortords

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

    resultcodes = soup.find_all('resultcode')             # 결과 코드
    resultmsgs = soup.find_all('resultmsg')               # 결과 메세지
    numofrowss = soup.find_all('numofrows')               # 한 페이지 결과 수
    pagenos = soup.find_all('pageno')                     # 페이지 번호
    totalcounts = soup.find_all('totalcount')             # 전체 결과 수
    nums = soup.find_all('num')                           # 결과순서
    sgids = soup.find_all('sgid')                         # 선거 ID
    sgtypecodes = soup.find_all('sgtypecode')             # 선거종류코드
    cnddtids = soup.find_all('cnddtid')                   # 후보자 ID
    sggnames = soup.find_all('sggname')                   # 선거구명
    sidonames = soup.find_all('sidoname')                 # 시도명
    wiwnames = soup.find_all('wiwname')                   # 구시군명
    partynames = soup.find_all('partyname')               # 정당명
    krnames = soup.find_all('partyname')                  # 한글명
    cnnames = soup.find_all('cnname')                     # 한자명
    prmscnts = soup.find_all('prmscnt')                   # 공약개수
    prmsord1s = soup.find_all('prmsord1')                 # 공약순번1
    prmsrealmname1s = soup.find_all('prmsrealmname1')     # 공약분야명1
    prmstitle1s = soup.find_all('prmstitle1')             # 공약제목명1
    prmscont1s = soup.find_all('prmscont1')               # 공약내용1
    prmsord10s = soup.find_all('prmsord10')               # 공약순번10
    prmsrealmname10s = soup.find_all('prmsrealmname10')   # 공약분야명10
    prmstitle10s = soup.find_all('prmstitle10')           # 공약제목명10
    prmscont10s = soup.find_all('prmscont10')             # 공약내용10

    return resultcodes, resultmsgs, numofrowss, pagenos, totalcounts, nums, sgids, sgtypecodes, cnddtids, sggnames, sidonames, wiwnames, partynames, krnames, cnnames, prmscnts, prmsord1s, prmsrealmname1s, prmstitle1s, prmscont1s, prmsord10s, prmsrealmname10s, prmstitle10s, prmscont10s

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

    resultcodes = soup.find_all('resultcode')             # 결과 코드
    resultmsgs = soup.find_all('resultmsg')               # 결과 메세지
    numofrowss = soup.find_all('numofrows')               # 한 페이지 결과 수
    pagenos = soup.find_all('pageno')                     # 페이지 번호
    totalcounts = soup.find_all('totalcount')             # 전체 결과 수
    nums = soup.find_all('num')                           # 결과순서
    sgids = soup.find_all('sgid')                         # 선거 ID
    partynames = soup.find_all('partyname')               # 정당명
    prmscnts = soup.find_all('prmscnt')                   # 공약개수
    prmsord1s = soup.find_all('prmsord1')                 # 공약순번1
    prmsrealmname1s = soup.find_all('prmsrealmname1')     # 공약분야명1
    prmstitle1s = soup.find_all('prmstitle1')             # 공약제목명1
    prmscont1s = soup.find_all('prmscont1')               # 공약내용1
    prmsord10s = soup.find_all('prmsord10')               # 공약순번10
    prmsrealmname10s = soup.find_all('prmsrealmname10')   # 공약분야명10
    prmstitle10s = soup.find_all('prmstitle10')           # 공약제목명10
    prmscont10s = soup.find_all('prmscont10')             # 공약내용10

    return resultcodes, resultmsgs, numofrowss, pagenos, totalcounts, nums, sgids, partynames, prmscnts, prmsord1s, prmsrealmname1s, prmstitle1s, prmscont1s, prmsord10s, prmsrealmname10s, prmstitle10s, prmscont10s

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

    resultcodes = soup.find_all('resultcode')             # 결과 코드
    resultmsgs = soup.find_all('resultmsg')               # 결과 메세지
    numofrowss = soup.find_all('numofrows')               # 한 페이지 결과 수
    pagenos = soup.find_all('pageno')                     # 페이지 번호
    totalcounts = soup.find_all('totalcount')             # 전체 결과 수
    nums = soup.find_all('num')                           # 결과순서
    sgids = soup.find_all('sgid')                         # 선거 ID
    sgtypecodes = soup.find_all('sgtypecode')             # 선거종류코드
    sdnames = soup.find_all('sdname')                     # 시도명
    sggnames = soup.find_all('sggname')                   # 선거구명
    jdnames = soup.find_all('jdname')                     # 정당명
    names = soup.find_all('name')                         # 한글성명
    hanjanames = soup.find_all('hanjaname')               # 한자성명
    genders = soup.find_all('gender')                     # 성별
    birthdays = soup.find_all('birthday')                 # 생년월일
    ages = soup.find_all('age')                           # 연령
    jobids = soup.find_all('jobid')                       # 직업코드
    jobs = soup.find_all('job')                           # 직업
    eduids = soup.find_all('eduid')                       # 학력코드
    edus = soup.find_all('edu')                           # 학력
    career1s = soup.find_all('career1')                   # 경력1
    career2s = soup.find_all('career2')                   # 경력2

    return resultcodes, resultmsgs, numofrowss, pagenos, totalcounts, nums, sgids, sgtypecodes, sdnames, sggnames, jdnames, names, hanjanames, genders, birthdays, ages, jobids, jobs, eduids, edus, career1s, career2s

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

    resultcodes = soup.find_all('resultcode')                        # 결과 코드
    resultmsgs = soup.find_all('resultmsg')                          # 결과 메세지
    numofrowss = soup.find_all('numofrows')                          # 한 페이지 결과 수
    pagenos = soup.find_all('pageno')                                # 페이지 번호
    otalcounts = soup.find_all('totalcount')                         # 전체 결과 수
    nums = soup.find_all('num')                                      # 결과순서
    sgids = soup.find_all('sgid')                                    # 선거 ID
    sdnames = soup.find_all('sdname')                                # 시도명
    wiwnames = soup.find_all('wiwname')                              # 구시군명
    sggnames = soup.find_all('sggname')                              # 선거구명
    wiwcounts = soup.find_all('wiwcount')                            # 구시군수
    emdcounts = soup.find_all('emdcount')                            # 읍면동수
    tpgcounts = soup.find_all('tpgcount')                            # 투표구수
    ppltcnts = soup.find_all('ppltcnt')                              # 인구수
    ntabppltcnts = soup.find_all('ntabppltcnt')                      # 인구수(재외국민)
    frgnrppltcnts = soup.find_all('frgnrppltcnt')                    # 인구수(외국인)
    cfmtnelcnts = soup.find_all('cfmtnelcnt')                        # 확정선거인수(계)
    cfmtnracnts = soup.find_all('cfmtnracnt')                        # 확정선거인수(계_재외국민)
    cfmtnfrgnrcnts = soup.find_all('cfmtnfrgnrcnt')                  # 확정선거인수(계_외국인)
    cfmtnmanelcnts = soup.find_all('cfmtnmanelcnt')                  # 확정선거인수(남)
    cfmtnmanracnts = soup.find_all('cfmtnmanracnt')                  # 확정선거인수(남_재외국민)
    cfmtnmanfrgnrcnts = soup.find_all('cfmtnmanfrgnrcnt')            # 확정선거인수(남_외국인)
    cfmtnfmlelcnts = soup.find_all('cfmtnfmlelcnt')                  # 확정선거인수(여)
    fmtnfmlracnts = soup.find_all('cfmtnfmlracnt')                   # 확정선거인수(여_재외국민)
    cfmtnfmlfrgnrcnts = soup.find_all('cfmtnfmlfrgnrcnt')            # 확정선거인수(여_외국인)
    cfmtnrdvtdccnts = soup.find_all('cfmtnrdvtdccnt')                # 거소투표 신고인명부 등재자수(계)
    cfmtnntabrdvtdccnts = soup.find_all('cfmtnntabrdvtdccnt')        # 거소투표 신고인명부 등재자수(계_재외국민)
    cfmtnrdvtmandccnts = soup.find_all('cfmtnrdvtmandccnt')          # 거소투표 신고인명부 등재자수(남)
    cfmtnntabrdvtmandccnts = soup.find_all('cfmtnntabrdvtmandccnt')  # 거소투표 신고인명부 등재자수(남_재외국민)
    cfmtnrdvtfmldccnts = soup.find_all('cfmtnrdvtfmldccnt')          # 거소투표 신고인명부 등재자수(여)
    cfmtnntabrdvtfmldccnts = soup.find_all('cfmtnntabrdvtfmldccnt')  # 거소투표 신고인명부 등재자수(여_재외국민)

    return resultcodes, resultmsgs, numofrowss, pagenos, otalcounts, nums, sgids, sdnames, wiwnames, sggnames, wiwcounts, emdcounts, tpgcounts, ppltcnts, ntabppltcnts, frgnrppltcnts, cfmtnelcnts, cfmtnracnts, cfmtnfrgnrcnts, cfmtnmanelcnts, cfmtnmanracnts, cfmtnmanfrgnrcnts, cfmtnfmlelcnts, fmtnfmlracnts, cfmtnfmlfrgnrcnts, cfmtnrdvtdccnts, cfmtnntabrdvtdccnts, cfmtnrdvtmandccnts, cfmtnntabrdvtmandccnts, cfmtnrdvtfmldccnts, cfmtnntabrdvtfmldccnts
