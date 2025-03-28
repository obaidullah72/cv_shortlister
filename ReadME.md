# CV Shortlister

## Overview
CV Shortlister is a Django-based web application that allows users to upload resumes and filter them based on experience, education, and skills. The system extracts text from uploaded resumes and matches them against specified criteria to shortlist the most relevant candidates.

## Features
- **Upload CVs**: Users can upload CV files (PDF, DOCX, etc.).
- **Keyword-Based Filtering**: Shortlists CVs based on specific keywords (skills, job titles, etc.).
- **Experience Matching**: Filters candidates based on minimum required experience.
- **Education Filtering**: Identifies candidates with relevant degrees or qualifications.
- **Shortlisted Results**: Displays shortlisted CVs for further review.

## Installation

### Prerequisites
Ensure you have the following installed:
- Python 3.x
- Django
- Dependencies from `requirements.txt`

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/obaidullah72/cv_shortlister.git
   cd cv_shortlister
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
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

6. Access the app in your browser at `http://127.0.0.1:8000/`.

## Usage

### Uploading a CV
- Navigate to the homepage and upload a CV file.
- The file will be stored in the database.

### Filtering CVs
- Go to the filtering page.
- Enter keywords, minimum experience, and education requirements.
- Click "Filter" to get a list of matching CVs.

## Project Structure
```
cv-shortlister/
├── server/  # Django project
│   ├── main_app/  # Main Django app
│   │   ├── templates/  # HTML templates
│   │   ├── views.py  # Handles upload & filtering logic
│   │   ├── models.py  # CV model
│   │   ├── utils.py  # Text extraction logic
│   ├── settings.py  # Django settings
│   ├── urls.py  # URL routing
├── manage.py  # Django entry point
├── requirements.txt  # Dependencies
├── README.md  # Project documentation
```

## Dependencies
- Django
- Python-docx (for .docx parsing)
- pdfplumber (for PDF parsing)

Install all dependencies with:
```bash
pip install -r requirements.txt
```

## License
This project is licensed under the MIT License.

## Contributing
Feel free to open issues or submit pull requests for improvements.

## Contact
For questions or feedback, reach out at [your.email@example.com].

