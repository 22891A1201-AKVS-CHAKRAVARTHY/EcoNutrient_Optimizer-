# Crop Yield Predictor

A Django-based web application that provides AI-powered crop yield recommendations using Google's Generative AI (Gemini). This application helps farmers and agricultural researchers make informed decisions about crop cultivation by providing personalized recommendations based on crop type and soil conditions.

## Features

* **AI-Powered Recommendations**: Utilizes Google's Gemini AI model to provide intelligent crop yield suggestions
* **Interactive Web Interface**: User-friendly form with autocomplete functionality for soil types
* **Comprehensive Analysis**: Provides detailed recommendations including:
    * Optimal NPK levels and soil pH
    * Fertilizer recommendations (organic and inorganic)
    * Companion planting suggestions
    * Alternative crop recommendations
* **Responsive Design**: Beautiful, mobile-friendly interface with farm-themed background
* **Real-time Processing**: Instant AI-generated recommendations

## Technology Stack

* **Backend**: Django 5.1.3 (Python)
* **AI Integration**: Google Generative AI (Gemini 1.5 Flash)
* **Database**: SQLite (default Django setup)
* **Frontend**: HTML5, CSS3, JavaScript
* **Template Engine**: Django Template Language
* **Markdown Support**: For formatted AI responses

## Project Structure

```
├── crop_yield_app/
│   ├── crop/                      # Main Django app
│   │   ├── migrations/
│   │   │   └── 0001_initial.py
│   │   ├── apps.py
│   │   ├── forms.py               # Form definitions
│   │   ├── models.py              # Database models
│   │   ├── urls.py                # URL routing
│   │   └── views.py               # Business logic
│   ├── crop_yield_app/            # Project configuration
│   │   ├── asgi.py
│   │   ├── settings.py            # Django settings
│   │   ├── urls.py                # Main URL configuration
│   │   └── wsgi.py
│   ├── templates/crop/
│   │   └── predict.html           # Main template
│   ├── manage.py                  # Django management script
│   └── requirements.txt           # Project dependencies
├── myenv/                         # Virtual environment
└── requirements.txt               # Global requirements
```

## Getting Started

### Prerequisites

* Python 3.8 or higher
* pip (Python package installer)
* Google Generative AI API key

### Installation

1. **Clone the repository**

``` bash
git clone https://github.com/22891A1201-AKVS-CHAKRAVARTHY/EcoNutrient_Optimizer-.git
```

2. **Set up virtual environment**

``` bash
# Windows
python -m venv myenv
myenv\Scripts\activate

# macOS/Linux
python3 -m venv myenv
source myenv/bin/activate
```

3. **Install dependencies**

``` bash
cd crop_yield_app
pip install -r requirements.txt
```

4. **Configure Google AI API**

``` python
genai.configure(api_key="YOUR_API_KEY_HERE")
```

* Get your API key from [Google AI Studio](https://makersuite.google.com/app/apikey)
    * Replace the API key in `crop/views.py`:
5. **Set up the database**

``` bash
python manage.py makemigrations
python manage.py migrate
```

6. **Run the development server**

``` bash
python manage.py runserver
```

7. **Access the application**
Open your browser and navigate to `http://127.0.0.1:8000/`

## Configuration

### Environment Variables (Recommended)

For production deployment, consider using environment variables for sensitive data:

1. Create a `.env` file in the project root
2. Add your configuration:

```
GOOGLE_AI_API_KEY=your_api_key_here
SECRET_KEY=your_django_secret_key
DEBUG=False
```

3. Update `views.py` to use environment variables:

``` python
import os
genai.configure(api_key=os.getenv('GOOGLE_AI_API_KEY'))
```

### Database Configuration

The project uses SQLite by default. For production, consider using PostgreSQL or MySQL:

``` python
# In settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

## Usage

1. **Access the Application**: Open your browser and go to the running server URL
2. **Enter Crop Information**:
    * Type the crop name (e.g., "Rice", "Wheat", "Corn")
    * Select or type the soil type (autocomplete available)
3. **Get Recommendations**: Click "Get Recommendations" to receive AI-powered advice
4. **Review Results**: The AI will provide structured recommendations including:
    * Optimal growing conditions
    * Fertilizer suggestions
    * Companion plants
    * Alternative crops

## Features in Detail

### Supported Soil Types

* Clay Soil
* Sandy Soil
* Silty Soil
* Loamy Soil
* Peaty Soil
* Chalky Soil
* Black Soil
* Red Soil
* Alluvial Soil
* Arid Soil
* Laterite Soil

### AI Recommendations Include

* **Optimal NPK Levels**: Nitrogen, Phosphorus, and Potassium recommendations
* **Soil pH Requirements**: Target pH levels for optimal growth
* **Fertilizer Suggestions**: Both organic and inorganic options
* **Companion Planting**: Plants that grow well together
* **Alternative Crops**: Better suited crops for your soil type

## Development

### Adding New Features

1. **Models**: Add new data models in `crop/models.py`
2. **Forms**: Create forms in `crop/forms.py`
3. **Views**: Add business logic in `crop/views.py`
4. **Templates**: Create HTML templates in `templates/crop/`
5. **URLs**: Configure routing in `crop/urls.py`

### Running Tests

``` bash
python manage.py test
```

### Code Style

The project follows PEP8 Python coding standards. Use tools like `black` or `flake8` for code formatting:

``` bash
pip install black flake8
black .
flake8 .
```

## Dependencies

* **django**: Web framework
* **google-generativeai**: Google AI integration
* **markdown**: Markdown processing for formatted responses

## License

This project is open source and available under the [MIT License](LICENSE).
