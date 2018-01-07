from django.db import models


class Term(models.Model):
    term_text = models.CharField(max_length=200)
    priority = models.IntegerField(default=1)

    def __str__(self):
        return self.term_text


class Sentence(models.Model):
    term = models.ForeignKey(Term, on_delete=models.CASCADE)
    sentence_text = models.CharField(max_length=500)

    def __str__(self):
        return self.sentence_text
