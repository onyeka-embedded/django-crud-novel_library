from multiprocessing import context
from django.shortcuts import render, redirect
from .models import Novel
from .forms import NovelForm


# Create your views here.
def allNovels(request):
    novels = Novel.objects.all()
    context = {'novels': novels,}
    return render(request, 'allnovels.html', context)


def getNovel(request, pk):
    novel = Novel.objects.get(id=pk)
    context = {'novel': novel,}
    return render(request, 'novel.html', context)


def addNovel(request):
    form = NovelForm()
    if request.method == "POST":
        form = NovelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('allnovels')
    
    context = {'form': form}
    return render(request, 'add_novel.html', context)


def updateProject(request, pk):
    novel = Novel.objects.get(id=pk)
    form = NovelForm(instance=novel)
    if request.method == 'POST':
        form = NovelForm(request.POST, instance=novel)
        if form.is_valid():
            form.save()
            return redirect('allnovels')
    context = {'form': form}
    return render(request, 'update_novel.html', context)


def deleteNovel(request, pk):
    novel = Novel.objects.get(id=pk)
    if request.method == 'POST':
        novel.delete()
        return redirect('allnovels')
    context = {'object': 'novel'}
    return render(request, 'delete_novel.html', context)



