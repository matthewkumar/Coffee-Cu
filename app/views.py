from flask import render_template, flash, redirect, session, url_for
from requests.exceptions import HTTPError
from app import app, firebase, db, auth
from .forms import LoginForm, SignupForm, ProfileForm
from .decorators import logged_in, not_logged_in


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/signup', methods=['GET', 'POST'])
@not_logged_in
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        try:
            user = auth.create_user_with_email_and_password(form.email.data,
                form.password.data)
            auth.send_email_verification(user['idToken'])

            uid = user['localId']

            userdata = {
                'uid': uid,
                'firstname': form.firstname.data,
                'lastname': form.lastname.data,
                'email': form.email.data,
                'enabled': True
            }
            db.child('users').child(uid).set(userdata, user['idToken'])

            flash('Thanks for signing up! Please verify your email to log in.')
            return redirect(url_for('login'))
        except HTTPError as e:
            # TODO more accurate error reporting -- pyrebase problem?
            #flash('An account already exists for that email address!')
            flash('Account creation failed.')
            print(e)
            return redirect(url_for('signup'))
    else:
        return render_template('signup.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
@not_logged_in
def login():
    form = LoginForm()
    if form.validate_on_submit():
        try:
            user = auth.sign_in_with_email_and_password(form.email.data,
                form.password.data)
            accountInfo = auth.get_account_info(user['idToken'])

            if (not accountInfo['users'][0]['emailVerified']):
                flash('Please verify your email address!')
            else:
                # create new user session
                session['idToken'] = user['idToken']
                uid = accountInfo['users'][0]['localId']
                session['uid'] = uid
                flash('Login complete for uid="%s"' % uid)
        except HTTPError as e:
            flash('Sorry, we couldn\'t find those credentials!')
            print(e)

        return redirect(url_for('index'))
    else:
        return render_template('login.html', title='Sign in', form=form)


@app.route('/edit', methods=['GET', 'POST'])
@logged_in
def edit():
    # TODO prepopulate form with existing profile
    #profile = db.child('profiles').child(session['email']).get(session['idToken']).val()

    form = ProfileForm()
    if form.validate_on_submit():
        new_profile = {
            'school': form.school.data,
            'year': form.year.data,
            'major': form.major.data,
            'about': form.about.data,
            'likes': form.likes.data,
            'contactfor': form.contactfor.data,
            'twitter': form.twitter.data,
            'facebook': form.facebook.data,
            'linkedin': form.linkedin.data,
            'website': form.website.data,
            'make_public': form.make_public.data
        }
        db.child('profiles').child(session['uid']).set(new_profile,
            session['idToken'])
        flash('Profile updated.')
        return redirect('/user/%s' % session['uid'])
    else:
        return render_template('edit.html', form=form)


@app.route('/user/<uid>', methods=['GET'])
@logged_in # eventually only require login if make_public == false
def user(uid):
    try:
        user = db.child('users').child(uid).get(session['idToken']).val()
        profile = db.child('profiles').child(uid).get(session['idToken']).val()
        if user is None or profile is None:
            return render_template('error/404.html')
        else:
            return render_template('user.html', user=user, profile=profile)
    except HTTPError:
        return render_template('error/400.html')


@app.route('/logout')
@logged_in
def logout():
    session.pop('idToken', None) # end user session
    session.pop('uid', None)
    return redirect(url_for('index'))
