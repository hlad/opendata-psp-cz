from django.conf.urls.defaults import patterns, url
from djangorestframework.views import ListOrCreateModelView, InstanceModelView
from api.resources import OsobaResource
from api.resources import TypOrganuResource
from api.resources import TypFunkceResource
from api.resources import OrganResource
from api.resources import FunkceResource
from api.resources import ZarazeniOrganResource
from api.resources import ZarazeniFunkceResource

urlpatterns = patterns('',
    url(r'^$', ListOrCreateModelView.as_view(resource=OsobaResource), name='osoby-root'),
    url(r'^osoba/$', ListOrCreateModelView.as_view(resource=OsobaResource), name='osoby'),
    url(r'^osoba/(?P<id>[^/]+)/$', InstanceModelView.as_view(resource=OsobaResource), name='osoba'),
    url(r'^typ_organu/$', ListOrCreateModelView.as_view(resource=TypOrganuResource), name='typy_organu'),
    url(r'^typ_organu/(?P<id>[^/]+)/$', InstanceModelView.as_view(resource=TypOrganuResource), name='typ_organu'),
    url(r'^typ_funkce/$', ListOrCreateModelView.as_view(resource=TypFunkceResource), name='typy_funkci'),
    url(r'^typ_funkce/(?P<id>[^/]+)/$', InstanceModelView.as_view(resource=TypFunkceResource), name='typ_funkce'),
    url(r'^organ/$', ListOrCreateModelView.as_view(resource=OrganResource), name='organy'),
    url(r'^organ/(?P<id>[^/]+)/$', InstanceModelView.as_view(resource=OrganResource), name='organ'),
    url(r'^funkce/$', ListOrCreateModelView.as_view(resource=FunkceResource), name='funkce-list'),
    url(r'^funkce/(?P<id>[^/]+)/$', InstanceModelView.as_view(resource=FunkceResource), name='funkce'),
    url(r'^zarazeni_organ/$', ListOrCreateModelView.as_view(resource=ZarazeniOrganResource), name='zarazeni_organu'),
    url(r'^zarazeni_organ/(?P<id>[^/]+)/$', InstanceModelView.as_view(resource=ZarazeniOrganResource), name='zarazeni_organ'),
    url(r'^zarazeni_funkce/$', ListOrCreateModelView.as_view(resource=ZarazeniFunkceResource), name='zarazeni_funkci'),
    url(r'^zarazeni_funkce/(?P<id>[^/]+)/$', InstanceModelView.as_view(resource=ZarazeniFunkceResource), name='zarazeni_funkce'),
)