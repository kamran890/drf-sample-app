from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .serializers import postSerializer
from .models import post
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from .permissions import IsOwnerOrReadOnly
from enum import Enum
from django.db.models import Q
from django.db.models import F

# Enum-class for status in post Model
class enum_status(Enum):
    draft = 'draft'
    unpublished = 'unpublished'
    published = 'published'

# Signup view
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'sample_app/signup.html', {'form': form})

# Home page view
def home(request):
    return render(request, 'sample_app/base.html', {'request': request})

# ViewSet for post end points 
class postViewSet(viewsets.ModelViewSet):
		permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
		queryset = post.objects.all().order_by('created_on')
		serializer_class = postSerializer

		def perform_create(self, serializer):
			serializer.save(author=self.request.user)

		def list(self, request):
			queryset = post.objects.filter(Q(status=enum_status.published) | Q(author=self.request.user))
			queryset.filter(~Q(author = self.request.user)).update(retrieves_count=F('retrieves_count')+1)
			serializer = postSerializer(queryset, many=True)
			return Response(serializer.data)

		def retrieve(self, request, pk=None):
			queryset = post.objects.filter(Q(status=enum_status.published) | Q(author=self.request.user))
			post_query = get_object_or_404(queryset, pk=pk)
			if post_query.author != self.request.user:
				post_query.retrieves_count += 1
				post_query.save()
			serializer = postSerializer(post_query)
			return Response(serializer.data)