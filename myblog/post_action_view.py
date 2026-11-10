from django.views.generic import View
from . models import Post,Comment
from django.http import JsonResponse



class LikeView(View):

    # CHECK IF USER ALREADY LIKED A POST
    def post(self,request,*args,**kwargs):

        feedback = {}

        user = request.user
        post_pk= kwargs.get("post_pk")

        try: 
            post_obj = Post.objects.get(pk=post_pk)
            # IF ALREADY LIKED, UNLIKE (REMOVE)
            if user in post_obj.liked_by.all():
                post_obj.liked_by.remove(user)
                feedback["liked"] = False 

            else:
                # ELSE LIKE (ADD)
                post_obj.liked_by.add(user)
                feedback["liked"] = True

            feedback["count"] = post_obj.liked_by.count()

        except Post.DoesNotExist:
            feedback["status"] = "error"

        return JsonResponse(feedback)   



class CommentLikeView(View):


    def post(self,request,*args,**kwargs):

        feedback = {}
        user = request.user
        comment_pk = kwargs.get("comment_pk")

        try:
            comment_obj = Comment.objects.get(pk=comment_pk)

            if user in comment_obj.liked_by.all():
                comment_obj.liked_by.remove(user)
                feedback["liked"] = False

            else:
                comment_obj.liked_by.add(user)  
                feedback["liked"] = True

            feedback["count"] = comment_obj.liked_by.count()    

        except Comment.DoesNotExist:
            feedback["status"] = "error" 

        return JsonResponse(feedback)        





