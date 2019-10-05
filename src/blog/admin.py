from django.contrib import admin
from blog.models import Post, Comment, Reaction


class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'comment_text', 'user')
admin.site.register(Comment, CommentAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display = ('post_title', 'user', 'updated', 'publish_status')
admin.site.register(Post, PostAdmin)

class ReactionAdmin(admin.ModelAdmin):
    list_display = ('post', 'user', 'react')
admin.site.register(Reaction, ReactionAdmin)