from django.db import models


# Create a Blog Model

class Blog(models.Model):

    title = models.CharField(max_length=255)
    pub_data = models.DateTimeField(auto_now=False, auto_now_add=False)
    body = models.TextField()
    image = models.ImageField( upload_to='images/')

    def __str__(self):
        return self.title


    def summary(self):
        return self.body[:100]


    def pub_date_pretty(self):
        return self.pub_data.strftime('%b %e %Y')


#Title
#pub_data
#body
#image


# Add the Blog app to the settings


# Create a migration

# Migrate


# Add to the Admin