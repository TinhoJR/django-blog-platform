from django.views.generic import CreateView
from . models import Comment,Post
from . forms import CommentForm
from django.urls import reverse_lazy,reverse
from django.http import JsonResponse,Http404
from django.shortcuts import get_object_or_404,redirect
from django.contrib.auth.mixins import LoginRequiredMixin


class CommentView(LoginRequiredMixin,CreateView):
    model = Comment
    # template_name = "comment.html"
    form_class = CommentForm
    

    def get_success_url(self):
        post_pk = self.kwargs.get("post_pk")
        return reverse("post_detail",args=[post_pk])


    def form_valid(self,form):
        comment = form.save(commit=False)
        # 
        comment.user = self.request.user
        # GET THE POST PK 
        post_pk = self.kwargs.get("post_pk")
        # GET THE POST OBJECT
        post_obj = get_object_or_404(Post,pk=post_pk)
        # CONNECT TO COMMENT SO COMMENT WILL KNOW THE POST.
        comment.post = post_obj

        comment.save()

        return redirect(self.get_success_url())