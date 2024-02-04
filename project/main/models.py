from django.db import models
# Файл для описания моделек!
# классы ОБЯЗАТЕЛЬНО наследуются от models.Model.
# Model это стандартный класс описаный в Джанго, который реализует взаимодействие наших обьектов с БД.
class Author(models.Model):# создавая класс, создаем таблицу в БД.
    # Ниже определяем поля таблицы задавая перечень атрибутов!
    name = models.CharField(max_length=100) # создали текстовое поле NAME с макс длиной в 100 символов.
    email = models.EmailField(primary_key = True) # Создали поле имейл и указали что оно является первичным ключем.
# Primary key задавать не обязательно, т/к джанго автоматически создаст дополнительное поле для идентификации.
# Ниже прописываем метод __str__ чтобы в админке отображалось имя автора
    def __str__(self):
        return self.name
    
class Post(models.Model):
    #POST_TYPES = [("c", "copyright"), ("p", "public license")] # в константе POST_TYPES перечисляем варианты выбора для переменной post_type. В проекте не использую.
    #post_type = models.CharField(max_length=1, choices = POST_TYPES)
    title = models.CharField(max_length=200, blank=True) # Свойство blank со значение True позволяет оставить строку пустой.По умолчанию False.
    content = models.TextField()
    issued = models.DateTimeField() # будет отображаться дата написания поста
    image = models.ImageField(upload_to= 'uploads', blank=True) # upload_to - это путь на файловой системе куда должны загружаться картинки
    # Ниже прописываем связь между таблицей Post и таблицей Author.
    # Первый параметр это имя таблицы. второй(on_delete) - сценарий удаления. Если какого-то автора удалят из БД - все его сообщения так же удаляться.
    author = models.ForeignKey('Author', on_delete = models.CASCADE)
    

class Request(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    phone_number = models.CharField(max_length=12, primary_key = True)
    message = models.TextField(max_length=250)
    def __str__(self):
	    return self.name
