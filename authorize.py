from flask_login import current_user
from flask import render_template, flash, current_app
from functools import wraps

def role_required(roles):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Checking if current_user exists and has the required role
            if current_user and current_user.role in roles:
                pass  # User has permission, do nothing
            else:
                # User does not have permission, show error message and render access denied template
                flash('You do not have permission to access this function.', 'error')
                return render_template('access_denied.html')

            # Checking if current_app has ensure_sync attribute callable and using it if present
            if callable(getattr(current_app, "ensure_sync", None)):
                return current_app.ensure_sync(func)(*args, **kwargs)
            return func(*args, **kwargs)  # Returning the original function

        return wrapper  # Returning the wrapper function

        return decorator  # Returning the decorator function