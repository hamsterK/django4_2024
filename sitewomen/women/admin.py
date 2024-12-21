from django.contrib import admin, messages
from django.utils.safestring import mark_safe

from .models import Women, Category
from django.contrib.admin.actions import delete_selected


class MarriedFilter(admin.SimpleListFilter):
    title = "Woman's status"
    parameter_name = 'status'

    def lookups(self, request, model_admin):
        return [
            ('married', 'Married'),
            ('single', 'Not married'),
        ]

    def queryset(self, request, queryset):
        if self.value() == 'married':
            return queryset.filter(husband__isnull=False)
        elif self.value() == 'single':
            return queryset.filter(husband__isnull=True)


@admin.register(Women)
class WomenAdmin(admin.ModelAdmin):
    fields = ['title', 'slug', 'content', 'photo', 'post_photo', 'cat', 'husband', 'tags']  # fields for edit page
    # exclude = ['tags', 'is_published']  # fields hidden on edit page
    readonly_fields = ['post_photo']
    prepopulated_fields = {"slug": ("title", )}  # doesn't edit existing slug
    # filter_horizontal = ['tags']
    filter_vertical = ['tags']
    list_display = ('title', 'post_photo', 'time_create', 'is_published', 'cat')
    list_display_links = ('title', )
    ordering = ['-time_create', 'title']
    list_editable = ('is_published', )
    list_per_page = 5
    actions = ['set_published', 'set_draft']
    search_fields = ['title__startswith', 'cat__name']
    list_filter = [MarriedFilter, 'cat__name', 'is_published']
    save_on_top = True

    @admin.display(description="Photo", ordering='content')
    def post_photo(self, women: Women):
        if women.photo:
            return mark_safe(f"<img src='{women.photo.url}', width=50>")
        return 'No photo added'

    @admin.action(description='Publish selected articles')
    def set_published(self, request, queryset):
        count = queryset.update(is_published=Women.Status.PUBLISHED)
        self.message_user(request, f"{count} record(s) updated")

    @admin.action(description='Move selected articles to drafts')
    def set_draft(self, request, queryset):
        count = queryset.update(is_published=Women.Status.DRAFT)
        self.message_user(request, f"{count} record(s) moved to drafts", messages.WARNING)

    delete_selected.short_description = 'Delete selected items'  # rename default delete action


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
