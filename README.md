# QR code
This is a QR code generator and scanner using the WebCam, that we made to check the attendees to an event at our university .
It has this functionalities implemented : 
- Generates QR codes starting from given data .
- Sends personalized emails using the SMTP protocol with the QRcode as attachement .
- Scans the QR  code and search for it's owner in the database and validate its attendance . 
- Generates a sheet with the attendees list and the time in which they arrived .



## Dependecies 
- OpenCV . 
- NumPy .
- pandas .
- tkinter .
- pyzbar .
- pygame (only if u want to play the "checked sound") .
