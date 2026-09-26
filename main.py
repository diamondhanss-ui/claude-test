"""
Simple Python Project
A basic starting point for a Python application.
"""

def greet(name: str) -> str:
    """Return a greeting message."""
    return f"Hello, {name}!"


def main():
    """Main entry point of the application."""
    print(greet("World"))
    print("Welcome to your simple Python project!")


if __name__ == "__main__":
    main()
