from flask import Flask

app = Flask(__name__)

# Minimal HTML content for the webpage
HTML_CONTENT = """
<!DOCTYPE html><html lang="en"><body>
    <div style="position:absolute;font-size:36px;left:50%;top:50%;transform:translate(-50%,-50%)">Hello World</div>
</body></html>
"""

# Define route to serve the HTML content
@app.route('/')
def hello():
    return HTML_CONTENT

if __name__ == '__main__':
    # Run the Flask app
    app.run(host='192.168.1.82', port=45680)
