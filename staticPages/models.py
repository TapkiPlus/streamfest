from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

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