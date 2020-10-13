from django_project import models

import factory.django


class ThingFactory(factory.django.DjangoModelFactory):

    do_calculate = False

    class Meta:
        model = models.Thing

    class Params:
        do_calculate = factory.Trait(
            _bogus=factory.PostGenerationMethodCall('calculate_sum')
        )


class DoCalculateFactory(ThingFactory):

    do_calculate = True


class Thing3Plus4Factory(DoCalculateFactory):

    a = 3
    b = 4
