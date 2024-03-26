from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World from Shreya Gupta! This is my first code change.'


@app.route('/hello')
def hello_template():  # Renamed from hello
    return render_template('hello.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/about-css')
def about_css():
    return render_template('about-css.html')


@app.route('/favorite-course', methods=['GET'])
def favorite_course():
    subject = request.args.get('subject', 'BMGT')
    course_number = request.args.get('course_number', '407')
    print('subject entered', subject)
    print('course_number entered', course_number)
    return render_template('favorite-course.html', subject=subject, course_number=course_number)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        return render_template('contact.html', form_submitted=True)
    else:
        return render_template('contact.html')


if __name__ == '__main__':
    app.run()