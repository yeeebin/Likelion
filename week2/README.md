# 개인 블로그 모델링, models.py 작성
![스크린샷 2023-05-16 000644](https://github.com/yeeebin/Likelion/assets/129045979/40c17adb-9039-4eec-ab66-7cd8e0ae7ee1)

# <코드리뷰>
1. Favorite, Like 모델에 'data' 필드를 추가하면 클릭 시간 알 수 있으니 좋을 것!
2. Like 모델에 self.blog.title 에서 blog => post로 수정할 것 
3. post가 여러 category에 속하려면 ManyToManyField 사용할것 추천1
4. Category모델 안의 post필드에서 ForeignKey 필드에서는 max_length 옵션을 사용할 수 없ㅇ, 아마 max_length는 CharField나 TextField에서만 사용 가능. 
