from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import GolfRound
from django.urls import reverse_lazy


class RoundListView(ListView):
    model = GolfRound
    template_name = 'golf_round_post/home.html'
    context_object_name = 'rounds'
    ordering = ['-date_posted']
    paginate_by = 5


class UserRoundListView(ListView):
    model = GolfRound
    template_name = 'golf_round_post/user_rounds.html'
    context_object_name = 'rounds'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return GolfRound.objects.filter(golfer=user).order_by('-date_posted')


class RoundDetailView(DetailView):
    model = GolfRound


# This mixin in forces a user to be logged in prior to creating
class RoundCreateView(LoginRequiredMixin, CreateView):
    # This will eventually allow for all necessary input in order to calculate strokes gained
    model = GolfRound
    fields = ['course', 'score']

    def form_valid(self, form):
        form.instance.golfer = self.request.user
        return super().form_valid(form)
    

# This mixin in forces a user to be logged in prior to updating, and forces user to be same as the one who created
class RoundUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    # This will eventually allow for all necessary input in order to calculate strokes gained
    model = GolfRound
    fields = ['course', 'score']

    def form_valid(self, form):
        form.instance.golfer = self.request.user
        return super().form_valid(form)
    

    def test_func(self):
        round = self.get_object()
        return True if self.request.user == round.golfer else False
    

class RoundDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = GolfRound
    success_url = reverse_lazy("golf-round-home")

    def test_func(self):
        round = self.get_object()
        return True if self.request.user == round.golfer else False


def about(request):
    return render(request, "golf_round_post/about.html", {"title": "About"})
