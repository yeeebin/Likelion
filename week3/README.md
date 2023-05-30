# 코드리뷰
## render과 redirectd의 차이점
 render은 템플릿을 불러온다. 즉, 동일한 url에 html을 띄워줌.
 redirect는 URL로 이동한다
## redirect()에서 reverse()를 사용하지 않아도 되는데, 무슨 차이가 있을까? 
 redirect 함수에는 reverse 함수를 사용하여 URL을 생성하는 것이 일반적인 방법이다. URL의 변경이나 수정이 발생할 경우 코드를 직접 수정하지 않고 URL 패턴 이름만 수정하면 된다. 따라서 reverse 함수를 사용하여 URL을 동적으로 생성하는 것은 좋은 방법입니다. 
 redirect 함수에는 URL 문자열을 직접 전달하는 것도 가능하다. 예를 들어 redirect('/some-url/')과 같이 문자열을 사용하여 리다이렉트할 URL을 지정할 수 있다. 이 경우 URL이 변경되는 경우에는 코드를 수정해야 하므로 유지보수 측면에서는 좋은 방법이 아니다.
