
from menus.base import Menu, NavigationNode
from menus.menu_pool import menu_pool
from django.utils.translation import ugettext_lazy as _
from cms.menu_bases import CMSAttachMenu

class TestMenu(Menu): 

    def get_nodes(self, request):
        """
        
        Arguments:
        - `self`:
        - `request`:
        """
        nodes = []
        n = NavigationNode(_('sample root page'), '/', 1)
        n2 = NavigationNode(_('sample settings page'), '/bye/', 2)
        n3 = NavigationNode(_('sample account page'), '/hello/', 3)
        # args: title, url, id, parent_id
        n4 = NavigationNode(_('sample my profile page'), '/hello/world/', 4, 3)
        nodes.append(n)
        nodes.append(n2)
        nodes.append(n3)
        nodes.append(n4)
        return nodes

menu_pool.register_menu(TestMenu)
        

# ----------
class TestAttachMenu(CMSAttachMenu):
    name = _('test menu')

    def get_nodes(self, request):
        """
        
        Arguments:
        - `self`:
        - `request`:
        """
        nodes = []
        n = NavigationNode(_('sample root page'), '/', 1)
        n2 = NavigationNode(_('sample settings page'), '/bye/', 2)
        n3 = NavigationNode(_('sample account page'), '/hello/', 3)
        # args: title, url, id, parent_id
        n4 = NavigationNode(_('sample my profile page'), '/hello/world/', 4, 3)
        nodes.append(n)
        nodes.append(n2)
        nodes.append(n3)
        nodes.append(n4)
        return nodes

menu_pool.register_menu(TestAttachMenu)
