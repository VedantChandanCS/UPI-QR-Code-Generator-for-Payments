import qrcode  # For generating QR codes
from PIL import Image, ImageDraw, ImageFont  # For adding text to the QR code

# Take UPI ID as input from the user
upi_id = input("Enter your UPI ID (e.g., name@okhdfcbank): ")

# Ask if the user wants to pre-fill the amount or not
prefill_amount = input("Do you want to pre-fill the amount in the QR code? (yes/no): ").strip().lower()

# Initialize the UPI URL
upi_url = f"upi://pay?pa={upi_id}"

# If the user wants to pre-fill the amount, ask for the amount and add it to the URL
if prefill_amount == "yes":
    amount = input("Enter the amount to be paid (in INR): ")
    upi_url += f"&am={amount}&cu=INR"  # Add the amount and currency to the UPI URL

# Generate the QR code
qr = qrcode.QRCode(
    version=1,  # Size of the QR code
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
    box_size=10,  # Size of each box in the QR code grid
    border=4,  # Border size of the QR code
)

qr.add_data(upi_url)  # Add the UPI URL to the QR code
qr.make(fit=True)

# Create the QR code image
img = qr.make_image(fill_color="black", back_color="white")

# Create a draw object to add text
draw = ImageDraw.Draw(img)

# Choose a font and size (adjust as needed)
try:
    font = ImageFont.truetype("arial.ttf", 25)  # You can replace "arial.ttf" with any font in your system
except IOError:
    font = ImageFont.load_default()

# Define the text to add
text = "Scan to Pay"

# Use textbbox to calculate the text size
bbox = draw.textbbox((0, 0), text, font=font)  # Get bounding box of the text
text_width = bbox[2] - bbox[0]
text_height = bbox[3] - bbox[1]

# Position the text at the upper center of the QR code
text_position = ((img.size[0] - text_width) // 2, 10)  # 10 pixels from the top

# Add the text on the QR code image
draw.text(text_position, text, fill="black", font=font)

# Save the QR code image with the text
img.save("upi_qr_code_with_text.png")

# Display the QR code with text
img.show()

# Print a message depending on whether the amount was pre-filled or not
if prefill_amount == "yes":
    print(f"UPI QR Code generated for UPI ID: {upi_id} with amount: {amount} INR")
else:
    print(f"UPI QR Code generated for UPI ID: {upi_id} without pre-filled amount. The payer can enter the amount manually.")
