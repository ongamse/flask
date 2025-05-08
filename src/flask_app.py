from flask import Flask
from rich import print

from db import get_challenges_for_candidate

app = Flask(__name__)


@app.route("/")
def index():
    return (
        "Hi 👋 head out to "
        '<a href="/challenges/111.111.111-11">this link</a> to get started.'
    )


@app.route("/challenges/<cpf>")
def get_challenges(cpf: str):
def get_challenges(cpf: str):
    print(f"[bold]{'-' * 50}[/bold]")
    print(f"[bold]Passing input:[/bold] [yellow]{cpf}[/yellow]")

    # Explicitly escape user input before processing
    escaped_cpf = html.escape(cpf)
    
    # Additional sanitization using bleach for deeper protection
    sanitized_cpf = bleach.clean(escaped_cpf)
    
    # Get challenges and sanitize challenge titles
    raw_challenges = get_challenges_for_candidate(cpf)
    sanitized_challenges = [(html.escape(title), score) for title, score in raw_challenges]
    
    # Create response with CSP headers
    response = Response(
        render_template(
            'challenge_results.html',  # Using a pre-defined template file instead of template string
            cpf=sanitized_cpf,
            challenges=sanitized_challenges
        )
    )
    
    # Add Content Security Policy headers
    response.headers['Content-Security-Policy'] = "default-src 'self'; script-src 'self'; object-src 'none';"
    
    return response
