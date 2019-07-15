from bs4 import BeautifulSoup

html_doc = """
<html>
 <head>
  <title>Hello world</title>
</head>
<body>
  <p>I like python </p>
 </body>
</html>
"""

soup = beautifulsoup(html_doc, 'html.parser')
