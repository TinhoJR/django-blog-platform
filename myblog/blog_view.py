from django.shortcuts import render
from django.views.generic import TemplateView,CreateView,RedirectView,UpdateView,DeleteView,View,ListView,DetailView
from django.utils.timezone import datetime
from django.urls import reverse_lazy
from .forms import PostForm,CommentForm
from .models import Post,Comment

from django.contrib.auth.mixins import PermissionRequiredMixin, UserPassesTestMixin, LoginRequiredMixin


class CreatePostView(LoginRequiredMixin,CreateView):
    model = Post
    template_name = "create-blog.html"
    # fields = ["title","author","body"]
    success_url = reverse_lazy("blog-list")
    form_class = PostForm 

    
    def form_valid(self,form):
        form.instance.user = self.request.user
        return super(CreatePostView,self).form_valid(form)
    
    def get_context_data(self, **kwargs):
        ctx =  super(CreatePostView,self).get_context_data()
        ctx["name"] = "TINHO"

        return ctx  


class PostDetailView(LoginRequiredMixin,DetailView):
    model = Post
    template_name = "post_detail.html"
    context_object_name = "post"


    def get_context_data(self, **kwargs):
        ctx =  super(PostDetailView,self).get_context_data()
        ctx["name"] = "TINHO"
        ctx["comment_form"] = CommentForm()
        ctx["is_liked"] = self.object.liked_by.filter(pk=self.request.user.pk).exists()
        # comments = Comment.objects.filter(post=self.object)
        # for comment in comments:


        # ctx["comments"] = Comment.objects.all()
        # USER CAN ONLY SEE COMMENT OF THE CURRENT POST.
        # ctx["comments"] = Comment.objects.filter(post=ctx["post"])

        return ctx  

    # slug_field = "slug"
    # slug_url_kwarg = "slug" 
    

class DetailViewX(View):
      
      context_object_name = "post"

      def get(self,request,*args,**kwargs):
          pk = kwargs.get("pk")
          try:
              post = Post.objects.get(pk=pk)
          except post.DoesNotExist :
              error_msg = f"Post with id {pk} does not Exist"
              return render(request,"error.html",{"error_msg": error_msg})   
          ctx = {self.context_object_name: post}

          return render(request,"detail.html",ctx)
      

      def post(self,request,*args,**kwargs):
          pass


class DeleteBlogView(DeleteView):
    model = Post
    template_name = "delete-blog.html"
    success_url = reverse_lazy("blog-list")  

    def get_context_data(self, **kwargs):
        ctx =  super(DeleteBlogView,self).get_context_data()
        ctx["name"] = "TINHO"

        return ctx  



class UpdatePostView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    template_name = "update-post.html"
    form_class = PostForm
    success_url = reverse_lazy("blog-list")

    def get_context_data(self, **kwargs):
        ctx =  super(UpdatePostView,self).get_context_data()
        ctx["name"] = "TINHO"
 
        return ctx  

    def test_func(self):
        # if not self.request.user.is_authenticated:
        #     return False

        # CHECK IF THE POST BELONGS TO THE PERSON LOGGED IN
        post = self.get_object()
        if post.user != self.request.user:
            return False
        
        return True




