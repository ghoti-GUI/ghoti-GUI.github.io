from django.urls import path, include, re_path
from django.views.static import serve
# from pos.settings import MEDIA_ROOT
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
# from .views import TestViewSet, TestImgViewSet, ProductViewSet, CategoryViewSet
from .views import viewsProduct, viewsCategory, viewsPrinter, viewsTVA, viewsCommon, viewsUser, viewsTest


router = DefaultRouter()
router.register(r'TestModel', viewsTest.TestViewSet)
router.register(r'testimg/viewsets', viewsTest.TestImgViewSet)
router.register(r'post/product', viewsProduct.ProductViewSet)
router.register(r'post/category', viewsCategory.CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),

    # path('get/product/next_id_user/', viewsProduct.get_next_product_id, name='get_next_product_id'), 
    path('product/check_id_Xu_existence/', viewsProduct.check_id_Xu_existence, name = 'check_id_Xu_existence'), 
    path('get/product/all/', viewsProduct.get_all_products, name = 'get_all_products'), 
    path('get/product/all/frontform/', viewsProduct.get_all_products_front_form, name = 'get_all_products_front_form'), 
    path('update/product_by_id/', viewsProduct.update_product_by_id, name='update_product_by_id'), 
    path('get/product/by/id_Xu/', viewsProduct.get_product_by_id_Xu, name='get_product_by_id_Xu'), 
    path('delete/product/', viewsProduct.delete_product, name='delete_product'), 
    

    path('get/category/all/', viewsCategory.get_all_categories, name='get_all_categories'), 
    path('category/check_name_category_existence/', viewsCategory.check_name_category_existence, name = 'check_name_category_existence'), 
    path('get/cid/by/categoryName/', viewsCategory.get_cid_by_categoryName, name='get_cid_by_categoryName'), 

    path('get/printers/', viewsPrinter.get_printer, name = 'get_printer'), 
    path('get/printers/by_id/', viewsPrinter.get_printers_by_id, name='get_printers_by_id'), 

    path('get/tva/', viewsTVA.get_TVA, name = 'get_TVA'),  
    path('get/tva/by_id/', viewsTVA.get_TVA_by_id, name = 'get_TVA_by_id'), 

    path('delete/all/', viewsCommon.delete_all, name='delete_all'), 
    path('update/Xu_class/', viewsCommon.update_Xu_class, name='update_Xu_class'), 

    path('testimg/APIView/', viewsTest.TestImgView.as_view(), name = 'test_img'), 
    path('testimg/get_all_TestImg/', viewsTest.get_all_TestImg, name='get_all_TestImg'), 

]
