from django.db import models


class FurColor(models.Model):
    color = models.CharField(max_length=45)

    def __str__(self):
        return self.color

    class Meta:
        verbose_name = 'Цвет'  # то как будет называться таблица в админке, если будет один кот
        verbose_name_plural = 'Цвета'

class Breed(models.Model):
    breed = models.CharField(max_length=45)

    def __str__(self):
        return self.breed

    class Meta:
        verbose_name = 'Порода'  # то как будет называться таблица в админке, если будет один кот
        verbose_name_plural = 'Породы'

class Cats(models.Model):
    idcats = models.AutoField(db_column='idCats', primary_key=True) # id котайв таблице, который будет автоматически создаваться при добавление нового кота
    nickname = models.CharField(db_column='Nickname', max_length=45)
    gender = models.CharField(db_column='Gender', choices=[('Мальчик','Мальчик'),('Девочка', 'Девочка')], max_length=45)
    fur = models.ForeignKey(FurColor, on_delete=models.PROTECT, null=True)
    breed = models.ForeignKey(Breed, on_delete=models.PROTECT, null=True)
    image = models.ImageField(db_column='Image', upload_to='img/', blank=True, null=True)
    description = models.TextField(default='')
    def __str__(self):
        return self.nickname

    class Meta:
        db_table = 'cats'
        verbose_name = 'Кот' # то как будет называться таблица в админке, если будет один кот
        verbose_name_plural = 'Коты' # то как будет называться таблица в админке, если будет два кота

class Feed(models.Model):
    idfeed = models.AutoField(db_column='idfeed', primary_key=True)
    feedname = models.CharField(max_length=45)
    feedkg = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.feedname

class Toys(models.Model):
    idtoy = models.AutoField(primary_key=True)
    toyname = models.CharField(max_length=45)
    toycount = models.IntegerField()

    def __str__(self):
        return self.toyname

class Filler(models.Model):
    fillid = models.AutoField(primary_key=True)
    fillkg = models.IntegerField()

class TakeCat(models.Model):
    idtiket = models.AutoField(primary_key=True)
    catid = models.ForeignKey(Cats, on_delete=models.PROTECT, null=False)
    cl_name = models.CharField(max_length=40)
    cl_number = models.CharField(max_length=20)

    def __str__(self):
        return self.cl_name