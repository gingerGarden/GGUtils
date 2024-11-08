from typing import List, Any, Tuple
from collections.abc import Callable

import time, datetime
import numpy as np




def make_numpy_arange(start:int, end:int, plus:bool=True)->np.ndarray:
    """
    start, end 사이에 np.arange()를 적용
        - start와 end가 동일한 경우, end에 +1을 하거나 start에 -1을 하여 size가 반드시 1 이상인 array가 생성되게 한다.

    Args:
        start (int): np.arange의 start
        end (int): np.arange의 end
        plus (bool, optional): 기본적으로 end += 1이 적용되나, plus=False 경우 start에 -1함. Defaults to True.

    Returns:
        np.ndarray: np.arange()의 결과
    """
    if start == end:
        if plus:
            end += 1
        else:
            start -= 1
    return np.arange(start, end)


def list_flatten(lists:List[List[Any]])->List[Any]:
    """list 안에 list들이 혼합되어 있는 경우, 이를 1개의 list로 병합한다

    Args:
        lists (List[List[Any]]): list 안에 list가 들어 있는 list

    Returns:
        List[Any]: 1개의 list
    """
    stack = []
    for item in lists:
        if isinstance(item, list):
            stack.extend(list_flatten(item))
        else:
            stack.append(item)
    return stack


def current_time(only_time:bool=True)->str:
    """현재 시간(날짜)를 반환한다.

    Args:
        only_time (bool, optional): 시간만 반환할지 여부(False인 경우, 날짜와 함께 반환). Defaults to True.

    Returns:
        str: 현재 시간의 문자열
    """
    format = "%H:%M:%S" if only_time else "%Y.%m.%d %H:%M:%S"
    return datetime.datetime.today().strftime(format)


def time_checker(start:float) -> str:
    """start(float: time.time())부터 time_checker() 코드 실행까지 걸린 시간을 깔끔하게 출력
    Example: '0:01:55.60'

    Args:
        start (float): 소수초

    Returns:
        str: "시:분:초.밀리초" 형식의 문자열
    """
    # 소모 시간 측정
    end = time.time()
    second_delta = (end - start)
    result = decimal_seconds_to_time_string(decimal_s=second_delta)
    
    return result


def decimal_seconds_to_time_string(decimal_s:float)->str:
    """소수 초 단위 시간을 받아 "시:분:초.밀리초" 형식의 문자열로 변환

    Args:
        decimal_s (_type_): 소수초                                                                                                                                                                                                                                                                                   
    Returns:
        str: "시:분:초.밀리초" 형식의 문자열
    """
    time_delta = datetime.timedelta(seconds=decimal_s)
    str_time_delta = str(time_delta).split(".")
    time1 = str_time_delta[0]
    if len(str_time_delta) == 1:
        time2 = "00"
    else:
        time2 = str_time_delta[1][:2]
    return f"{time1}.{time2}"



