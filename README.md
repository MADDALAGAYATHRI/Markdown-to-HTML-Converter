
# Markdown to HTML Converter

## Description
A simple web application that converts Markdown text into HTML. Users can enter Markdown-formatted text, preview the converted HTML, and download the result as an HTML file. The app is built using Python and Flask.

## Features
- **Markdown Input**: Enter Markdown text in a user-friendly text area.
- **HTML Preview**: View the converted HTML in real-time.
- **Download Option**: Download the HTML output as a file.
- **Responsive Design**: Modern and mobile-friendly interface with CSS styling.

## Technologies Used
- **Backend**: Python, Flask
- **Frontend**: HTML, CSS
- **Markdown Parsing**: Python `markdown` library

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/markdown-to-html.git
   cd markdown-to-html
   ```

2. Install the required Python packages:
   ```bash
   pip install flask markdown
   ```

3. Run the application:
   ```bash
   python app.py
   ```

4. Open your browser and visit:
   ```
   http://127.0.0.1:5000/
   ```

## Usage
1. Enter your Markdown text in the text box.
2. Click **Convert to HTML** to preview the HTML output.
3. Download the converted HTML file if needed.

## Example Markdown
```markdown
# Heading 1
## Heading 2
- Bullet 1
- Bullet 2

[Link](https://example.com)
```

## Screenshots
### Input Page
- Markdown entry area with a submit button.

### Output Page
- HTML preview and download options.
