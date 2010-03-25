from django.conf import settings

from rip.core import Controller, DEFAULT_FACTORIES

RIP_FACTORIES = getattr(settings, 'RIP_FACTORIES', DEFAULT_FACTORIES)

RIP_SETTINGS = getattr(settings, 'RIP_SETTINGS', {})

formatter = Controller(RIP_FACTORIES, **RIP_SETTINGS)

render = formatter.render
