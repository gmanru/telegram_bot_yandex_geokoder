from django.contrib import admin

#from .forms import ProfileForm
#from .models import Message
from .models import Profile, Filter, Result


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    def display_results(self, obj: Profile):
        result = obj.result.all()
        return " | ".join((r.result for r in result))

    list_display = ('user_id', 'display_results',)
    #form = ProfileForm

@admin.register(Filter)
class FilterAdmin(admin.ModelAdmin):
    list_display = ('text',)
'''@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'profile', 'text', 'created_at')'''

@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ('id','uid','request', 'result', 'created_at',)