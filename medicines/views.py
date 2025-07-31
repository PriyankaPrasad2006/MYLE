from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from .forms import MedicineForm
from .models import Medicine
import qrcode
from io import BytesIO
import base64


def home(request):
    """Home page view."""
    recent_medicines = Medicine.objects.all()[:5]
    return render(request, 'medicines/home.html', {'recent_medicines': recent_medicines})


def create_medicine_qr(request):
    """Create medicine and generate QR code."""
    if request.method == 'POST':
        form = MedicineForm(request.POST)
        if form.is_valid():
            medicine = form.save()
            messages.success(request, f'Medicine "{medicine.name}" added successfully!')
            return redirect('medicines:qr_code_display', pk=medicine.pk)
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = MedicineForm()
    
    return render(request, 'medicines/medicine_form.html', {'form': form})


def qr_code_display(request, pk):
    """Display the QR code for a specific medicine."""
    medicine = get_object_or_404(Medicine, pk=pk)
    qr_data = medicine.get_qr_data()

    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(qr_data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    # Convert image to base64 for embedding in HTML
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    qr_code_base64 = base64.b64encode(buffer.getvalue()).decode()

    return render(request, 'medicines/qr_code_display.html', {
        'medicine': medicine,
        'qr_code_base64': qr_code_base64
    })


def medicine_list(request):
    """Display list of all medicines."""
    medicines = Medicine.objects.all()
    return render(request, 'medicines/medicine_list.html', {'medicines': medicines})


@require_POST
def delete_medicine(request, pk):
    """Delete a specific medicine."""
    medicine = get_object_or_404(Medicine, pk=pk)
    medicine_name = medicine.name
    medicine.delete()
    messages.success(request, f'Medicine "{medicine_name}" has been deleted successfully!')
    return redirect('medicines:medicine_list')


@require_POST
def delete_all_medicines(request):
    """Delete all medicines."""
    count = Medicine.objects.count()
    Medicine.objects.all().delete()
    messages.success(request, f'All {count} medicines have been deleted successfully!')
    return redirect('medicines:medicine_list')


def download_qr_code(request, pk):
    """Download QR code as PNG file."""
    medicine = get_object_or_404(Medicine, pk=pk)
    qr_data = medicine.get_qr_data()

    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(qr_data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    # Create HTTP response with image
    response = HttpResponse(content_type="image/png")
    response['Content-Disposition'] = f'attachment; filename="qr_code_{medicine.batch_number}.png"'
    img.save(response, "PNG")
    
    return response
