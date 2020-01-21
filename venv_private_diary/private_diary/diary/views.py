from django.shortcuts import render
from django.views import generic

# Create your views here.
# テンプレートに処理を渡す
class IndexView(generic.TemplateView):
    # ここで指定したhtmlを<アプリ名>/templatesディレクトリから探す
    template_name="index.html"
