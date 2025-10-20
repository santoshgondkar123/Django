from django.shortcuts import render, redirect, get_object_or_404
from .models import CartItem
from books.models import Book

def view_cart(request):
    items = []
    total = 0

    if request.user.is_authenticated:
        qs = CartItem.objects.filter(user=request.user)
        for it in qs:
            items.append(it)
            total += it.total_price
    else:
        session_cart = request.session.get('cart', {})
        for book_id, qty in session_cart.items():
            try:
                book = Book.objects.get(pk=book_id)
            except Book.DoesNotExist:
                continue
            # create a simple object for display (no id for guest)
            obj = type('x', (), {})()
            obj.book = book
            obj.quantity = qty
            obj.total_price = book.price * qty
            obj.id = book.id   # ✅ Add this line so template has a valid id
            items.append(obj)
            total += obj.total_price

    return render(request, 'cart/cart.html', {'items': items, 'total': total})


def remove_from_cart(request, pk):
    if request.user.is_authenticated:
        CartItem.objects.filter(pk=pk, user=request.user).delete()
    else:
        cart = request.session.get('cart', {})
        if str(pk) in cart:
            del cart[str(pk)]
            request.session['cart'] = cart

    return redirect('cart:view_cart')   # ✅ redirect instead of render


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
        cart = request.session.get('cart', {})
        cart[str(book.id)] = cart.get(str(book.id), 0) + quantity
        request.session['cart'] = cart

    return redirect('cart:view_cart')
