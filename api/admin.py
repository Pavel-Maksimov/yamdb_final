from django.contrib import admin

from api.models.user import YaUser
from .models.category import Category
from .models.comment import Comment
from .models.genre import Genre
from .models.review import Review
from .models.title import Title
from api.authentication.forms import YaUserChangeForm, YaUserCreationForm

admin.site.site_header = 'YaMDb API'


@admin.register(YaUser)
class YaUserAdmin(admin.ModelAdmin):
    add_form = YaUserCreationForm
    form = YaUserChangeForm
    list_display = ('username', 'email', 'role',)
    search_fields = ('email',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("pk", "name", "slug",)
    search_fields = ("name", "slug",)
    empty_value_display = "-пусто-"


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("pk", "review", "text", "author", "pub_date",)
    search_fields = ("pk", "review",)
    list_filter = ("pub_date",)
    empty_value_display = "-пусто-"


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("name", "slug",)
    search_fields = ("name", "slug",)
    empty_value_display = "-пусто-"


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("pk", "title", "text", "author", "pub_date", "score",)
    search_fields = ("title", "text", "author",)
    list_filter = ("score",)
    empty_value_display = "-пусто-"


@admin.register(Title)
class TitleAdmin(admin.ModelAdmin):
    list_display = ("name", "year", "description", "category",)
    search_fields = ("name", "year", "description", "category",)
    list_filter = ("year", "category",)
    empty_value_display = "-пусто-"
