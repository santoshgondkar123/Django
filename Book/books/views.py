from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, Category
from cart.models import CartItem
from django.core.paginator import Paginator


def index(request):
    qs = Book.objects.all().order_by('title')
    paginator = Paginator(qs, 12)
    page = request.GET.get('page')
    books = paginator.get_page(page)
    page_number = request.GET.get('page')  # ✅ defines the variable
    books = paginator.get_page(page_number)
    categories = Category.objects.all()
    return render(request, 'books/index.html', {'books': books, 'categories': categories})

def book_detail(request, slug):
    book = get_object_or_404(Book, slug=slug)
    return render(request, 'books/book_detail.html', {'book': book})

def add_to_cart(request, slug):
    book = get_object_or_404(Book, slug=slug)
    quantity = int(request.POST.get('quantity', 1))
    if request.user.is_authenticated:
        cart_item, created = CartItem.objects.get_or_create(user=request.user, book=book)
        if not created:
            cart_item.quantity += quantity
        else:
            cart_item.quantity = quantity
        cart_item.save()
    else:
        # Simple session-based cart for anonymous users
        cart = request.session.get('cart', {})
        cart[book.id] = cart.get(str(book.id), 0) + quantity
        request.session['cart'] = cart
    return redirect('cart:view_cart')

