from django.shortcuts import redirect
from django.urls.base import reverse
from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response
from post.models import Post
from django.core.paginator import Paginator


class listPosts(APIView):
    def get(self, request):
        posts_qset = Post.objects.all().order_by('id')
        posts_paginator = Paginator(posts_qset, 10)
        page_number = request.GET.get('page')
        page_obj = posts_paginator.get_page(page_number)
        posts = list(page_obj.object_list.values())
        pagination_details = {
            'all_post_count': posts_paginator.count,
            'page_count': posts_paginator.num_pages,
            'this_page_number': page_obj.number,
            'has_next_page': page_obj.has_next(),
            'has_previous_page': page_obj.has_previous()
        }
        if pagination_details['has_next_page']:
            pagination_details['next_page_number'] = page_obj.next_page_number(
            )
        if pagination_details['has_previous_page']:
            pagination_details[
                'previous_page_number'] = page_obj.previous_page_number()
        posts.append(pagination_details)
        return Response(posts)


class Redirect_to_ListPosts(View):
    def get(self, request):
        return redirect(reverse('list_posts'))