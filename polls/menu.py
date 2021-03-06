
from cms.menu_bases import CMSAttachMenu
from menus.base import Menu, NavigationNode
from menus.menu_pool import menu_pool
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from polls.models import Poll


class PollsMenu(CMSAttachMenu):
    name = _("Polls Menu")      # give the menu a name, this is required.

    def get_nodes(self, request):
        """
        This method is used to build the menu tree
        Arguments:
        - `self`:
        - `request`:
        """
        nodes = []
        for poll in Poll.objects.all():
            # the menu tree consists of NavigationNode instances
            # Each NavigationNode take a label as its first argument, a URL as
            # its second argument and a (for this tree) unique id as its third
            # argument
            node = NavigationNode(
                poll.question,
                reverse('polls.views.detail', args=(poll.pk,)),
                poll.pk
            )
            nodes.append(node)
        return nodes

menu_pool.register_menu(PollsMenu) # register the menu
