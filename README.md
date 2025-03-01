# QR Code Scanner Module for Odoo

## 📌 Overview
The **QR Code Scanner** module for Odoo allows users to scan QR codes containing predefined data formats and automatically create records in the `res.partner` model. If a record already exists for the scanned QR code, an error message will be displayed.

## 🚀 Features
- Scan QR codes to create **res.partner** records.
- Prevents duplicate records by checking existing entries.
- Compatible with **Odoo 16+**.
- Simple and lightweight installation.

## 🛠 Installation Guide
### **Prerequisites**
Before installing the module, ensure you have:
- **Odoo installed** on your Windows machine.
- **Admin access** to the Odoo instance.

### **Step 1: Copy the Module to Odoo Addons Directory**
1. Locate the Odoo addons path by checking `odoo.conf` (usually in `C:\Program Files\Odoo\server\odoo.conf`).
2. Copy the `qr_code_scanner` module folder to the Odoo addons directory.

### **Step 2: Update Odoo Configuration (Optional)**
If you are using a custom module path, edit `odoo.conf` and add your module path:
```ini
addons_path = C:\Program Files\Odoo\server\addons,C:\path\to\your\qr_code_scanner
```

### **Step 3: Restart Odoo Server**
Open a terminal (Command Prompt) and restart Odoo with:
```sh
odoo-bin --addons-path="C:\Program Files\Odoo\server\addons,C:\path\to\your\qr_code_scanner" --db-filter=your_db_name
```

### **Step 4: Install the Module in Odoo**
1. Log in to Odoo.
2. Go to **Apps**.
3. Click **Update Apps List** (top-right corner).
4. Search for **QR Code Scanner**.
5. Click **Install**.

## 🏗 Usage Guide
1. Navigate to **Contacts > Customers**.
2. Click the **QR Scanner** feature (if configured in views).
3. Scan a QR code using your webcam or barcode scanner.
4. If the scanned QR code contains valid data, a new **res.partner** record will be created.
5. If a record with the same QR code already exists, an error message will be displayed.

## 🔧 Troubleshooting
- **Module not showing in Apps?**
  - Ensure the module is inside the correct `addons` path.
  - Click **Update Apps List** and search again.
- **QR Code not scanning?**
  - Check if the webcam or scanner is properly configured.
  - Test the QR scanner with a sample QR code.

