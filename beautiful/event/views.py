from django.shortcuts import render, redirect
from . models import Event, Tag, Googlemap
from . forms import EventCreateForm, TagForm
# Create your views here.



def event_main(request, tag_pk=None):
    if tag_pk is not None:
        event_list = Event.objects.filter(tag__pk=tag_pk)
        tag = Tag.objects.get(pk=tag_pk)

        a = event_list.count()

    else:
        event_list = Event.objects.all()
        tag = None

        a = event_list.count()


    ctx = {
        'event_list' : event_list,
        'tag_list' : Tag.objects.all(),
        'tag_selected' : tag,

            }
    return render(request, 'event/event_main.html', ctx)


def event_create(request):
    form = EventCreateForm(request.POST or None)
    tag = TagForm(request.POST or None)

    ctx = {
        'form' : form,
        'tag' : tag,
    }
    if request.method == "POST":
        if form.is_valid() and tag.is_valid():
            event = form.save(commit=False)
            event.tag = tag.save() #여기 잘못됐대
            event.save()
            return redirect(event.get_absolute_url())


    return render(request, 'event/event_create.html', ctx)


def event_place(request):
    Map = Googlemap.objects.all()
    ctx = {
        'map': Map,
    }

    return render(request, 'event/event_place.html', ctx)




# Create your views here.
