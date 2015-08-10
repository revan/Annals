from jinja2 import Template

template = Template("""
<html>
<head>
	<meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{{ title }}</title>

    <link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css" rel="stylesheet">

    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
      <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
    <![endif]-->

</head>
<body style="padding-top: 50px;">

	<nav class="navbar navbar-inverse navbar-fixed-top">
      <div class="container">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" href="#">{{ title }}</a>
        </div>
        <div id="navbar" class="collapse navbar-collapse">
          <ul class="nav navbar-nav">
            <li class="active"><a href="#">Annals</a></li>
            {% if latest %}
            	<li><a href="{{ latest }}">Latest</a></li>
        	{% endif %}
          </ul>
        </div><!--/.nav-collapse -->
      </div>
    </nav>

	<div class="container" style="padding: 40px 15px;text-align: center;">
		<div class="page-header">
			<h1> {{ title }} - Archive </h1>
		</div>

		<ul style="list-style-position: inside;">
			{% for file in files %}
				<li>
					<a href="{{ file }}"> {{ file }} </a>
				</li>
			{% endfor %}
		</ul>
	</div>

	<footer class="footer" style="position: absolute;bottom: 0;width: 100%;height: 60px;background-color: #f5f5f5;">
      <div class="container" style="margin-top:20px;text-align: center;">
        <p class="text-muted">Archived with Annals. <a href="https://github.com/revan/Annals">Github!</a></p>
      </div>
    </footer>
</body>
</html>
"""
)