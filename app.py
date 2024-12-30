from flask import Flask, render_template_string, request, send_file
import markdown
from io import BytesIO

app = Flask(__name__)

# Base HTML with CSS
BASE_HTML = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Markdown to HTML Converter</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f9;
            margin: 0;
            padding: 0;
        }
        header {
            background-color: #4CAF50;
            color: white;
            padding: 1rem;
            text-align: center;
        }
        main {
            max-width: 800px;
            margin: 2rem auto;
            background: white;
            padding: 2rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            border-radius: 8px;
        }
        textarea {
            width: 100%;
            height: 150px;
            font-size: 16px;
            padding: 0.5rem;
            border: 1px solid #ccc;
            border-radius: 4px;
            margin-bottom: 1rem;
        }
        button {
            background-color: #4CAF50;
            color: white;
            padding: 0.75rem 1.5rem;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
        }
        button:hover {
            background-color: #45a049;
        }
        .output {
            padding: 1rem;
            background: #eaf7e4;
            border: 1px solid #d1e7d1;
            border-radius: 4px;
            margin-bottom: 1rem;
        }
        a {
            color: #4CAF50;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <header>
        <h1>Markdown to HTML Converter</h1>
    </header>
    <main>
        {% block content %}{% endblock %}
    </main>
</body>
</html>
'''

@app.route('/')
def index():
    content = '''
        <form method="POST" action="/convert">
            <textarea name="markdown_text" placeholder="Enter Markdown text here"></textarea>
            <button type="submit">Convert to HTML</button>
        </form>
    '''
    return render_template_string(BASE_HTML.replace("{% block content %}{% endblock %}", content))

@app.route('/convert', methods=['POST'])
def convert():
    markdown_text = request.form['markdown_text']
    html_content = markdown.markdown(markdown_text)
    content = f'''
        <div class="output">
            <h2>HTML Preview</h2>
            <div>{html_content}</div>
        </div>
        <form method="POST" action="/download">
            <input type="hidden" name="html_content" value="{html_content}">
            <button type="submit">Download HTML</button>
        </form>
        <a href="/">Go back</a>
    '''
    return render_template_string(BASE_HTML.replace("{% block content %}{% endblock %}", content))

@app.route('/download', methods=['POST'])
def download():
    html_content = request.form['html_content']
    buffer = BytesIO()
    buffer.write(html_content.encode('utf-8'))
    buffer.seek(0)
    return send_file(
        buffer, 
        as_attachment=True, 
        download_name="converted.html", 
        mimetype='text/html'
    )

if __name__ == '__main__':
    app.run(debug=True)
