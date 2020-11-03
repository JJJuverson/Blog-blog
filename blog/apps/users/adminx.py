import xadmin
from xadmin import views



class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = "我的个人博客后台系统"
    site_footer = "1178562887@qq.com"
    # menu_style = "accordion"






xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)