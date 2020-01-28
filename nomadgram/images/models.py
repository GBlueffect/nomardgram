from django.db import models
from django.utils.translation import ugettext_lazy as _
from nomadgram.users import models as user_models

# Create your models here.
class TimeStampedModel(models.Model):
    """ TimeStampedModel model """

    created_at = models.DateTimeField(_("created_at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated_at"), auto_now=True)

    class Meta:
        abstract = True


class Image(TimeStampedModel):
    """ Image model """

    file = models.ImageField(_("file"))
    location = models.CharField(_("location"), max_length=140)
    caption = models.TextField(_("caption"))
    creator = models.ForeignKey(user_models.User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return "{} - {}".format(self.location, self.caption)


class Comment(TimeStampedModel):
    """ Comment model """

    message = models.TextField(_("message"))
    creator = models.ForeignKey(user_models.User, on_delete=models.CASCADE, null=True)
    image = models.ForeignKey(Image, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.message


class Like(TimeStampedModel):
    """ Like model """

    creator = models.ForeignKey(user_models.User, on_delete=models.CASCADE, null=True)
    image = models.ForeignKey(Image, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return "User: {} - Image Caption: {}".format(self.creator.username, self.image.caption)

