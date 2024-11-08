import time
from collections import deque


class ProgressBar:
    def __init__(self, header, bar_size, delta_format="{:.3f}", log_save:bool=False):
        self.header = header
        self.bar_size = bar_size
        self.delta_format = delta_format
        self.log_save = log_save

        self.delta_deque = deque(maxlen=2)      # 순간 변화 
        self.eta_deque = deque(maxlen=20)       # 평균 변화
        self.start_time = time.time()           # instance 생성 시 시간

        # callable 시 고정 변수
        self.iter_size = None                   # iteration의 크기
        self.int_size = None                    # [  1 / 1000] 의 정수 크기

        # 동적 변수
        self.current_iter = None                # 현재 iter


    def __call__(self, iter):
        self._callable_initial_variable(iter)


    def _callable_initial_variable(self, iter):
        self.iter_size = len(iter)
        self.int_size = len(set(self.iter_size)) + 1







