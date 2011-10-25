from django.template import Context
import settings

def custom_context(request):
    context_options = {}

    if request.user.is_authenticated():
        profile = request.user.profile
        timezone = profile.timezone
        context_options['timezone'] = timezone
    else:
        context_options['timezone'] = 'US/Eastern'

    context_options['SHAREJS_SERVER']  = settings.SHAREJS_SERVER
    context_options['SITE_ENV']  = settings.SITE_ENV

    c = Context(context_options)
    return c
