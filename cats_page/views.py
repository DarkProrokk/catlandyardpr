from django.db import connection
from django.shortcuts import render

from layout_app.models import Cats, Breed, FurColor, Feed, Toys, Filler


def cats_page(request):
	result = []
	with connection.cursor() as cursor:
		feeds = Feed.objects.all()
		toys = Toys.objects.all()
		home = Cats.objects.all()
		fillers = Filler.objects.all()
		breed_db = Breed.objects.all()
		fur_db = FurColor.objects.all()
		breed = request.GET.get("breed_id", "breed_id")
		gender = request.GET.get("gender", "gender")
		fur = request.GET.get("fur_id", "fur_id")
		if breed != 'breed_id':
			breed = int(breed)
		if fur != 'fur_id':
			fur = int(fur)
		cursor.execute(f'select idcats from cats where gender = {gender} and breed_id = {breed} and fur_id = {fur}')
		rows = cursor.fetchall()
		for i in rows:
			result.append(Cats.objects.get(idcats=int(i [0])))
		t_count_all = 0
		feed_kg_all = 0
		filler_kg_all = 0
		for toy in toys:
			t_count_all += int(toy.toycount)
		for feed in feeds:
			feed_kg_all += int(feed.feedkg)
		for filler in fillers:
			filler_kg_all += int(filler.fillkg)
		print(t_count_all)
	if rows:
		return render(request, 'cats_page/cats_page.html',
		              {'cats': home, 'breed': breed_db, 'fur': fur_db, 'search': result, 't_count': t_count_all,
		               'feed_kg': feed_kg_all, 'fill_kg': filler_kg_all})
	else:
		return render(request, 'cats_page/cats_page.html',
		              {'cats': home, 'breed': breed_db, 'fur': fur_db, 'search': rows,
		               'err': 'Такого котёнка не нашлось :C'})


def cat(request, cats_name):
	cats = Cats.objects.get(nickname=cats_name)
	return render(request, 'cats_page/cat.html', {'cats': cats})
# Create your views here.
