def opt():
	options = {
		 'app' : {
			'name' : 'WDD_PY_2017',
			'author' : 'Allan Davidson | http://github.com/SneakyMelon/',
			'description' : 'Testing the Python Environment for Web development using Flask as the operating engine',
			'version' : '127.0.0.1',
			'build_date' : '2017'
		},
		'users' : [
					{
						'name': 'World',
						'nick' : 'Whole Wide World'
					},
					{
						'name': 'Allan', # Data
						'nick': 'Melon'  # Data
					},
					{
						'name': 'Steve', # Data
						'nick': 'Sloth'  # Data
					},
					{
						'name': 'Phil', # Data
						'nick': 'Beavur'  # Data
					}
		],
		'page' : {
			'title' : "Home Page",
			'resources' : {
				'bootstrap' : {
					'js' : [
						'static/vendor/jquery/jquery.min.js',
						'static/vendor/popper/popper.min.js',
						'static/vendor/bootstrap/js/bootstrap.min.js',
						'static/vendor/jquery-easing/jquery.easing.min.js',
						'static/js/scrolling-nav.js'
					],
					'css' : [
						'static/vendor/bootstrap/css/bootstrap.min.css',
						'static/css/scrolling-nav.css'
					],
				},
				'stylesheets' : {
					'custom' :	[
						#'static/style.css',
					]
				},
			},
		},
		'content' : {
			# world, name, nick
		}
	}

	return options