"""
This module sets up a Flask web server with routes for rendering templates
and handling form submissions.
"""

from flask import Flask, render_template, request
from gebruiker import send_email

app = Flask(__name__)

@app.route('/')
def index():
    """
    Render the index.html template.
    
    Returns:
        A rendered HTML template for the index page.
    """
    return render_template('index.html')

@app.route('/gebruiker', methods=['POST'])
def gebruiker():
    """
    Handle form submission, send an email with the form data, and render the gebruiker.html template.
    
    Returns:
        A rendered HTML template for the gebruiker page with the form data.
    """
    # Get the form data
    form_data = request.form

    try:
        send_email(form_data)
    except Exception as e:
        # Log the exception and stop the Flask server
        app.logger.error(f"Error sending email: {e}")
        exit(1)
        return "Server shutting down..."

    # Pass the output to the template
    return render_template('gebruiker.html', form_data=form_data)

if __name__ == '__main__':
    app.run(debug=True)
