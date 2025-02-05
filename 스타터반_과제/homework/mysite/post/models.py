from django.db import models

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    

# 2. post 앱의 models.py에 Tag 모델을 추가하고 Post 모델과 다대다 관계로 연결하세요.

from django.db import models  # Django의 ORM을 사용하기 위해 models 모듈을 가져옴
from django.contrib.auth.models import User  # 기본 Django 제공 User 모델인데 별도로 만들어도 문제 없음

# 블로그 게시글 저장 모델
class Post(models.Model):
    title = models.CharField(max_length=255)  # 제목 (최대 길이 255자)
    content = models.TextField()  # 게시글 본문 저장
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    # User 모델과 1:N 관계 (ForeignKey) => 유저 한명이서 여러개의 Post를 만들 수 있음
    # on_delete=models.CASCADE => User가 삭제되면 관련된 Post도 삭제됨
    # related_name="posts" => user.posts로 해당 유저의 모든 게시글 조회 가능
    created_at = models.DateTimeField(auto_now_add=True)
    # 생성된 시간 자동 저장 (최초 생성 시 한 번만 설정됨)
    tags = models.ManyToManyField('Tag', related_name="posts")
    # 다대다(M:N) 관계 (ManyToManyField)
    # 하나의 게시글에 여러 개의 태그를 가질 수 있고 하나의 태그가 여러 게시글에 사용될 수 있음
    # related_name="posts" => tag.posts로 해당 태그가 포함된 모든 게시글 조회 가능

    def __str__(self):
        return self.title  # 객체 print()할 때 게시글 제목으로 반환

# 태그 저장 모델
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    # 태그 (최대 길이 50자, 중복 불가)

    def __str__(self):
        return self.name  # 객체 print()할 때 태그 이름으로 반환
    
    from django.db import models  # Django의 ORM을 사용하기 위해 models 모듈을 가져옴
from django.contrib.auth.models import User  # 기본 Django 제공 User 모델인데 별도로 만들어도 문제 없음

# 블로그 게시글 저장 모델
class Post(models.Model):
    title = models.CharField(max_length=255)  # 제목 (최대 길이 255자)
    content = models.TextField()  # 게시글 본문 저장
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    # User 모델과 1:N 관계 (ForeignKey) => 유저 한명이서 여러개의 Post를 만들 수 있음
    # on_delete=models.CASCADE => User가 삭제되면 관련된 Post도 삭제됨
    # related_name="posts" => user.posts로 해당 유저의 모든 게시글 조회 가능
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # 생성된 시간 자동 저장 (최초 생성 시 한 번만 설정됨)

    def __str__(self):
        return self.name # 객체 print()할 때 게시글 제목으로 반환
    
    # 3. user 앱의 models.py에 Profile 모델(user, bio 필드)을 추가하고 User 모델과 일대일 관계로 연결하세요.

from django.db import models  # Django ORM을 사용하기 위한 models 모듈
from django.contrib.auth.models import User  # Django 기본 제공 User 모델

# 프로필 정보 모델
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    # User 모델과 1:1 관계 (OneToOneField)
    # on_delete=models.CASCADE => User가 삭제되면 해당 Profile도 함께 삭제됨
    # related_name="profile" => user.profile로 프로필 정보에 접근 가능

    bio = models.TextField(blank=True, null=True) # 자기소개 필드 (기획 상 무조건 쓰지 않는다면 비어있어도 무방)

    def __str__(self):
        return self.user.username  # 객체 print()할 때 사용자 이름으로 반환