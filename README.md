
---

## **UPI QR Code Generator for Payments 💳📱**

**UPI QR Code Generator** is a tool that enables users to generate customized UPI payment QR codes. This project allows you to create a QR code linked to your UPI ID, with the option to pre-fill a payment amount. Additionally, you can add a custom "Scan to Pay" message at the top of the QR code. The generated QR code can be scanned by others to easily make payments, either with or without the pre-filled amount.

---

## **Features ✨**

- 💳 **Generate UPI QR codes** for payments using your UPI ID.
- 💰 **Optional Pre-fill Payment Amount**: Add an amount to be pre-filled when the QR code is scanned.
- 📱 **User-friendly**: Easily input your UPI ID and amount via the command line interface.
- ✍️ **Customizable Text**: Add a "Scan to Pay" message on top of the QR code.
- 🔄 **Instant Payment**: Generate a ready-to-scan QR code for UPI payments.

---

## **Installation 🛠️**

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/UPI-QR-Code-Generator.git
   ```

2. **Install the required libraries**:

   ```bash
   pip install qrcode[pil] Pillow
   ```

---

## **Usage 🚀**

1. **Run the** `upi_qr_generator.py` **script**:

   ```bash
   main.py
   ```

2. A prompt will appear asking for your **UPI ID** and whether you want to pre-fill the **payment amount**.

3. After entering your details, a **QR code** will be generated.

4. The QR code will be saved as an image file (`upi_qr_code.png`), with the **Scan to Pay** text added at the top.

5. You can scan the generated QR code using any UPI-enabled payment app to make the payment.

---

## **How It Works 🧑‍💻**

- The **UPI URL** is formatted as `upi://pay?pa=UPI_ID&am=Amount&cu=INR` to create a link for making payments.
- If an amount is specified, the generated QR code will include the **amount** to be paid.
- The **qrcode** library generates the QR code, while **Pillow** adds a custom text message on top of the QR code.

---

## **Example 🎥**

Once the script is executed and the QR code is generated, you will see an output similar to:

- If an **amount** is provided, the payer will see the amount automatically pre-filled when scanning the QR code.
- If **no amount** is entered, the payer will be able to enter the amount manually after scanning the QR code.

---

## **Customization ⚙️**

- **Custom Text**: The text "Scan to Pay" is added at the top of the QR code image. You can modify this text or adjust its positioning as needed.
- **QR Code Settings**: Customize the size and border of the QR code by modifying the parameters in the code.

```python
qr = qrcode.QRCode(
    version=1,  # QR code size
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
    box_size=10,  # Box size in the QR code
    border=4,  # Border size around the QR code
)
```

---

## **Contributing 🤝**

If you'd like to contribute to this project, feel free to **fork the repository**, create a new branch, and submit a pull request.

We welcome all contributions! 🚀

---
