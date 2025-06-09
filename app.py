from flask import Flask, render_template_string, request, redirect, url_for
import os
import uuid

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploaded'

# Базовый шаблон для всех страниц
def base_template(content, title="Rally mix"):
    return f'''
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>{title} </title>
        <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🏁</text></svg>">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
    </head>
    <body>
        <!-- Навигационное меню -->
        <nav class="navbar navbar-expand-lg navbar-dark bg-dark mb-4">
            <div class="container">
                <a class="navbar-brand" href="/">Rally cars</a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarNav">
                    <ul class="navbar-nav">
                        <li class="nav-item"><a class="nav-link" href="/about">About</a></li>
                        <li class="nav-item"><a class="nav-link" href="/image">Images</a></li>
                        <li class="nav-item"><a class="nav-link" href="/bootstrap">Bootstrap</a></li>
                        <li class="nav-item"><a class="nav-link" href="/form">Select Form</a></li>
                        <li class="nav-item"><a class="nav-link" href="/upload">Upload file</a></li>
                        <li class="nav-item"><a class="nav-link" href="/gallery">Gallery</a></li>
                        <li class="nav-item"><a class="nav-link" href="/archive/audi/400/8">Archive</a></li>
                    </ul>
                </div>
            </div>
        </nav>

        <!-- Основной контент -->
        <div class="container">
            {content}
        </div>

        <!-- Футер -->
        <footer class="bg-light text-center py-3 mt-5">
            <div class="container">
                <p class="mb-0">© 2025 rally 0.0</p>
            </div>
        </footer>

        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    </body>
    </html>
    '''

@app.route('/')
def home():
    content = '''
    <h1 class="mb-4 text-center">Rally mega mix</h1>
    
    <div class="alert alert-info">
        <p class="text-center mb-0">Welcome to rally temple!</p>
    </div>

    <!-- Быстрый доступ к разделам -->
    <div class="row mt-5">
        <!-- Карточка 1 -->
        <div class="col-md-4 mb-4">
            <div class="card h-100 text-center">
                <div class="card-body">
                    <h5 class="card-title">Cars</h5>
                    <p class="card-text">Get known about rally cars</p>
                    <a href="/choice/cat" class="btn btn-primary">More...</a>
                </div>
            </div>
        </div>
        
        <!-- Карточка 2 -->
        <div class="col-md-4 mb-4">
            <div class="card h-100 text-center">
                <div class="card-body">
                    <h5 class="card-title">Drivers</h5>
                    <p class="card-text">Best drivers of all time</p>
                    <a href="/choice/dog" class="btn btn-primary">More...</a>
                </div>
            </div>
        </div>
        
        <!-- Карточка 3 -->
        <div class="col-md-4 mb-4">
            <div class="card h-100 text-center">
                <div class="card-body">
                    <h5 class="card-title">Tracks and stages</h5>
                    <p class="card-text">Legendary stages of rally races</p>
                    <a href="/choice/hamster" class="btn btn-primary">More...</a>
                </div>
            </div>
        </div>
    </div>

    <!-- Горизонтальные кнопки-ссылки -->
    <div class="d-flex justify-content-center flex-wrap gap-3 mt-4">
        <a href="/image" class="btn btn-outline-primary">Images</a>
        <a href="/form" class="btn btn-outline-success">Select form</a>
        <a href="/gallery" class="btn btn-outline-info">Gallery</a>
        <a href="/upload" class="btn btn-outline-warning">Upload</a>
    </div>
    '''
    return render_template_string(base_template(content))

# Страница "О проекте"
@app.route('/about')
def about():
    content = '''
        <h1 class="mb-4">About "Rally mega mix"</h1>
        <div class="card">
            <div class="card-body">
                <p class="card-text">This website is about best thing in the world - rally</p>
                <p>We tell you about cars, drivers, tracks and emtions.</p>
                <p>It's not only about dust and oil smell, but about mindset and soul of rally</p>
            </div>
        </div>
    '''
    return render_template_string(base_template(content, "About"))

# Страница с изображением
@app.route('/image')
def image():
    content = '''
<h1 class="mb-4">My favourite image</h1>
        <div class="text-center">
            <img src="{{ url_for('static', filename='img/2.jpg') }}" class="img-fluid rounded" alt="rally" style="max-height: 1000px;">
            <p class="mt-3">Beautiful car on a beautiful road</p>
        </div>
    '''
    return render_template_string(base_template(content, "Rally car"))

# Страница с Bootstrap компонентами (сохраняем оригинальный стиль)
@app.route('/bootstrap')
def bootstrap():
    content = '''
        <h1 class="text-center my-header">Legend car</h1>
        
        <!-- Цитата -->
        <blockquote class="blockquote text-center">
            <p>Audi legend that broke records</p>
        </blockquote>
        
        <!-- Карточка -->
        <div class="card mx-auto" style="width: 18rem;">
            <img src="{{ url_for('static', filename='img/audi.jpg') }}" class="card-img-top" alt="Котик">
            <div class="card-body">
                <h5 class="card-title">Audi sport s1 quatro</h5>
                <p class="card-text">Car that changed the rules</p>
                <a href="/" class="btn btn-primary">Main</a>
            </div>
        </div>
        
        <!-- Alert -->
        <nav class="navbar navbar-expand-lg navbar-dark bg-secondary mb-4">
            Subscribe to us
        </div>
    '''
    return render_template_string(base_template(content, "Bootstrap components"))

# Страница с формой
@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        car_brand = request.form.get('car_brand')
        return redirect(url_for('choice', name=car_brand))
    
    content = '''
        <h1 class="mb-4">Car choose form</h1>
        <form method="POST" class="bg-light p-4 rounded">
            <div class="mb-3">
                <label for="car_brand" class="form-label">Car brand</label>
                <select class="form-select" id="car_brand" name="car_brand" required>
                    <option value="">Choose car</option>
                    <option value="audi">Audi</option>
                    <option value="toyota">Toyota</option>
                    <option value="mitsubishi">Mitsubishi</option>
                    <option value="chevrolet">Chevrolet</option>
                </select>
            </div>
            
            <div class="mb-3">
                <label for="team_number" class="form-label">Team number</label>
                <input type="text" class="form-control" id="team_number" name="team_number" required>
            </div>
            
            <div class="mb-3">
                <label for="email" class="form-label">Email:</label>
                <input type="email" class="form-control" id="email" name="email" required>
            </div>
            
            <div class="mb-3">
                <label class="form-label">Experience</label>
                <div class="form-check">
                    <input class="form-check-input" type="radio" name="experience" id="exp1" value="none" checked>
                    <label class="form-check-label" for="exp1">No experience</label>
                </div>
                <div class="form-check">
                    <input class="form-check-input" type="radio" name="experience" id="exp2" value="some">
                    <label class="form-check-label" for="exp2">1-3 years</label>
                </div>
                <div class="form-check">
                    <input class="form-check-input" type="radio" name="experience" id="exp3" value="much">
                    <label class="form-check-label" for="exp3">3+ years</label>
                </div>
            </div>
            
            <div class="mb-3">
                <label class="form-label">Transmission</label>
                <div class="form-check">
                    <input class="form-check-input" type="checkbox" name="features" id="feature1" value="fwd">
                    <label class="form-check-label" for="feature1">FWD</label>
                </div>
                <div class="form-check">
                    <input class="form-check-input" type="checkbox" name="features" id="feature2" value="rwd">
                    <label class="form-check-label" for="feature2">RWD</label>
                </div>
                <div class="form-check">
                    <input class="form-check-input" type="checkbox" name="features" id="feature3" value="awd">
                    <label class="form-check-label" for="feature3">AWD</label>
                </div>
            </div>
            
            <button type="submit" class="btn btn-primary">Send</button>
        </form>
    '''
    return render_template_string(base_template(content, "Select form"))

# Страница выбора
@app.route('/choice/<name>')
def choice(name):
    descriptions = {
        'audi': ('Audi', 'German clegends'),
        'toyota': ('Toyota', 'Good japanese car'),
        'mitsubishi': ('Mitsubishi', 'Good reliable cars'),
        'chevrolet': ('Chevrolet', 'Good american car')
    }
    
    title, description = descriptions.get(name, ('Unkwonw car', 'no information'))
    
    content = f'''
        <div class="alert alert-info">
            <h1>You chose: {title}</h1>
            <p>{description}</p>
        </div>
        '''
        # <div class="card">
        #     <div class="card-body">
        #         <h2 class="card-title">Почему {title} - отличный выбор?</h2>
        #         <ul class="list-group">
        #             <li class="list-group-item">Легко ухаживать</li>
        #             <li class="list-group-item">Подходит для квартиры</li>
        #             <li class="list-group-item">Дружелюбный характер</li>
        #         </ul>
        #     </div>
        # </div>
    # '''
    return render_template_string(base_template(content, f"Chosen: {title}"))

# Страница архива
@app.route('/archive/<name>/<int:number1>/<int:number2>')
def archive(name, number1, number2):
    result = number1 * number2
    content = f'''
        <div class="jumbotron">
            <h1 class="display-4">Archive: {name.capitalize()}</h1>
            <p class="lead">Statistics</p>
            <hr class="my-4">
            <p>Horsepowers: {number1} hpw</p>
            <p>Championships: {number2} 🏆</p>
            <p>Winability: {result}</p>
        </div>
        
        <div class="progress mt-3">
            <div class="progress-bar" role="progressbar" style="width: {number1*10}%" 
                aria-valuenow="{number1}" aria-valuemin="0" aria-valuemax="10">
                Popularity: {number1}/10
            </div>
        </div>
    '''
    return render_template_string(base_template(content, f"АArchive: {name}"))

# Страница загрузки фото
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['photo']
        if file and allowed_file(file.filename):
            # Генерируем уникальное имя файла
            filename = str(uuid.uuid4()) + '.jpg'
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('upload'))
    
    # Получаем список всех загруженных изображений
    uploaded_files = []
    for f in os.listdir(app.config['UPLOAD_FOLDER']):
        if f.endswith('.jpg'):
            uploaded_files.append(f)
    
    content = '''
        <h1 class="text-center">Upload your car photo</h1>
        <form method="POST" enctype="multipart/form-data" class="mt-4">
            <div class="mb-3">
                <label for="photo" class="form-label">Choose file:</label>
                <input class="form-control" type="file" id="photo" name="photo" accept="image/*" required>
            </div>
            <button type="submit" class="btn btn-primary">Upload</button>
        </form>
        
        {% if uploaded_files %}
        <div class="mt-4">
            <h3 class="text-center">Your uploaded photos:</h3>
            <div class="row">
                {% for file in uploaded_files %}
                <div class="col-md-4 mb-3">
                    <img src="{{ url_for('static', filename='uploaded/' + file) }}" class="img-thumbnail uploaded-photo" alt="Загруженное фото">
                </div>
                {% endfor %}
            </div>
        </div>
        {% endif %}
    '''
    return render_template_string(base_template(content, "Upload photo"), uploaded_files=uploaded_files)

# Галерея
@app.route('/gallery')
def gallery():
    content = '''
        <h1 class="text-center mb-4">Little gallery</h1>
        
        <div id="petCarousel" class="carousel slide" data-bs-ride="carousel" style="max-width: 600px; margin: 0 auto;">
            <div class="carousel-inner">
                <div class="carousel-item active">
                    <img src="{{ url_for('static', filename='img/1.jpg') }}" class="d-block w-100" style="max-height: 400px; object-fit: contain;" alt="Кошка">
                </div>
                <div class="carousel-item">
                    <img src="{{ url_for('static', filename='img/2.jpg') }}" class="d-block w-100" alt="Собака">
                </div>
                <div class="carousel-item">
                    <img src="{{ url_for('static', filename='img/3.webp') }}" class="d-block w-100" alt="Хомяк">
                </div>
            </div>
            <button class="carousel-control-prev" type="button" data-bs-target="#petCarousel" data-bs-slide="prev">
                <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                <span class="visually-hidden">Previous</span>
            </button>
            <button class="carousel-control-next" type="button" data-bs-target="#petCarousel" data-bs-slide="next">
                <span class="carousel-control-next-icon" aria-hidden="true"></span>
                <span class="visually-hidden">Next</span>
            </button>
        </div>
    '''
    return render_template_string(base_template(content, "Gallery"))

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'jpg', 'jpeg', 'png', 'gif'}

if __name__ == '__main__':
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug=True)