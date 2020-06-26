from django.shortcuts import render

from django.http import HttpResponse

from django.template import loader, RequestContext, Context

from book.models import Book

# Create your views here.

def sayHelloAt20200626(request):
    return HttpResponse("Hello World")

def indexPage(request):
    # return render(request, "book/index.html", {})
    # 记载模板文件，生产模板对象
    template = loader.get_template('book/index.html')
    # 给定模板上下文，给模板文件传递数据
    context = {'numbers': list(range(1, 10))}
    # 模板渲染：产生标准的html文档
    res_html = template.render(context, request)
    # 返回
    return HttpResponse(res_html)

def showBooks(request):
    '''显示所有书籍'''
    books = Book.objects.all();
    return render(request, "book/showBooks.html", {'books' : books})


def bookDetail(request, bookId):
    book = Book.objects.get(id=bookId)
    return render(request, "book/bookInformation.html", {'book': book})



