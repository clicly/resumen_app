from django.urls import path
from django.conf.urls import include
from . import views
from rest_framework import routers

from .models import UserProfile
from .views import SkillViewSet, UserProfileViewSet, ContactProfileViewSet, TestimonialViewSet, MediaViewSet, \
    PortfolioViewSet, BlogViewSet, RatingViewSet, CertificateViewSet

router = routers.DefaultRouter()
router.register('skills', SkillViewSet)
router.register('userprofiles', UserProfileViewSet)
router.register('contactprofiles', ContactProfileViewSet)
router.register('testimonials', TestimonialViewSet)
router.register('medias', MediaViewSet)
router.register('portfolios', PortfolioViewSet)
router.register('blogs', BlogViewSet)
router.register('ratings', RatingViewSet)
router.register('certificates', CertificateViewSet)

app_name = 'main'

urlpatterns = [
    path('', views.IndexView.as_view(), name="home"),
    path('contact/', views.ContactView.as_view(), name="contact"),
    path('portfolio/', views.PortfolioView.as_view(), name="portfolios"),
    path('portfolio/<slug:slug>', views.PortfolioDetailView.as_view(), name="portfolio"),
    path('blog/', views.BlogView.as_view(), name="blogs"),
    path('blog/<slug:slug>', views.BlogDetailView.as_view(), name="blog"),
    path('api/', include(router.urls))
]
