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


class Faq(models.Model):
    question = models.ImageField('Вопрос)', upload_to='sponsor_img/',
                              blank=False, null=True)
    answer = RichTextUploadingField('Ответ', blank=True, null=True)
    isVip = models.BooleanField('Выводить на странице', default=True)
    def __str__(self):
        return 'Вопрос - Ответ №{}'.format(self.id)

    class Meta:
        verbose_name = "Вопрос - Ответ"
        verbose_name_plural = "Вопросы - Ответы"