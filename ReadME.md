# Smart AI-Based Resume Parser

## Overview
Smart AI-Based Resume Parser is a Django-based web application that automates resume screening. Using Artificial Intelligence (AI) and Natural Language Processing (NLP), it extracts structured data from resumes—such as skills, experience, and education—and matches candidates to job requirements with high accuracy. The system aims to streamline recruitment by reducing processing time, minimizing bias, and improving shortlisting efficiency.

## Features
- **Resume Upload**: Supports multiple file formats (PDF, DOCX, scanned documents).
- **AI-Powered Parsing**: Extracts structured data (personal details, skills, experience, education) using Named Entity Recognition (NER) and deep learning.
- **Keyword & Contextual Matching**: Filters resumes based on job-specific keywords and semantic understanding.
- **Experience & Education Filtering**: Shortlists candidates by minimum experience and relevant qualifications.
- **Candidate Ranking**: Ranks resumes based on job description compatibility.
- **Bias Reduction**: Minimizes human bias in the shortlisting process.
- **Scalable Deployment**: Built for integration with HR systems and large-scale recruitment.

## Installation

### Prerequisites
Ensure you have the following installed:
- Python 3.x
- Django
- Dependencies listed in `requirements.txt`

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/obaidullah72/cv_shortlister.git
   cd smart-ai-resume-parser
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: `env\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```bash
   python manage.py migrate
   ```

5. Start the server:
   ```bash
   python manage.py runserver
   ```

6. Access the app at `http://127.0.0.1:8000/`.

## Usage

### Uploading a Resume
- Navigate to the homepage and upload a resume file (PDF, DOCX, or scanned document).
- The system processes the file and stores extracted data in the database.

### Filtering & Ranking Resumes
- Go to the filtering page.
- Enter job-specific criteria (e.g., keywords, minimum experience, education level).
- Click "Filter" to view shortlisted and ranked resumes.

## Project Structure
```
smart-ai-resume-parser/
├── env/                     # Virtual environment (if applicable)
├── server/                  # Django project
│   ├── cv_shortlister/      # Main Django app
│   │   ├── migrations/      # Database migrations
│   │   ├── templatetags/    # Custom template tags
│   │   ├── __init__.py      # Marks this as a package
│   │   ├── admin.py         # Admin panel configuration
│   │   ├── apps.py          # App configuration
│   │   ├── models.py        # Database models (Resume, etc.)
│   │   ├── tasks.py         # Asynchronous tasks (if using Celery)
│   │   ├── tests.py         # Unit tests
│   │   ├── urls.py          # App-specific URL routing
│   │   ├── utils.py         # Helper functions (AI parsing, etc.)
│   │   ├── views.py         # Handles requests & responses
│   ├── cv_shortlister/      # Main Django app
│   │   ├── settings.py          # Django project settings
│   │   ├── urls.py              # Global URL routing
│   │   ├── asgi.py              # ASGI entry point (if using)
│   │   ├── wsgi.py              # WSGI entry point
├── media/                   # Uploaded resumes and files
├── templates/               # Global HTML templates
│   ├── cv_list.html         # Resume listing page
│   ├── filter.html          # Filtering interface
│   ├── index.html           # Homepage
│   ├── results.html         # Filtered results display
│   ├── upload.html          # Resume upload form
├── db.sqlite3               # SQLite database file
├── manage.py                # Django management script
├── .gitignore               # Git ignored files
├── model-install.txt        # AI model installation instructions (if applicable)

```

## Dependencies
- `django` - Web framework
- `python-docx` - DOCX file parsing
- `pdfplumber` - PDF file parsing
- `pytesseract` - OCR for scanned documents
- `transformers` - BERT and NLP models
- `spacy` - Named Entity Recognition (NER)

Install all dependencies with:
```bash
pip install -r requirements.txt
```

## License
This project is licensed under the MIT License.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for suggestions or improvements.

## Contact
For questions or feedback, reach out at [your.email@example.com].
