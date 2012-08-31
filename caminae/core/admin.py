from django.contrib import admin

from caminae.core.models import Datasource, Stake, Usage, Network, Trail


admin.site.register(Datasource)
admin.site.register(Stake)
admin.site.register(Usage)
admin.site.register(Network)
admin.site.register(Trail)