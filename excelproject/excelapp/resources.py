from import_export import resources
from .models import Person

class PersonResources(resources.ModelResource):
    class meta:
        model = Person