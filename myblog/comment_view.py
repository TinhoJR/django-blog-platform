from django.views.generic import CreateView
from . models import Comment,Post
from . forms import CommentForm
from django.urls import reverse_lazy,reverse
from django.http import JsonResponse,Http404


class CommentView(CreateView):
    model = Comment
    # template_name = "comment.html"
    form_class = CommentForm
    

    def get_success_url(self):
        post_pk = self.kwargs.get("post_pk")
        return reverse("post_detail",args=[post_pk])


    def form_valid(self,form):
        comment = form.save(commit=False)
        # 
        comment.instance.user = self.request.user
        # GET THE POST PK 
        post_pk = self.kwargs.get("post_pk")
        try:
            # GET THE POST OBJECT
            post_obj = Post.objects.get(pk=post_pk)
        except Post.DoesNotExist:
            raise Http404("POST NOT FOUND")
        # CONNECT TO COMMENT SO COMMENT WILL KNOW THE POST.
        comment.instance.post = post_obj

        comment.save()

        data = {
            "id": comment.pk,
            "username": comment.user.username,
            "comment": comment.comment,
            "date": comment.date
        }

           
         
        return JsonResponse(data,status=201)