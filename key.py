# some private account settings
MODE = 'local'

settings = {
			'local': {
				'database': {
					'name': '',
					'user': '',
					'password': '',
					'host': '',
					'port': ''
				},
				'staticfiles_dir':'',
				'template_dirs':(
					'',
				)
			},

			'remote': {
				'database': {
					'name': '',
					'user': '',
					'password': '',
					'host': '',
					'port': ''
				},
				'staticfiles_dir':'',
				'template_dirs':(
					'',
				)
			}
		}

setting = settings[MODE]
