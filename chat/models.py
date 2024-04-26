from django.conf import settings
from django.db import models
from django.utils import timezone

class ChatSession(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # 세션 생성 시간, 자동으로 현재 시간이 저장됩니다.
    created_at = models.DateTimeField(auto_now_add=True)

class Message(models.Model):
    # 이 메시지가 속한 채팅 세션
    session = models.ForeignKey(ChatSession, related_name='messages', on_delete=models.CASCADE)
    # 메시지를 보낸 사용자
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='sent_messages', on_delete=models.CASCADE)
    # 메시지 본문
    text = models.TextField()
    # 메시지 생성 시간, 기본값으로 현재 시간이 설정됩니다.
    created_at = models.DateTimeField(default=timezone.now)
    # 메시지가 중요 표시되었는지 여부, 데이터베이스에서 효율적으로 검색 가능하게 인덱스를 추가합니다.
    important = models.BooleanField(default=False, db_index=True)
    # 메시지 읽음 상태, 기본적으로 '읽지 않음'(False) 상태입니다.
    read = models.BooleanField(default=False)
    # 메시지 삭제 시간, null 허용. 실제 데이터는 삭제되지 않고, 이 필드에 삭제 시간이 기록되어 '소프트 삭제'를 구현합니다.
    deleted_at = models.DateTimeField(null=True, blank=True)

    def soft_delete(self):
        # 메시지를 소프트 삭제하는 함수입니다. 삭제 시간을 현재 시간으로 설정하고 저장합니다.
        self.deleted_at = timezone.now()
        self.save()
