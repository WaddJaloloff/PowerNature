from django.db import models



class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    context = models.TextField(verbose_name='Текст')
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Новости'
        verbose_name_plural = 'Новости'

class Savollar(models.Model):
    savol = models.CharField(max_length=110, verbose_name='Вопрос')
    javob = models.TextField(verbose_name='Ответ')
    
    def __str__(self):
        return self.savol
    
    class Meta:
        verbose_name = "Часто задаваемые вопросы"
        verbose_name_plural = "Часто задаваемые вопросы"

class OurWorks(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    image = models.ImageField(upload_to='our_works/', verbose_name='Изображение')
    
    class Meta:
        verbose_name = "Наши работы"
        verbose_name_plural = "Наши работы"
