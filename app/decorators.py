from functools import wraps
from flask import session, url_for, request, redirect

def logged_in(f):
  @wraps(f)
  def decorated_function(*args, **kwargs):
    """A decorator that redirects to the login form if the user is not logged in.
    """
    if 'idToken' in session:
      return f(*args, **kwargs)
    else:
      return redirect(url_for('login'))
  return decorated_function

def not_logged_in(f):
  """A decorator that redirects to index if the user is logged in.
  """
  @wraps(f)
  def decorated_function(*args, **kwargs):
    if 'idToken' in session:
      return redirect(url_for('index'))
    else:
      return f(*args, **kwargs)
  return decorated_function