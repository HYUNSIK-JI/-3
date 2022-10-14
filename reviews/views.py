from django.shortcuts import render,redirect,get_object_or_404
from .models import Review,Comment
from .forms import ReviewForm,CommentForm
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth import get_user_model
from accounts.models import User

def index(request):
    reviews = Review.objects.all().order_by('-pk')
    page = int(request.GET.get('p', 1))
    pagenator = Paginator(reviews, 5)
    boards = pagenator.get_page(page)
    context = {
        'reviews': reviews,
        "boards":boards,
    }
    return render(request, 'reviews/index.html', context)
    
@login_required
def create(request):
    if request.method == 'POST':
        Review_Form = ReviewForm(request.POST)
        if Review_Form.is_valid():
            post = Review_Form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('reviews:index')
    else: 
        Review_Form = ReviewForm()
    context = {
        'Review_Form': Review_Form
    }
    return render(request, 'reviews/new.html', context=context)

@login_required()
def detail(request, pk):
    review = Review.objects.get(pk=pk)
    review = get_object_or_404(Review, pk=pk)
    comments = Comment.objects.filter(article_id=pk)
    comment_form = CommentForm(request.POST)
    context = {
            "review": review,
            "all": review.like_users.all(),
            "count": review.like_users.count,
            "comment_form":comment_form,
            "comments":comments,
    }
    return render(request, "reviews/detail.html", context)
    
@login_required
def update(request, pk):
    reviews = Review.objects.get(pk=pk)
    if request.method == "POST":
        Review_form = ReviewForm(request.POST, instance=reviews)
        if Review_form.is_valid():
            Review_form.save()
            return redirect("reviews:index")
    else:
        Review_form = ReviewForm(instance=reviews)
    context = {
        "Review_form": Review_form,
        "reviews": reviews,
    }
    return render(request, 'reviews/update.html', context)
    
@login_required
def delete(request, pk):
    reviews = Review.objects.get(pk=pk)
    reviews.delete()
    return redirect('reviews:index')
@login_required()
def like(request, pk):
    reviews = get_object_or_404(Review, pk=pk)
    if reviews.like_users.filter(id=request.user.pk).exists():
        reviews.like_users.remove(request.user)
    else:
        reviews.like_users.add(request.user)
    return redirect('reviews:detail', pk)

@require_POST
def comments_create(request, pk):
    if request.user.is_authenticated:
        reviews = get_object_or_404(Review, pk=pk)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.article = reviews
            comment.user = request.user
            comment.save()
        return redirect('reviews:detail', reviews.pk)
    return redirect('accounts:login')


@require_POST
def comments_delete(request, review_pk, comment_pk):
    if request.user.is_authenticated:
        comment = Comment.objects.get(pk=comment_pk)  
        if request.user == comment.user:
            comment.delete()
    return redirect('reviews:detail', review_pk)


def search(request):
    search = request.GET.get('search','')
    c = Comment.objects.filter(content = search)

    list_ =[]
    for i in c:
        r = Review.objects.get(pk=i.article_id).id
        list_.append(r)

    search_list = Review.objects.filter(
            Q(title__icontains = search) | #제목
            Q(content__icontains = search)| #내용
            Q(grade__icontains = search)| #평점
            Q(user_id__username__icontains = search)| #작성자 이름
            Q(id__in=list_) #댓글
        )

    if search:
        if search_list:
            page = int(request.GET.get('p', 1))
            pagenator = Paginator(search_list, 3)
            boards = pagenator.get_page(page)
            return render(request, 'reviews/search.html',{'search':search, "boards":boards, "search_list":search_list})
        else:
            k="검색 결과가 없습니다 다시 검색해주세요"
            context = {
                "v":k
                }
            return render(request,'reviews/searchfail.html', context)
    else:
        k="검색 결과가 없습니다 다시 검색해주세요"
        context = {
            "v":k
        }
        return render(request,'reviews/searchfail.html', context)
def searchfail(request):
    return render(request,'reviews/searchfail.html')