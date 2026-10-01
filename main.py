import tkinter as tk
from tkinter import messagebox
import qrcode
from PIL import ImageTk

class QRGeration(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Генератор QR-кодов")
        self.resizable(False, False)
        self.configure(bg="#f4f4f4")

        self.entry = tk.Entry(self, width=40, font=("Helvetica", 14))
        self.entry.pack(pady=(20, 10), padx=20)

        self.paste_button = tk.Button(
            self,
            text="Вставить",
            font=("Helvetica", 11),
            command=self.paste_from_clipboard
        )
        self.paste_button.pack(pady=5)

        self.button = tk.Button(self, text="Сгенерировать", font=("Helvetica", 12, "bold"),
                                bg="#2e86de", fg="white", command=self.generate)
        self.button.pack(pady=10)
    
    # Место, где будет отображаться QR-код
       
        self.image_label = tk.Label(self, bg="#f4f4f4")
        self.image_label.pack(pady=20)
    
        self.qr_image = None

    def paste_from_clipboard(self):
        try:
            text = self.clipboard_get()
            self.entry.delete(0, tk.END)
            self.entry.insert(0,text)
        except tk.TclError:
            messagebox.showwarning("Ошибка", "Буфер обмена пуст")
    

    def generate(self):
        text = self.entry.get().strip()
        if not text:
            messagebox.showwarning("Ошибка", "Введите текст или ссылку")
            return

        qr = qrcode.QRCode(box_size=8, border=4)
        qr.add_data(text)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")

        self.qr_image = ImageTk.PhotoImage(img)
        self.image_label.configure(image=self.qr_image)

if __name__ == "__main__":
    QRGeration().mainloop()