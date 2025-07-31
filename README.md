
# Medicine QR Code Generator

A Django web application that allows users to input medicine data and generate unique QR codes containing the medicine information for better tracking and verification.

## Features

- **Medicine Data Input**: User-friendly form to enter medicine details (name, batch number, manufacturing date, expiry date, manufacturer)
- **QR Code Generation**: Dynamically create unique QR codes based on submitted data
- **QR Code Display**: View generated QR codes with medicine information
- **Data Storage**: Save medicine data in SQLite database
- **QR Code Download**: Download QR codes as PNG files
- **Print Functionality**: Print QR codes for physical labeling
- **Responsive Design**: Modern Bootstrap-based UI that works on all devices
- **Admin Interface**: Django admin panel for managing medicines
- **Data Validation**: Form validation including expiry date checks

## Installation

1. **Clone or download the project**
   ```bash
   git clone <repository-url>
   cd medicine_qr_app
   ```

2. **Create virtual environment** (already done if using the provided setup)
   ```bash
   python -m venv .venv
   ```

3. **Activate virtual environment**
   - Windows: `.venv\Scripts\activate`
   - macOS/Linux: `source .venv/bin/activate`

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create superuser** (optional)
   ```bash
   python manage.py createsuperuser
   ```

7. **Run development server**
   ```bash
   python manage.py runserver
   ```

8. **Access the application**
   - Main App: http://127.0.0.1:8000/
   - Admin Panel: http://127.0.0.1:8000/admin/

## Usage

### Adding a New Medicine

1. Navigate to the home page
2. Click "Add New Medicine" or go to `/create/`
3. Fill in the required fields:
   - Medicine Name
   - Batch Number (must be unique)
   - Manufacturing Date
   - Expiry Date
   - Manufacturer
4. Click "Generate QR Code"
5. View the generated QR code with medicine details

### Managing Medicines

- **View All Medicines**: Click "View All" to see a list of all registered medicines
- **View QR Code**: Click the QR icon next to any medicine in the list
- **Download QR Code**: Click "Download QR Code" to save as PNG file
- **Print QR Code**: Use the print button for physical printing
- **Delete Medicine**: Click the trash icon to delete individual medicines
- **Delete All Medicines**: Use "Delete All" button to clear all medicines (with confirmation)

### QR Code Content

Each QR code contains the following information:
```
Medicine: [Medicine Name]
Batch: [Batch Number]
Mfg Date: [Manufacturing Date]
Exp Date: [Expiry Date]
Manufacturer: [Manufacturer Name]
```

## Project Structure

```
medicine_qr_app/
├── manage.py
├── medicine_qr_app/          # Main project directory
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── medicines/                # Django app for medicine functionalities
│   ├── migrations/
│   ├── templates/medicines/  # HTML templates
│   ├── __init__.py
│   ├── admin.py             # Admin configuration
│   ├── apps.py
│   ├── models.py            # Medicine model
│   ├── forms.py             # Medicine input form
│   ├── urls.py              # App-specific URLs
│   └── views.py             # Business logic
├── static/                  # Static files (CSS, JS, images)
├── media/                   # User uploads (auto-created)
├── .venv/                   # Virtual environment
├── requirements.txt         # Project dependencies
└── README.md               # This file
```

## Key Files

- **`medicines/models.py`**: Defines the Medicine model with QR data generation
- **`medicines/forms.py`**: Form handling with validation
- **`medicines/views.py`**: QR code generation and business logic
- **`medicines/templates/`**: HTML templates with Bootstrap styling
- **`requirements.txt`**: Project dependencies

## Dependencies

- **Django 5.2+**: Web framework
- **qrcode[pil]**: QR code generation library
- **Pillow**: Image processing (required by qrcode)

## Development

### Adding New Features

1. **Models**: Add new fields to `Medicine` model in `models.py`
2. **Forms**: Update `MedicineForm` in `forms.py`
3. **Views**: Add new views in `views.py`
4. **Templates**: Create/update HTML templates
5. **URLs**: Add URL patterns in `urls.py`

### Database Operations

```bash
# Create migrations after model changes
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Access Django shell
python manage.py shell
```

### Admin Interface

Access the Django admin at `/admin/` to:
- View all medicines
- Add/edit/delete medicines directly
- Export data
- Manage users

## Security Notes

- Change `SECRET_KEY` in production
- Set `DEBUG = False` in production
- Configure `ALLOWED_HOSTS` for production
- Use environment variables for sensitive settings
- Set up proper database (PostgreSQL/MySQL) for production

## Troubleshooting

### Common Issues

1. **QR Code not displaying**: Check that Pillow is properly installed
2. **Form validation errors**: Ensure expiry date is after manufacturing date
3. **Batch number conflicts**: Each batch number must be unique
4. **Static files not loading**: Run `python manage.py collectstatic`
5. **"View All" button not working**:
   - Check that the server is running on <http://127.0.0.1:8000/>
   - Ensure sample data exists (run `python manage.py create_sample_data`)
   - Verify URL configuration in `medicines/urls.py`
6. **Empty medicine list**: Create sample data with `python manage.py create_sample_data`

### Testing the Application

1. **Create sample data**:

   ```bash
   # Create sample data (clears existing data first)
   python manage.py create_sample_data
   
   # Create sample data without clearing existing data
   python manage.py create_sample_data --clear
   
   # Clear all medicines
   python manage.py clear_medicines
   
   # Force clear without confirmation
   python manage.py clear_medicines --force
   ```

2. **Access different pages**:
   - Home: <http://127.0.0.1:8000/>
   - Add Medicine: <http://127.0.0.1:8000/create/>
   - View All Medicines: <http://127.0.0.1:8000/list/>
   - Admin Panel: <http://127.0.0.1:8000/admin/>

### Debug Mode

If you encounter issues, check:

- Console logs in browser developer tools
- Django logs in terminal
- Database content via admin panel

## Future Enhancements

- User authentication and authorization
- QR code scanning for verification
- Bulk medicine import/export
- API endpoints for mobile apps
- Advanced reporting and analytics
- Email notifications for expiring medicines
- Barcode generation support

## License

This project is open source and available under the MIT License.

## Support

For issues and questions, please check the Django documentation or create an issue in the project repository.
#
