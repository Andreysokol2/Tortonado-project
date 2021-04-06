from django.urls  import path
from . import views

urlpatterns =  [
    path( 'sweets' ,  views.sweets,  name= 'sweets'),
    path( 'mousse' ,  views.mousse,  name= 'mousse'),
    path( 'sponge' ,  views.sponge,  name= 'sponge'),
    path('product/<product_id>/',  views.product,  name= 'product'),
]