# GGUtils
이미지 처리, 머신러닝 등 Python을 이용하는 대부분의 프로세스에서 사용할 수 있는 프로세싱 유틸리티 코드들을 모아놓은 라이브러리입니다. Python을 이용한 개발 과정 중 반복성이 높은 코드들에 대하여, 디버깅 성능 최적화 등을 중점으로 개발되었습니다.
* 현재 개발 진행 중인 코드로, 내부 코드들과 라이브러리 구조는 언제든지 수정될 수 있습니다.

</br>
</br>
</br>

* 해당 라이브러리는 다음과 같은 패키지들로 구성되어 있습니다.

## A. img
기본적인 이미지 처리와 Jupyter notebook(.ipynb) 에서 이미지를 보다 편하게 볼 수 있는 method들의 모음입니다.
### 1. img
* 이미지 파일을 읽어오거나, 이미지로부터 주요 정보들을 추출하는 알고리즘들, 이미지로 구성된 디렉터리 내 이미지를 편하게 가져오는 class 등으로 구성되어 있습니다.
* 해당 코드에는 다음과 같은 method 들로 구성되어 있습니다.
> * get_rgb_img(): cv2를 이용해 BGR 이미지를 RGB로 가져옴.
> * get_img_axis_size(): 이미지의 무결성을 확인하고, 흑백, RGB, RGBA 등의 이미지로부터 x, y축의 길이를 반환한다.
> * check_rgb_or_rgba(): 입력된 배열이 BGR, RGB, RGBA와 같은 일반적인 2D 이미지인지 확인한다.
> * size_tuple_type_error(): 입력 값이 일반적인 이미지의 형태인 (x, y) 로 구성되어 있는지 확인한다.
> * img_corners(): 입력 이미지의 x, y축을 기준으로 4개 꼭지점을 numpy 배열로 출력한다.
> * img_center(): 입력 이미지(또는 x, y) 축에 대하여 중심 좌표를 Tuple로 출력한다.
> * RGBTuple: 이 클래스는 RGB 픽셀에 대하여 무결성 또는 특정 색깔에 해당하는 픽셀을 출력하기 위해 설계되었습니다.
>> * get(): 입력된 색깔 문자열에 해당하는 RGB 튜플을 출력합니다.
>> * check(): 입력된 값이 RGB 픽셀 튜플에 해당하는지 확인합니다.
>> * random(): 임의의 RGB 픽셀 튜플을 출력합니다.
> * GetInDirectory: 이 클래스는 이미지로 구성된 디렉터리에서 이미지 파일들을 효율적으로 출력하기 위해 설계되었습니다.
>> * Callable: 주요 기능으로, 입력된 index에 해당하는 이미지를 read_fn의 방법으로 출력합니다.
>> * slide_viewer(): 모든 이미지들을 Slider로 보기 쉽게 출력한다.

</br>

### 2. viewer
* 이미지를 출력하는 코드들의 모음입니다 - .ipynb 환경을 상정하고 만들어져 있습니다.
* 해당 코드에는 다음과 같은 method 들로 구성되어 있습니다.
> * show_img(): matplotlib.pyplot 환경으로 이미지 출력
> * Slider: 이 클래스는 대량의 이미지를 slider로 보기 쉽게 출력하기 위해 설계되었습니다.
>> * run(): 생성된 Slider 인스턴스에 대하여 위젯을 출력하는 메서드.

</br>
</br>
</br>

## B. utils
python 프로세스 개발 중 사용 빈도가 높은 method들의 모음.
### 1. utils
* 자주 사용되는 기타 util method들의 모음
* 해당 코드에는 다음과 같은 method 들로 구성되어 있습니다.
> * make_numpy_arange(): np.arange()와 동일한 기능을 하는 method로 start와 end가 동일한 경우, 이를 보정하여 np.arange가 생성될 수 있게 함.
> * list_flatten(): list 안에 list가 들어 있는 형태의 list에 대하여, 한 개의 list로 변환.
> * time_checker(): start부터 해당 method가 실행될 때까지 걸린 시간 출력.
> * decimal_seconds_to_time_string(): 소수 초 단위 시간을 읽기 쉬운 문자열로 변환.

</br>

### 2. path
* 경로 또는 파일에 관련된 method들의 모음
* 해당 코드에는 다음과 같은 method 들로 구성되어 있습니다.
> * do_or_load(): fn의 결과를 pickle로 저장할 수 있는 경우, savepath가 존재하지 않는다면 fn을 실행하고, 그렇지 않다면 savepath에서 pickle을 불러옴.
> * new_dir_maker(): dir_path가 존재하지 않거나, makes_new=True인 경우, 해당 경로에 새로운 디렉터리를 생성한다.
> * make_null_list_pickle(): 비어 있는 list가 포함된 pickle을 생성한다.
> * save_pickle(): data를 pickle로 저장.
> * load_pickle(): pickle로부터 data를 불러온다.
> * write_json(): data를 json_path로 저장.
> * read_json(): json_path로부터 data를 불러온다.
> * read_txt_file(): txt파일의 내용을 읽어서 문자열로 불러온다.
> * write_txt_file(): 문자열을 txt파일로 저장한다.
> * get_file_name(): 파일의 경로에서 확장자를 제외한(선택 가능) 파일 이름을 가져온다.
> * check_file_path_use_only_txt(): 문자열만을 기준으로 해당 문자열이 file인지 여부를 확인.
> * file_download(): url로부터 대상 file을 다운로드 한다.
> * GetAbsolutePath: 이 클래스는 Collabla 메서드에서 입력한 parents_path의 하위 파일들의 모든 절대 경로를 출력하기 위해 설계되었습니다.
>> * 해당 클래스는 특정 확장자에 해당하는 파일만 대상으로 하는 것이 가능합니다.
>> * Callable: 주요 기능으로, parents_path의 하위 파일들의 모든 절대 경로들을 가지고 옵니다 - instance에 특정 extension만 대상으로 하는 것으로 설정되었다면, 그 extension에 해당하는 파일만 대상으로 합니다.
>> * get_all_path(): parents_path의 하위 파일들의 모든 절대 경로들을 list로 가지고 옵니다.

</br>

### 3. module
* python module에 관련된 method들의 모음
* 해당 코드에는 다음과 같은 method 들로 구성되어 있습니다.
> * get_module_from_py(): python 파일을 module로 로드함 - unique_module=False인 경우, 해당 py파일의 이름으로 module명 설정
> * explore_modules_recursiverly(): python 파일의 의존성 모듈들을 재귀적으로 탐색
> * get_module_list_in_py_file(): python 파일의 의존성 모듈들을 출력
> * get_module_path(): py_path를 기반으로 module 파일들의 경로 생성
> * GithubHelper: 이 클래스는 깃허브에 있는 특정 repository 내 특정 디렉터리(package)만 다운로드 하는 것을 목적으로 설계되었습니다.
>> * download_repo_directory(): 깃허브 레포지토리 내 특정 디렉터리 다운로드(download_contents() 메서드를 보다 쉽게 사용하는 것을 목적으로 개발)
>> * download_contents(): 깃허브 레포지토리 내 특정 tree 구조에 대하여 재귀적으로(내부 디렉터리 존재 시) 다운로드
>> * download_file(): 깃허브 레포지토리 내 특정 contents를 다운로드 합니다.
>> * get_repo_from_url(): 깃허브 url을 대상으로 repository의 문자열을 출력합니다.
>> * get_directory_tree(): 깃허브 repository의 특정 디렉터리의 url을 기반으로 tree에(디렉터리 단계) 대한 문자열을 출력합니다.

</br>
</br>
</br>

## C. 외부 라이브러리 의존성
* 해당 코드는 현재 개발중인 단계로 CI/CD 를 위한 외부 라이브러리 의존성 버전 확인이 진행되지 않은 상태입니다.
* 현재 작성되어 있는 각 라이브러리의 버전은 개발 환경의 버전입니다.
> * opencv-python == 4.10.0
> * numpy == 1.26.4
> * pandas == 2.2.2
> * matplotlib == 3.9.1
> * ipywidgets == 8.1.3
> * PyGithub == 2.4.0
