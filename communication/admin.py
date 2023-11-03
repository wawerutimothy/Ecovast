from django.contrib import admin
from .models import Conversation, ConversationsMessage
# Register your models here.

admin.site.register(Conversation)
admin.site.register(ConversationsMessage)
