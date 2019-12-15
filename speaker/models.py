from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from pytils.translit import slugify
from random import choices
import string


class Speaker(models.Model):
    name = models.CharField('ФИО', max_length=255, blank=False, null=True)
    nickName = models.CharField('Ник', max_length=255, blank=False, null=True)
    photo = models.ImageField('Фото)', upload_to='speaker_img/',
                              blank=False, null=True)
    pageHeader = models.ImageField('Изображение для шапки страницы', upload_to='speaker_img/', blank=False,
                                    null=True)

    nickNameSlug = models.CharField(max_length=255, blank=True, null=True, unique=True, db_index=True)
    linkVK = models.CharField('Ссылка на VK', max_length=255, blank=True, null=True, default='Не указано')
    linkTW = models.CharField('Ссылка на Twitch', max_length=255, blank=True, null=True, default='Не указано')
    linkYT = models.CharField('Ссылка на YouTube', max_length=255, blank=True, null=True, default='Не указано')
    linkIN = models.CharField('Ссылка на Instagram', max_length=255, blank=True, null=True, default='Не указано')
    views = models.IntegerField('Просмотров профиля', default=0)
    buys = models.IntegerField('Покупок', default=0)



    about = RichTextUploadingField('Описание', blank=True, null=True)
    streaming = RichTextUploadingField('Что стримит', blank=True, null=True)
    isAtHome = models.BooleanField('Отображать на главной?', default=False)

    def save(self, *args, **kwargs):
        slug = slugify(self.nickName)

        if self.nickNameSlug != slug:
            testSlug = Speaker.objects.filter(nickNameSlug=slug)
            slugRandom = ''
            if testSlug:
                slugRandom = '-' + ''.join(choices(string.ascii_lowercase + string.digits, k=2))
            self.nickNameSlug = slug + slugRandom
        super(Speaker, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return '/speaker/{}/'.format(self.nickNameSlug)

    def __str__(self):
        return 'Стример : {}'.format(self.name)

    class Meta:
        verbose_name = "Стример"
        verbose_name_plural = "Стримеры"