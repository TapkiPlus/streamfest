from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from pytils.translit import slugify
from random import choices
import string
from colorfield.fields import ColorField

class Sponsor(models.Model):
    image = models.ImageField('Изображение)', upload_to='sponsor_img/',
                              blank=False, null=True)
    bg_color = ColorField('Цвет бордера',default='#000000')
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

class StandStar(models.Model):
    question = models.CharField('Вопрос', max_length=255, blank=False,null=True)
    answer = RichTextUploadingField('Ответ', blank=True, null=True)
    isActive = models.BooleanField('Выводить на странице', default=True)
    def __str__(self):
        return 'Вопрос - Ответ №{}'.format(self.id)

    class Meta:
        verbose_name = "Стать участником Вопрос - Ответ"
        verbose_name_plural = "Стать участником Вопросы - Ответы"

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


class Settings(models.Model):
    showTwitch = models.BooleanField('Показывать твич?', default=False)


class Callback(models.Model):
    name = models.CharField('Имя', max_length=255, blank=False, null=True)
    email = models.CharField('E-Mail', max_length=255, blank=False, null=True)
    text = models.TextField('Сообщение', blank=True, null=True)

    def __str__(self):
        return 'Сообщение от: {}'.format(self.name)

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"


class StaticPage(models.Model):
    apply_text = RichTextUploadingField('Текст на странице - Стать участником', blank=False, null=True)
    index_about_text = RichTextUploadingField('Текст на главной странице - Информация', blank=False, null=True)
    index_about_image = models.ImageField('Изображение на главной странице - Информация', upload_to='img/', blank=False,
                             null=True)
    class Meta:
        verbose_name = "Текст для статических страниц"
        verbose_name_plural = "Текст для статических страниц"

class Feedback(models.Model):
    quote = models.CharField('Цитата', max_length=255, blank=False, null=True)
    name = models.CharField('Отзыв от', max_length=255, blank=False, null=True)
    image = models.ImageField('Аватарка от кого отзыв', upload_to='post_img/', blank=False,
                              null=True)
    text = models.TextField('Текст', blank=True, null=True)
    is_active = models.BooleanField('Отображать?', default=True)

    def __str__(self):
        return 'Отзыв от: {}'.format(self.name)

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

class Activity(models.Model):
    name = models.CharField('Название', max_length=255, blank=False, null=True)
    image = models.ImageField('Картинка', upload_to='post_img/', blank=False,
                              null=True)
    text = RichTextUploadingField('Текст', blank=False, null=True)

    def __str__(self):
        return 'Активность: {}'.format(self.name)

    class Meta:
        verbose_name = "Активность"
        verbose_name_plural = "Активности"

class MailSubscribe(models.Model):
    email = models.CharField('E-Mail', max_length=255, blank=False, null=True)

    def __str__(self):
        return 'Подписка на рассылку: {}'.format(self.email)

    class Meta:
        verbose_name = "Подписка на рассылку"
        verbose_name_plural = "Подписки на рассылку"