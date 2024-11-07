from typing import Dict, Optional, Union, Any, Callable, List

import inspect
from collections import OrderedDict



def get_method_parameters(fn:Callable, to_list:bool=False)->Union[OrderedDict, List]:
    """
    fn의 parameter들을 odict_keys 또는 list로 출력

    Args:
        fn (callable): 대상 method
        to_list (bool, optional): list로 출력할지 여부. Defaults to False.

    Returns:
        _type_: _description_
    """
    # method의 signature
    sig = inspect.signature(fn)
    # method의 parameter 이름 목록 추출
    params = sig.parameters.keys()
    if to_list:
        return list(params)
    else:
        return params