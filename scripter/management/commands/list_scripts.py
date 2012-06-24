from django.core.management.base import BaseCommand, CommandError
from scripter.conf import settings
from scripter import VERSION


class Command(BaseCommand):
    help = 'This is will lists all available registered Scripts.'

    def handle(self, *args, **options):
        self.stdout.write('\n')
        self.stdout.write('** Django-Scripter v%s **\n' % VERSION)
        self.stdout.write('\n\n')

        try:
            self.stdout.write('* Available Javascripts:\n')
            self.stdout.write('  ----------------------\n')
            for js in settings.SCRIPTER_JS:
                self.stdout.write('  '+js[0]+'\n')
                for j in js[1]:
                    self.stdout.write('  |____['+j[1]+'], "'+j[0]+'"\n')
                self.stdout.write('\n')
                
            self.stdout.write('\n')

            self.stdout.write('* Available Stylesheet:\n')
            self.stdout.write('  ----------------------\n')
            for js in settings.SCRIPTER_CSS:
                self.stdout.write('  '+js[0]+'\n')
                for j in js[1]:
                    self.stdout.write('  |____['+j[1]+'], "'+j[0]+'"\n')
                self.stdout.write('\n')
                
            self.stdout.write('\n')
        except:
            raise CommandError('command failed..')
