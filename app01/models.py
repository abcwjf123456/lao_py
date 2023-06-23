from django.db import models


# Create your models here.
class Book(models.Model):
    # 如果没有指定主键字段,默认orm会给这个表添加一个名称为id的主键自增字段
    # 如果制定了,以指定的为准,那么orm不在创建那个id字段了
    # nid = models.AutoField(primary_key=True)  #int primary_key auto_increment,
    title = models.CharField(max_length=32)  # varchar 书籍名称
    # price = models.FloatField()  #
    price = models.DecimalField(max_digits=5, decimal_places=2)  # 999.99 价格
    pub_date = models.DateField()  # date  出版日期
    publish = models.CharField(max_length=32)  # 出版社名称
