# Python-hwpxlib

[hwpxlib 바로가기](https://github.com/neolord0/hwpxlib)

hwpxlib 패키지 python에서 쉽게 사용할 수 있게 만든 github repo 입니다.

- .hwpx 파일의 text를 추출할때 가장 좋은 성능을 보였던 java 패키지인 hwpxlib를 컴파일 해서 사용하는 방식으로 구성했습니다.

&nbsp;

### 필수 설치

- 해당 방법은 Java가 사용하시는 OS에 설치되야 합니다.
    - Maven Compile을 통해서 hwplib github를 .jar로 컴파일을 수행합니다.
        - Maven 컴파일이 어려울 경우에는 [mvnrepository](https://mvnrepository.com/artifact/kr.dogfoot/hwplib/1.1.7) 에 올려져 있는 것을
          다운받으셔도 됩니다.

- 기본적으로 python JPype package를 이용한 방법이며, hwpxlib의 다양한 기능중에 한글 추출기능만을 사용합니다.

&nbsp;

### 사용 방법

### Docker

[Docker Desktop](https://www.docker.com/products/docker-desktop)을 설치 후 실행해 주세요.

이후 프로젝트 루트 폴더에서 터미널을 실행 후 다음 명령어를 입력해 주세요.

```bash

docker build -t test:test.

docker run -p 7860:7860 test:test

```
hwpx 텍스트 변환 서버가 7860번 포트에 실행됩니다.
위 명령어에서 test:test는 <이미지 이름>:<태그 이름> 을 의미합니다. 필요에 따라 바꾸시길 바랍니다.

코드를 바꾸지 않고 서버를 재실행하고 싶을 때는 2번째 줄만 다시 실행하시면 됩니다.
코드를 바꿀 경우에는 build부터 다시 하셔야 합니다. 생성된 이미지과 실행된 컨테이너 목록은 Docker Desktop 앱에서 확인하고 삭제할 수 있습니다.

이후 testing.ipynb 파일을 Jupyter notebook을 사용해서 실행하시기 바랍니다. 만약 Jupyter Notebook이 설치되어 있지 않다면 `pip install jupyter`를 터미널에 입력해
설치해 주세요.
