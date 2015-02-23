from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model
from optparse import make_option

import logging

logger = logging.getLogger('django.commands')


class Command(BaseCommand):
    help = "Create a super user"
    option_list = BaseCommand.option_list + (
        make_option('--password', action='store', dest='password',
                    help=('Password of the superuser'), ),
        make_option('--email', action='store', dest='email',
                    help=('Email of the superuser'), ),
    )

    def handle(self, *args, **options):
        logger.info('Creation of a superuser')
        if options['email'] is None and\
           options['password'] is None:
            raise CommandError('You must provide --email'
                               'and --password argument')

        UserModel = get_user_model()
        user = UserModel.objects.create(email=options['email'])
        user.set_password(options['password'])
        user.save()
        logger.info('SuperUser [{!s}] created'.format(user.pk))
