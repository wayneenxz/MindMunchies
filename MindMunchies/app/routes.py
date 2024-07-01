from flask import Blueprint, render_template, redirect, url_for, flash, request, abort
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from app.models import User, Flashcard
from app.forms import RegistrationForm, LoginForm, FlashcardForm
from app import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='pbkdf2:sha256', salt_length=8)
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('main.login'))
    return render_template('register.html', form=form)

@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('main.flashcards'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', form=form)

@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))

@main.route('/flashcard/new', methods=['GET', 'POST'])
@login_required
def new_flashcard():
    form = FlashcardForm()
    if form.validate_on_submit():
        flashcard = Flashcard(question=form.question.data, answer=form.answer.data, author=current_user)
        db.session.add(flashcard)
        db.session.commit()
        flash('Your flashcard has been created!', 'success')
        return redirect(url_for('main.flashcards'))
    return render_template('create_flashcard.html', title='New Flashcard', form=form, legend='New Flashcard')

import random

@main.route('/flashcards')
@login_required
def flashcards():
    flashcards = Flashcard.query.filter_by(author=current_user).all()
    total_flashcards = len(flashcards)
    tested_flashcards = Flashcard.query.filter_by(author=current_user, tested=True).count()
    correct_answers = Flashcard.query.filter_by(author=current_user, correct=True).count()
    progress = int((tested_flashcards / total_flashcards) * 100) if total_flashcards > 0 else 0

    random.shuffle(flashcards)  # Shuffle the flashcards

    return render_template('flashcards.html', flashcards=flashcards, progress=progress, total_flashcards=total_flashcards, tested_flashcards=tested_flashcards, correct_answers=correct_answers)



@main.route('/flashcard/test/<int:flashcard_id>', methods=['GET', 'POST'])
@login_required
def test_flashcard(flashcard_id):
    flashcard = Flashcard.query.get_or_404(flashcard_id)
    flashcards = Flashcard.query.filter_by(author=current_user).all()
    total_flashcards = len(flashcards)
    current_flashcard_index = next((index for (index, d) in enumerate(flashcards) if d.id == flashcard_id), None)
    next_flashcard_id = flashcards[
        current_flashcard_index + 1].id if current_flashcard_index < total_flashcards - 1 else None

    if request.method == 'POST':
        user_answer = request.form['answer']
        if user_answer.strip().lower() == flashcard.answer.strip().lower():
            flash('Correct!', 'success')
            flashcard.correct = True
        else:
            flash('Incorrect. The correct answer is: ' + flashcard.answer, 'danger')
            flashcard.correct = False
        flashcard.tested = True
        db.session.commit()
        return redirect(url_for('main.test_flashcard', flashcard_id=flashcard.id))

    return render_template('test_flashcard.html', title='Test Flashcard', flashcard=flashcard,
                           next_flashcard_id=next_flashcard_id, current_flashcard=current_flashcard_index + 1,
                           total_flashcards=total_flashcards)



@main.route('/flashcard/delete/<int:flashcard_id>', methods=['POST'])
@login_required
def delete_flashcard(flashcard_id):
    flashcard = Flashcard.query.get_or_404(flashcard_id)
    if flashcard.author != current_user:
        abort(403)
    db.session.delete(flashcard)
    db.session.commit()
    flash('Your flashcard has been deleted!', 'success')
    return redirect(url_for('main.flashcards'))

@main.route('/flashcard/<int:flashcard_id>')
@login_required
def flashcard(flashcard_id):
    flashcard = Flashcard.query.get_or_404(flashcard_id)
    return render_template('flashcard.html', flashcard=flashcard, name=current_user.username)

@main.route('/progress')
@login_required
def progress():
    total_flashcards = Flashcard.query.count()
    tested_flashcards = Flashcard.query.filter_by(tested=True).count()
    progress_percentage = (tested_flashcards / total_flashcards) * 100 if total_flashcards > 0 else 0
    return render_template('progress.html', progress=progress_percentage)

# Add this route for deleting all flashcards
@main.route('/flashcards/delete_all', methods=['POST'])
@login_required
def delete_all_flashcards():
    flashcards = Flashcard.query.filter_by(author=current_user).all()
    for flashcard in flashcards:
        db.session.delete(flashcard)
    db.session.commit()
    flash('All flashcards have been deleted.', 'success')
    return redirect(url_for('main.flashcards'))