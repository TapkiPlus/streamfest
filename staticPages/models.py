from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from pytils.translit import slugify
from random import choices
import string

class Sponsor(models.Model):
    image = models.ImageField('Изображение)', upload_to='sponsor_img/',
                              blank=False, null=True)
    isVip = models.BooleanField('ВИП спонсор?', default=False)
    def __str__(self):
        return 'Спонсор №{}'.format(self.id)

    class Meta:
        verbose_name = "Спонсор"
        verbose_name_plural = "Спонсоры"

class Banner(models.Model):
    order = models.IntegerField('Порядок отображения', default=1)
    image = models.ImageField('Картинка', upload_to='banners/', blank=False)
    smallText = models.CharField('Маленький текст', max_length=255, blank=False)
    bigText = models.CharField('Большой текст', max_length=255, blank=False)
    buttonText = models.CharField('Надпись на кнопке', max_length=255, blank=False)
    buttonUrl = models.CharField('Ссылка с кнопки', max_length=255, blank=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return 'Баннер, порядковый номер : %s' % self.order

    class Meta:
        verbose_name = "Баннер"
        verbose_name_plural = "Баннеры"


class Faq(models.Model):
    question = models.CharField('Вопрос', max_length=255, blank=False,null=True)
    answer = RichTextUploadingField('Ответ', blank=True, null=True)
    isActive = models.BooleanField('Выводить на странице', default=True)
    def __str__(self):
        return 'Вопрос - Ответ №{}'.format(self.id)

    class Meta:
        verbose_name = "Вопрос - Ответ"
        verbose_name_plural = "Вопросы - Ответы"

class Post(models.Model):
    name = models.CharField('Название', max_length=255, blank=False, null=True)
    image = models.ImageField('Изображение для поста', upload_to='post_img/', blank=False,
                                   null=True)
    nameSlug = models.CharField(max_length=255, blank=True, null=True, unique=True, db_index=True)
    author = models.CharField('Автор',max_length=255, blank=True, null=True, unique=True, db_index=True)
    date = models.CharField('Дата', max_length=255, blank=True, null=True, unique=True, db_index=True)

    views = models.IntegerField('Просмотров', default=0)

    about = models.TextField('Описание', blank=True, null=True)
    fullText = RichTextUploadingField('Содержание поста', blank=True, null=True)
    isAtHome = models.BooleanField('Отображать на главной?', default=False)

    def save(self, *args, **kwargs):
        slug = slugify(self.name)
        if self.nameSlug != slug:
            testSlug = Post.objects.filter(nameSlug=slug)
            slugRandom = ''
            if testSlug:
                slugRandom = '-' + ''.join(choices(string.ascii_lowercase + string.digits, k=2))
            self.nameSlug = slug + slugRandom
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return 'Пост: {}'.format(self.name)

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"