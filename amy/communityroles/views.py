from django.contrib.auth.mixins import PermissionRequiredMixin

from workshops.base_views import (
    AMYCreateView,
    AMYDeleteView,
    AMYDetailView,
    AMYUpdateView,
    RedirectSupportMixin,
)
from workshops.util import OnlyForAdminsMixin

from .forms import CommunityRoleForm
from .models import CommunityRole

# ------------------------------------------------------------
# CommunityRole related views


class CommunityRoleDetails(OnlyForAdminsMixin, AMYDetailView):
    queryset = CommunityRole.objects.all()
    context_object_name = "role"
    template_name = "communityroles/communityrole.html"

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context["title"] = str(self.object)
        return context


class CommunityRoleCreate(
    OnlyForAdminsMixin, PermissionRequiredMixin, RedirectSupportMixin, AMYCreateView
):
    permission_required = "communityroles.add_communityrole"
    model = CommunityRole
    form_class = CommunityRoleForm

    def get_form_kwargs(self) -> dict:
        kwargs = super().get_form_kwargs()
        kwargs.update({"prefix": "communityrole"})
        return kwargs


class CommunityRoleUpdate(OnlyForAdminsMixin, PermissionRequiredMixin, AMYUpdateView):
    permission_required = "communityroles.change_communityrole"
    model = CommunityRole
    form_class = CommunityRoleForm

    def get_form_kwargs(self) -> dict:
        kwargs = super().get_form_kwargs()
        kwargs.update({"prefix": "communityrole"})
        return kwargs


class CommunityRoleDelete(OnlyForAdminsMixin, AMYDeleteView):
    permission_required = "communityroles.delete_communityrole"
    model = CommunityRole

    def get_success_url(self) -> str:
        # Currently can only be called via redirect.
        # There is no direct view for all Community Roles.
        return self.request.GET.get("next", "")
