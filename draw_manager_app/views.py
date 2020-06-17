from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import DetailView

from .forms import InquiryForm, DrawCreateForm
from django.contrib import messages
import logging
from .models import Draw

logger = logging.getLogger(__name__)


# Create your views here.
class Top_pageView(generic.TemplateView):
    template_name = 'top_page.html'


class InquiryView(generic.FormView):
    template_name = "inquiry.html"
    form_class = InquiryForm
    success_url = reverse_lazy('draw:inquiry')

    def form_valid(self, form):
        form.send_email()
        messages.success(self.request, 'メッセージを送信しました。')
        logger.info('Inquiry sent by {}'.format(form.cleaned_data['name']))
        return super().form_valid(form)





class DrawListView(LoginRequiredMixin, generic.ListView):
    model = Draw
    template_name = 'draw_list.html'
    pagenate_by = 5

    def get_queryset(self):

        #検索
        q_word = self.request.GET.get('query')

        if q_word:
            drawlist = Draw.objects.filter(
                Q(draw_number__icontains=q_word,user=self.request.user)).order_by('-created_at')
        else:
            drawlist = Draw.objects.filter(user=self.request.user).order_by('-created_at')
        return drawlist




class DrawDetailView(LoginRequiredMixin, generic.DetailView):
    model = Draw
    template_name = 'draw_detail.html'


class DrawCreateView(LoginRequiredMixin, generic.CreateView):
    model = Draw
    template_name = 'draw_create.html'
    form_class = DrawCreateForm
    success_url = reverse_lazy('draw:draw_list')

    def form_valid(self, form):
        draw = form.save(commit=False)
        draw.user = self.request.user
        draw.save()
        messages.success(self.request, '図面を登録しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, '図面の登録に失敗しました。')
        return super().form_invalid(form)


class DrawUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Draw
    template_name = 'draw_update.html'
    form_class = DrawCreateForm

    def get_success_url(self):
        return reverse_lazy('draw:draw_detail', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        messages.success(self.request, '図面情報を更新しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, '図面情報の更新に失敗しました。')
        return super().form_invalid(form)


class DrawDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Draw
    template_name = 'draw_delete.html'
    success_url = reverse_lazy('draw:draw_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, '図面情報を削除しました。')
        return super().delete(request, *args, **kwargs)
