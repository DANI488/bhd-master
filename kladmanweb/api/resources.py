from tastypie.resources import ModelResource
from kladmanweb.models import KladMan, GeoTag
from tastypie import fields


class KladManResource(ModelResource):
    class Meta:
        queryset = KladMan.objects.all()
        resource_name = 'kladman'


class GeoTagResource(ModelResource):
    kladman = fields.ForeignKey(KladManResource, 'kladman', blank=True, null=True)

    class Meta:
        queryset = GeoTag.objects.all()
        resource_name = 'geotag'
