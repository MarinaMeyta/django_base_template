from django.core.management.base import BaseCommand, CommandError

class  Command(BaseCommand):
	help = 'Changes logo in the header'

	def handle(self, *args, **options):
		try:
			logo = "city.gif"
		except Exception, e:
			raise CommandError("Logo does not exists!")

		self.stdout.write('Sucsessfully changed logo')
