import math
import tkinter as tk
from tkinter import ttk, messagebox
import re

class KalkulatorKeuangan:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Kalkulator Keuangan")
        self.root.geometry("600x500")
        self.setup_ui()
    
    def setup_ui(self):
        # Membuat notebook (tab)
        self.notebook = ttk.Notebook(self.root)
        
        # Membuat tab
        self.tab_anuitas = ttk.Frame(self.notebook)
        self.tab_kpr = ttk.Frame(self.notebook)
        self.tab_pensiun = ttk.Frame(self.notebook)
        self.tab_waktu_lipat = ttk.Frame(self.notebook)
        self.tab_logaritma = ttk.Frame(self.notebook)
        self.tab_notasi_ilmiah = ttk.Frame(self.notebook)
        
        # Menambahkan tab ke notebook
        self.notebook.add(self.tab_anuitas, text="Kalkulator Anuitas")
        self.notebook.add(self.tab_kpr, text="Kalkulator KPR")
        self.notebook.add(self.tab_pensiun, text="Kalkulator Pensiun")
        self.notebook.add(self.tab_waktu_lipat, text="Waktu Pelipatgandaan")
        self.notebook.add(self.tab_logaritma, text="Persamaan Logaritma")
        self.notebook.add(self.tab_notasi_ilmiah, text="Notasi Ilmiah")
        
        self.notebook.pack(expand=True, fill='both', padx=10, pady=10)
        
        # Setup setiap tab
        self.setup_tab_anuitas()
        self.setup_tab_kpr()
        self.setup_tab_pensiun()
        self.setup_tab_waktu_lipat()
        self.setup_tab_logaritma()
        self.setup_tab_notasi_ilmiah()
        
        # Area output
        self.frame_output = ttk.Frame(self.root)
        self.frame_output.pack(fill='x', padx=10, pady=5)
        
        self.teks_output = tk.Text(self.frame_output, height=4, width=70)
        self.gulir_output = ttk.Scrollbar(self.frame_output, orient='vertical', command=self.teks_output.yview)
        self.teks_output.configure(yscrollcommand=self.gulir_output.set)
        
        self.teks_output.pack(side='left', fill='both', expand=True)
        self.gulir_output.pack(side='right', fill='y')
    
    def setup_tab_anuitas(self):
        # Widget Kalkulator Anuitas
        ttk.Label(self.tab_anuitas, text="Kalkulator Anuitas", font=('Arial', 12, 'bold')).pack(pady=10)
        
        # Input PV
        frame_pv = ttk.Frame(self.tab_anuitas)
        frame_pv.pack(fill='x', padx=20, pady=5)
        ttk.Label(frame_pv, text="Nilai Sekarang (PV):").pack(side='left')
        self.var_pv = tk.StringVar(value="0")
        self.entry_pv = ttk.Entry(frame_pv, textvariable=self.var_pv, width=15)
        self.entry_pv.pack(side='right')
        
        # Input PMT
        frame_pmt = ttk.Frame(self.tab_anuitas)
        frame_pmt.pack(fill='x', padx=20, pady=5)
        ttk.Label(frame_pmt, text="Pembayaran Berkala (PMT):").pack(side='left')
        self.var_pmt = tk.StringVar(value="0")
        self.entry_pmt = ttk.Entry(frame_pmt, textvariable=self.var_pmt, width=15)
        self.entry_pmt.pack(side='right')
        
        # Input Suku Bunga
        frame_bunga = ttk.Frame(self.tab_anuitas)
        frame_bunga.pack(fill='x', padx=20, pady=5)
        ttk.Label(frame_bunga, text="Suku Bunga (%):").pack(side='left')
        self.var_bunga = tk.StringVar(value="5")
        self.entry_bunga = ttk.Entry(frame_bunga, textvariable=self.var_bunga, width=15)
        self.entry_bunga.pack(side='right')
        
        # Input Periode
        frame_periode = ttk.Frame(self.tab_anuitas)
        frame_periode.pack(fill='x', padx=20, pady=5)
        ttk.Label(frame_periode, text="Periode (bulan):").pack(side='left')
        self.var_periode = tk.StringVar(value="12")
        self.entry_periode = ttk.Entry(frame_periode, textvariable=self.var_periode, width=15)
        self.entry_periode.pack(side='right')
        
        # Dropdown Pemajemukan
        frame_pemajemukan = ttk.Frame(self.tab_anuitas)
        frame_pemajemukan.pack(fill='x', padx=20, pady=5)
        ttk.Label(frame_pemajemukan, text="Pemajemukan:").pack(side='left')
        self.var_pemajemukan = tk.StringVar(value="bulanan")
        self.combo_pemajemukan = ttk.Combobox(frame_pemajemukan, textvariable=self.var_pemajemukan, 
                                            values=['bulanan', 'kontinu'], width=12, state='readonly')
        self.combo_pemajemukan.pack(side='right')
        
        # Tombol hitung dan hasil
        ttk.Button(self.tab_anuitas, text="Hitung Nilai Masa Depan", command=self.hitung_nilai_masa_depan).pack(pady=10)
        
        self.var_hasil_fv = tk.StringVar(value="Nilai Masa Depan: Rp0,00")
        ttk.Label(self.tab_anuitas, textvariable=self.var_hasil_fv, font=('Arial', 10)).pack(pady=5)
    
    def setup_tab_kpr(self):
        ttk.Label(self.tab_kpr, text="Kalkulator KPR", font=('Arial', 12, 'bold')).pack(pady=10)
        
        # Input Pokok Pinjaman
        frame_pokok = ttk.Frame(self.tab_kpr)
        frame_pokok.pack(fill='x', padx=20, pady=5)
        ttk.Label(frame_pokok, text="Jumlah Pinjaman:").pack(side='left')
        self.var_pokok = tk.StringVar(value="200000000")
        self.entry_pokok = ttk.Entry(frame_pokok, textvariable=self.var_pokok, width=15)
        self.entry_pokok.pack(side='right')
        
        # Input Suku Bunga
        frame_bunga_kpr = ttk.Frame(self.tab_kpr)
        frame_bunga_kpr.pack(fill='x', padx=20, pady=5)
        ttk.Label(frame_bunga_kpr, text="Suku Bunga (%):").pack(side='left')
        self.var_bunga_kpr = tk.StringVar(value="4.5")
        self.entry_bunga_kpr = ttk.Entry(frame_bunga_kpr, textvariable=self.var_bunga_kpr, width=15)
        self.entry_bunga_kpr.pack(side='right')
        
        # Input Jangka Waktu
        frame_jangka = ttk.Frame(self.tab_kpr)
        frame_jangka.pack(fill='x', padx=20, pady=5)
        ttk.Label(frame_jangka, text="Tahun:").pack(side='left')
        self.var_jangka = tk.StringVar(value="30")
        self.entry_jangka = ttk.Entry(frame_jangka, textvariable=self.var_jangka, width=15)
        self.entry_jangka.pack(side='right')
        
        # Tombol hitung dan hasil
        ttk.Button(self.tab_kpr, text="Hitung Angsuran", command=self.hitung_kpr).pack(pady=10)
        
        self.var_hasil_angsuran = tk.StringVar(value="Angsuran Bulanan: Rp0,00")
        ttk.Label(self.tab_kpr, textvariable=self.var_hasil_angsuran, font=('Arial', 10)).pack(pady=5)
    
    def setup_tab_pensiun(self):
        ttk.Label(self.tab_pensiun, text="Kalkulator Pensiun", font=('Arial', 12, 'bold')).pack(pady=10)
        
        # Investasi Awal
        frame_investasi_awal = ttk.Frame(self.tab_pensiun)
        frame_investasi_awal.pack(fill='x', padx=20, pady=5)
        ttk.Label(frame_investasi_awal, text="Investasi Awal:").pack(side='left')
        self.var_investasi_awal = tk.StringVar(value="10000000")
        self.entry_investasi_awal = ttk.Entry(frame_investasi_awal, textvariable=self.var_investasi_awal, width=15)
        self.entry_investasi_awal.pack(side='right')
        
        # Kontribusi Bulanan
        frame_kontribusi = ttk.Frame(self.tab_pensiun)
        frame_kontribusi.pack(fill='x', padx=20, pady=5)
        ttk.Label(frame_kontribusi, text="Kontribusi Bulanan:").pack(side='left')
        self.var_kontribusi = tk.StringVar(value="500000")
        self.entry_kontribusi = ttk.Entry(frame_kontribusi, textvariable=self.var_kontribusi, width=15)
        self.entry_kontribusi.pack(side='right')
        
        # Input Tingkat Pengembalian
        frame_imbal_hasil = ttk.Frame(self.tab_pensiun)
        frame_imbal_hasil.pack(fill='x', padx=20, pady=5)
        ttk.Label(frame_imbal_hasil, text="Tingkat Pengembalian (%):").pack(side='left')
        self.var_imbal_hasil = tk.StringVar(value="7")
        self.entry_imbal_hasil = ttk.Entry(frame_imbal_hasil, textvariable=self.var_imbal_hasil, width=15)
        self.entry_imbal_hasil.pack(side='right')
        
        # Input Tahun
        frame_tahun_pensiun = ttk.Frame(self.tab_pensiun)
        frame_tahun_pensiun.pack(fill='x', padx=20, pady=5)
        ttk.Label(frame_tahun_pensiun, text="Tahun:").pack(side='left')
        self.var_tahun_pensiun = tk.StringVar(value="30")
        self.entry_tahun_pensiun = ttk.Entry(frame_tahun_pensiun, textvariable=self.var_tahun_pensiun, width=15)
        self.entry_tahun_pensiun.pack(side='right')
        
        # Tombol hitung dan hasil
        ttk.Button(self.tab_pensiun, text="Hitung Saldo", command=self.hitung_pensiun).pack(pady=10)
        
        self.var_saldo_pensiun = tk.StringVar(value="Saldo Masa Depan: Rp0,00")
        ttk.Label(self.tab_pensiun, textvariable=self.var_saldo_pensiun, font=('Arial', 10)).pack(pady=5)
    
    def setup_tab_waktu_lipat(self):
        ttk.Label(self.tab_waktu_lipat, text="Kalkulator Waktu Pelipatgandaan", font=('Arial', 12, 'bold')).pack(pady=10)
        
        # Input Suku Bunga
        frame_bunga_lipat = ttk.Frame(self.tab_waktu_lipat)
        frame_bunga_lipat.pack(fill='x', padx=20, pady=20)
        ttk.Label(frame_bunga_lipat, text="Suku Bunga (%):").pack(side='left')
        self.var_bunga_lipat = tk.StringVar(value="7")
        self.entry_bunga_lipat = ttk.Entry(frame_bunga_lipat, textvariable=self.var_bunga_lipat, width=15)
        self.entry_bunga_lipat.pack(side='right')
        
        # Tombol hitung dan hasil
        ttk.Button(self.tab_waktu_lipat, text="Hitung", command=self.hitung_waktu_lipat).pack(pady=10)
        
        self.var_hasil_waktu_lipat = tk.StringVar(value="Waktu untuk Melipatgandakan: 0 tahun")
        ttk.Label(self.tab_waktu_lipat, textvariable=self.var_hasil_waktu_lipat, font=('Arial', 10)).pack(pady=5)
    
    def setup_tab_logaritma(self):
        ttk.Label(self.tab_logaritma, text="Pemecah Persamaan Logaritma", font=('Arial', 12, 'bold')).pack(pady=10)
        
        # Input Basis
        frame_basis = ttk.Frame(self.tab_logaritma)
        frame_basis.pack(fill='x', padx=20, pady=5)
        ttk.Label(frame_basis, text="Basis:").pack(side='left')
        self.var_basis_log = tk.StringVar(value="10")
        self.entry_basis_log = ttk.Entry(frame_basis, textvariable=self.var_basis_log, width=15)
        self.entry_basis_log.pack(side='right')
        
        # Input Argumen
        frame_argumen = ttk.Frame(self.tab_logaritma)
        frame_argumen.pack(fill='x', padx=20, pady=5)
        ttk.Label(frame_argumen, text="Argumen:").pack(side='left')
        self.var_argumen_log = tk.StringVar(value="100")
        self.entry_argumen_log = ttk.Entry(frame_argumen, textvariable=self.var_argumen_log, width=15)
        self.entry_argumen_log.pack(side='right')
        
        # Tombol hitung dan hasil
        ttk.Button(self.tab_logaritma, text="Hitung", command=self.hitung_logaritma).pack(pady=10)
        
        self.var_hasil_log = tk.StringVar(value="Hasil: 0")
        ttk.Label(self.tab_logaritma, textvariable=self.var_hasil_log, font=('Arial', 10)).pack(pady=5)
    
    def setup_tab_notasi_ilmiah(self):
        ttk.Label(self.tab_notasi_ilmiah, text="Konverter Notasi Ilmiah", font=('Arial', 12, 'bold')).pack(pady=10)
        
        # Input Angka Standar
        frame_standar = ttk.Frame(self.tab_notasi_ilmiah)
        frame_standar.pack(fill='x', padx=20, pady=10)
        ttk.Label(frame_standar, text="Angka Standar:").pack(side='left')
        self.var_angka_standar = tk.StringVar(value="12345")
        self.entry_angka_standar = ttk.Entry(frame_standar, textvariable=self.var_angka_standar, width=20)
        self.entry_angka_standar.pack(side='right')
        
        # Frame tombol
        frame_tombol = ttk.Frame(self.tab_notasi_ilmiah)
        frame_tombol.pack(fill='x', padx=20, pady=10)
        ttk.Button(frame_tombol, text="→ Notasi Ilmiah", command=self.ke_notasi_ilmiah).pack(side='left', padx=10)
        ttk.Button(frame_tombol, text="← Angka Standar", command=self.dari_notasi_ilmiah).pack(side='right', padx=10)
        
        # Input Notasi Ilmiah
        frame_ilmiah = ttk.Frame(self.tab_notasi_ilmiah)
        frame_ilmiah.pack(fill='x', padx=20, pady=10)
        ttk.Label(frame_ilmiah, text="Notasi Ilmiah:").pack(side='left')
        self.var_notasi_ilmiah = tk.StringVar()
        self.entry_notasi_ilmiah = ttk.Entry(frame_ilmiah, textvariable=self.var_notasi_ilmiah, width=20)
        self.entry_notasi_ilmiah.pack(side='right')
    
    def catat_output(self, pesan):
        """Method pembantu untuk mencatat pesan ke area output"""
        self.teks_output.insert('end', pesan + '\n')
        self.teks_output.see('end')
    
    def bersihkan_output(self):
        """Membersihkan area output"""
        self.teks_output.delete('1.0', 'end')
    
    def hitung_nilai_masa_depan(self):
        try:
            pv = float(self.var_pv.get())
            pmt = float(self.var_pmt.get())
            bunga = float(self.var_bunga.get()) / 100
            n = int(self.var_periode.get())
            pemajemukan = self.var_pemajemukan.get()

            if pemajemukan == "bulanan":
                r = bunga / 12
                fv = pv * (1 + r)**n + pmt * ((1 + r)**n - 1) / r
            else:  # kontinu
                fv = pv * math.exp(bunga * n/12) + pmt * (math.exp(bunga * n/12) - 1) / (math.exp(bunga/12) - 1)

            self.var_hasil_fv.set(f'Nilai Masa Depan: Rp{fv:,.2f}')
            self.catat_output(f"Nilai masa depan anuitas dihitung: Rp{fv:,.2f}")
            
        except Exception as e:
            messagebox.showerror("Error", f"Kesalahan menghitung nilai masa depan: {str(e)}")
    
    def hitung_kpr(self):
        try:
            P = float(self.var_pokok.get())
            r = float(self.var_bunga_kpr.get()) / 100 / 12
            n = int(self.var_jangka.get()) * 12

            if r == 0:  # Menangani kasus bunga 0%
                angsuran_bulanan = P / n
            else:
                angsuran_bulanan = P * (r * (1 + r)**n) / ((1 + r)**n - 1)

            self.var_hasil_angsuran.set(f'Angsuran Bulanan: Rp{angsuran_bulanan:,.2f}')
            self.catat_output(f"Angsuran KPR dihitung: Rp{angsuran_bulanan:,.2f}")
            
        except Exception as e:
            messagebox.showerror("Error", f"Kesalahan menghitung KPR: {str(e)}")
    
    def hitung_pensiun(self):
        try:
            P = float(self.var_investasi_awal.get())
            C = float(self.var_kontribusi.get())
            r = float(self.var_imbal_hasil.get()) / 100 / 12
            n = int(self.var_tahun_pensiun.get()) * 12

            if r == 0:  # Menangani kasus bunga 0%
                FV = P + C * n
            else:
                FV = P * (1 + r)**n + C * ((1 + r)**n - 1) / r

            self.var_saldo_pensiun.set(f'Saldo Masa Depan: Rp{FV:,.2f}')
            self.catat_output(f"Saldo pensiun dihitung: Rp{FV:,.2f}")
            
        except Exception as e:
            messagebox.showerror("Error", f"Kesalahan menghitung saldo pensiun: {str(e)}")
    
    def hitung_waktu_lipat(self):
        try:
            bunga = float(self.var_bunga_lipat.get()) / 100
            if bunga <= 0:
                messagebox.showwarning("Peringatan", "Suku bunga harus positif")
                return

            # Aturan 72 sebagai pendekatan
            waktu = 72 / (bunga * 100)
            self.var_hasil_waktu_lipat.set(f'Waktu untuk Melipatgandakan: {waktu:.2f} tahun')
            self.catat_output(f"Waktu pelipatgandaan dihitung: {waktu:.2f} tahun dengan suku bunga {bunga*100}%")
            
        except Exception as e:
            messagebox.showerror("Error", f"Kesalahan menghitung waktu pelipatgandaan: {str(e)}")
    
    def hitung_logaritma(self):
        try:
            basis = float(self.var_basis_log.get())
            argumen = float(self.var_argumen_log.get())

            if basis <= 0 or basis == 1:
                messagebox.showwarning("Peringatan", "Basis harus positif dan tidak sama dengan 1")
                return
            if argumen <= 0:
                messagebox.showwarning("Peringatan", "Argumen harus positif")
                return

            hasil = math.log(argumen, basis)
            self.var_hasil_log.set(f'Hasil: {hasil:.4f}')
            self.catat_output(f"Log basis {basis} dari {argumen} = {hasil:.4f}")
            
        except Exception as e:
            messagebox.showerror("Error", f"Kesalahan menghitung logaritma: {str(e)}")
    
    def ke_notasi_ilmiah(self):
        try:
            angka = float(self.var_angka_standar.get())
            notasi_ilmiah = f"{angka:.4e}"
            self.var_notasi_ilmiah.set(notasi_ilmiah)
            self.catat_output(f"Mengkonversi {angka} ke notasi ilmiah: {notasi_ilmiah}")
        except ValueError:
            messagebox.showerror("Error", "Masukkan angka yang valid")
    
    def dari_notasi_ilmiah(self):
        try:
            # Menangani notasi ilmiah (misalnya, 1.23e4 atau 1.23E4)
            notasi_ilmiah = self.var_notasi_ilmiah.get().lower().replace('×10^', 'e').replace('·10^', 'e')
            angka = float(notasi_ilmiah)
            self.var_angka_standar.set(f"{angka:,}")
            self.catat_output(f"Mengkonversi {notasi_ilmiah} ke notasi standar: {angka:,}")
        except ValueError:
            messagebox.showerror("Error", "Masukkan notasi ilmiah yang valid (misalnya, 1.23e4)")
    
    def jalankan(self):
        self.root.mainloop()

# Menjalankan kalkulator
if __name__ == "__main__":
    print("💰 Kalkulator Keuangan")
    print("=========================================")
    print("Kalkulator keuangan komprehensif dengan berbagai alat:")
    print("• Kalkulator Anuitas")
    print("• Kalkulator KPR")
    print("• Kalkulator Pensiun")
    print("• Kalkulator Waktu Pelipatgandaan")
    print("• Pemecah Persamaan Logaritma")
    print("• Konverter Notasi Ilmiah")
    print()
    
    kalkulator = KalkulatorKeuangan()
    kalkulator.jalankan()