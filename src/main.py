import math
import tkinter as tk
from tkinter import ttk, messagebox
import re

class FinancialCalculator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Financial Calculator")
        self.root.geometry("600x500")
        self.setup_ui()
    
    def setup_ui(self):
        # Create notebook (tabs)
        self.notebook = ttk.Notebook(self.root)
        
        # Create tabs
        self.annuity_tab = ttk.Frame(self.notebook)
        self.mortgage_tab = ttk.Frame(self.notebook)
        self.retirement_tab = ttk.Frame(self.notebook)
        self.doubling_time_tab = ttk.Frame(self.notebook)
        self.logarithmic_tab = ttk.Frame(self.notebook)
        self.scientific_notation_tab = ttk.Frame(self.notebook)
        
        # Add tabs to notebook
        self.notebook.add(self.annuity_tab, text="Annuity Calculator")
        self.notebook.add(self.mortgage_tab, text="Mortgage Calculator")
        self.notebook.add(self.retirement_tab, text="Retirement Calculator")
        self.notebook.add(self.doubling_time_tab, text="Doubling Time")
        self.notebook.add(self.logarithmic_tab, text="Logarithmic Equations")
        self.notebook.add(self.scientific_notation_tab, text="Scientific Notation")
        
        self.notebook.pack(expand=True, fill='both', padx=10, pady=10)
        
        # Setup each tab
        self.setup_annuity_tab()
        self.setup_mortgage_tab()
        self.setup_retirement_tab()
        self.setup_doubling_time_tab()
        self.setup_logarithmic_tab()
        self.setup_scientific_notation_tab()
        
        # Output area
        self.output_frame = ttk.Frame(self.root)
        self.output_frame.pack(fill='x', padx=10, pady=5)
        
        self.output_text = tk.Text(self.output_frame, height=4, width=70)
        self.output_scroll = ttk.Scrollbar(self.output_frame, orient='vertical', command=self.output_text.yview)
        self.output_text.configure(yscrollcommand=self.output_scroll.set)
        
        self.output_text.pack(side='left', fill='both', expand=True)
        self.output_scroll.pack(side='right', fill='y')
    
    def setup_annuity_tab(self):
        # Annuity Calculator widgets
        ttk.Label(self.annuity_tab, text="Annuity Calculator", font=('Arial', 12, 'bold')).pack(pady=10)
        
        # PV input
        pv_frame = ttk.Frame(self.annuity_tab)
        pv_frame.pack(fill='x', padx=20, pady=5)
        ttk.Label(pv_frame, text="PV:").pack(side='left')
        self.pv_var = tk.StringVar(value="0")
        self.pv_entry = ttk.Entry(pv_frame, textvariable=self.pv_var, width=15)
        self.pv_entry.pack(side='right')
        
        # PMT input
        pmt_frame = ttk.Frame(self.annuity_tab)
        pmt_frame.pack(fill='x', padx=20, pady=5)
        ttk.Label(pmt_frame, text="PMT:").pack(side='left')
        self.pmt_var = tk.StringVar(value="0")
        self.pmt_entry = ttk.Entry(pmt_frame, textvariable=self.pmt_var, width=15)
        self.pmt_entry.pack(side='right')
        
        # Rate input
        rate_frame = ttk.Frame(self.annuity_tab)
        rate_frame.pack(fill='x', padx=20, pady=5)
        ttk.Label(rate_frame, text="Rate (%):").pack(side='left')
        self.rate_var = tk.StringVar(value="5")
        self.rate_entry = ttk.Entry(rate_frame, textvariable=self.rate_var, width=15)
        self.rate_entry.pack(side='right')
        
        # Periods input
        periods_frame = ttk.Frame(self.annuity_tab)
        periods_frame.pack(fill='x', padx=20, pady=5)
        ttk.Label(periods_frame, text="Periods:").pack(side='left')
        self.periods_var = tk.StringVar(value="12")
        self.periods_entry = ttk.Entry(periods_frame, textvariable=self.periods_var, width=15)
        self.periods_entry.pack(side='right')
        
        # Compounding dropdown
        compounding_frame = ttk.Frame(self.annuity_tab)
        compounding_frame.pack(fill='x', padx=20, pady=5)
        ttk.Label(compounding_frame, text="Compounding:").pack(side='left')
        self.compounding_var = tk.StringVar(value="monthly")
        self.compounding_combo = ttk.Combobox(compounding_frame, textvariable=self.compounding_var, 
                                            values=['monthly', 'continuous'], width=12, state='readonly')
        self.compounding_combo.pack(side='right')
        
        # Calculate button and result
        ttk.Button(self.annuity_tab, text="Calculate FV", command=self.calculate_fv).pack(pady=10)
        
        self.fv_result_var = tk.StringVar(value="Future Value: $0.00")
        ttk.Label(self.annuity_tab, textvariable=self.fv_result_var, font=('Arial', 10)).pack(pady=5)
    
    def setup_mortgage_tab(self):
        ttk.Label(self.mortgage_tab, text="Mortgage Calculator", font=('Arial', 12, 'bold')).pack(pady=10)
        
        # Principal input
        principal_frame = ttk.Frame(self.mortgage_tab)
        principal_frame.pack(fill='x', padx=20, pady=5)
        ttk.Label(principal_frame, text="Loan Amount:").pack(side='left')
        self.principal_var = tk.StringVar(value="200000")
        self.principal_entry = ttk.Entry(principal_frame, textvariable=self.principal_var, width=15)
        self.principal_entry.pack(side='right')
        
        # Rate input
        mortgage_rate_frame = ttk.Frame(self.mortgage_tab)
        mortgage_rate_frame.pack(fill='x', padx=20, pady=5)
        ttk.Label(mortgage_rate_frame, text="Rate (%):").pack(side='left')
        self.mortgage_rate_var = tk.StringVar(value="4.5")
        self.mortgage_rate_entry = ttk.Entry(mortgage_rate_frame, textvariable=self.mortgage_rate_var, width=15)
        self.mortgage_rate_entry.pack(side='right')
        
        # Loan term input
        loan_term_frame = ttk.Frame(self.mortgage_tab)
        loan_term_frame.pack(fill='x', padx=20, pady=5)
        ttk.Label(loan_term_frame, text="Years:").pack(side='left')
        self.loan_term_var = tk.StringVar(value="30")
        self.loan_term_entry = ttk.Entry(loan_term_frame, textvariable=self.loan_term_var, width=15)
        self.loan_term_entry.pack(side='right')
        
        # Calculate button and result
        ttk.Button(self.mortgage_tab, text="Calculate Payment", command=self.calculate_mortgage).pack(pady=10)
        
        self.payment_result_var = tk.StringVar(value="Monthly Payment: $0.00")
        ttk.Label(self.mortgage_tab, textvariable=self.payment_result_var, font=('Arial', 10)).pack(pady=5)
    
    def setup_retirement_tab(self):
        ttk.Label(self.retirement_tab, text="Retirement Calculator", font=('Arial', 12, 'bold')).pack(pady=10)
        
        # Initial investment
        initial_frame = ttk.Frame(self.retirement_tab)
        initial_frame.pack(fill='x', padx=20, pady=5)
        ttk.Label(initial_frame, text="Initial Investment:").pack(side='left')
        self.initial_investment_var = tk.StringVar(value="10000")
        self.initial_investment_entry = ttk.Entry(initial_frame, textvariable=self.initial_investment_var, width=15)
        self.initial_investment_entry.pack(side='right')
        
        # Monthly contribution
        monthly_frame = ttk.Frame(self.retirement_tab)
        monthly_frame.pack(fill='x', padx=20, pady=5)
        ttk.Label(monthly_frame, text="Monthly Contribution:").pack(side='left')
        self.monthly_contribution_var = tk.StringVar(value="500")
        self.monthly_contribution_entry = ttk.Entry(monthly_frame, textvariable=self.monthly_contribution_var, width=15)
        self.monthly_contribution_entry.pack(side='right')
        
        # Rate input
        retirement_rate_frame = ttk.Frame(self.retirement_tab)
        retirement_rate_frame.pack(fill='x', padx=20, pady=5)
        ttk.Label(retirement_rate_frame, text="Return (%):").pack(side='left')
        self.retirement_rate_var = tk.StringVar(value="7")
        self.retirement_rate_entry = ttk.Entry(retirement_rate_frame, textvariable=self.retirement_rate_var, width=15)
        self.retirement_rate_entry.pack(side='right')
        
        # Years input
        years_frame = ttk.Frame(self.retirement_tab)
        years_frame.pack(fill='x', padx=20, pady=5)
        ttk.Label(years_frame, text="Years:").pack(side='left')
        self.retirement_years_var = tk.StringVar(value="30")
        self.retirement_years_entry = ttk.Entry(years_frame, textvariable=self.retirement_years_var, width=15)
        self.retirement_years_entry.pack(side='right')
        
        # Calculate button and result
        ttk.Button(self.retirement_tab, text="Calculate Balance", command=self.calculate_retirement).pack(pady=10)
        
        self.retirement_balance_var = tk.StringVar(value="Future Balance: $0.00")
        ttk.Label(self.retirement_tab, textvariable=self.retirement_balance_var, font=('Arial', 10)).pack(pady=5)
    
    def setup_doubling_time_tab(self):
        ttk.Label(self.doubling_time_tab, text="Doubling Time Calculator", font=('Arial', 12, 'bold')).pack(pady=10)
        
        # Rate input
        rate_frame = ttk.Frame(self.doubling_time_tab)
        rate_frame.pack(fill='x', padx=20, pady=20)
        ttk.Label(rate_frame, text="Rate (%):").pack(side='left')
        self.doubling_rate_var = tk.StringVar(value="7")
        self.doubling_rate_entry = ttk.Entry(rate_frame, textvariable=self.doubling_rate_var, width=15)
        self.doubling_rate_entry.pack(side='right')
        
        # Calculate button and result
        ttk.Button(self.doubling_time_tab, text="Calculate", command=self.calculate_doubling_time).pack(pady=10)
        
        self.doubling_time_result_var = tk.StringVar(value="Time to Double: 0 years")
        ttk.Label(self.doubling_time_tab, textvariable=self.doubling_time_result_var, font=('Arial', 10)).pack(pady=5)
    
    def setup_logarithmic_tab(self):
        ttk.Label(self.logarithmic_tab, text="Logarithmic Equation Solver", font=('Arial', 12, 'bold')).pack(pady=10)
        
        # Base input
        base_frame = ttk.Frame(self.logarithmic_tab)
        base_frame.pack(fill='x', padx=20, pady=5)
        ttk.Label(base_frame, text="Base:").pack(side='left')
        self.log_base_var = tk.StringVar(value="10")
        self.log_base_entry = ttk.Entry(base_frame, textvariable=self.log_base_var, width=15)
        self.log_base_entry.pack(side='right')
        
        # Argument input
        argument_frame = ttk.Frame(self.logarithmic_tab)
        argument_frame.pack(fill='x', padx=20, pady=5)
        ttk.Label(argument_frame, text="Argument:").pack(side='left')
        self.log_argument_var = tk.StringVar(value="100")
        self.log_argument_entry = ttk.Entry(argument_frame, textvariable=self.log_argument_var, width=15)
        self.log_argument_entry.pack(side='right')
        
        # Calculate button and result
        ttk.Button(self.logarithmic_tab, text="Calculate", command=self.calculate_logarithm).pack(pady=10)
        
        self.log_result_var = tk.StringVar(value="Result: 0")
        ttk.Label(self.logarithmic_tab, textvariable=self.log_result_var, font=('Arial', 10)).pack(pady=5)
    
    def setup_scientific_notation_tab(self):
        ttk.Label(self.scientific_notation_tab, text="Scientific Notation Converter", font=('Arial', 12, 'bold')).pack(pady=10)
        
        # Standard number input
        standard_frame = ttk.Frame(self.scientific_notation_tab)
        standard_frame.pack(fill='x', padx=20, pady=10)
        ttk.Label(standard_frame, text="Standard Number:").pack(side='left')
        self.standard_number_var = tk.StringVar(value="12345")
        self.standard_number_entry = ttk.Entry(standard_frame, textvariable=self.standard_number_var, width=20)
        self.standard_number_entry.pack(side='right')
        
        # Buttons frame
        buttons_frame = ttk.Frame(self.scientific_notation_tab)
        buttons_frame.pack(fill='x', padx=20, pady=10)
        ttk.Button(buttons_frame, text="→ Scientific", command=self.to_scientific).pack(side='left', padx=10)
        ttk.Button(buttons_frame, text="← Standard", command=self.from_scientific).pack(side='right', padx=10)
        
        # Scientific notation input
        scientific_frame = ttk.Frame(self.scientific_notation_tab)
        scientific_frame.pack(fill='x', padx=20, pady=10)
        ttk.Label(scientific_frame, text="Scientific Notation:").pack(side='left')
        self.scientific_number_var = tk.StringVar()
        self.scientific_number_entry = ttk.Entry(scientific_frame, textvariable=self.scientific_number_var, width=20)
        self.scientific_number_entry.pack(side='right')
    
    def log_output(self, message):
        """Helper method to log messages to output area"""
        self.output_text.insert('end', message + '\n')
        self.output_text.see('end')
    
    def clear_output(self):
        """Clear output area"""
        self.output_text.delete('1.0', 'end')
    
    def calculate_fv(self):
        try:
            pv = float(self.pv_var.get())
            pmt = float(self.pmt_var.get())
            rate = float(self.rate_var.get()) / 100
            n = int(self.periods_var.get())
            compounding = self.compounding_var.get()

            if compounding == "monthly":
                r = rate / 12
                fv = pv * (1 + r)**n + pmt * ((1 + r)**n - 1) / r
            else:  # continuous
                fv = pv * math.exp(rate * n/12) + pmt * (math.exp(rate * n/12) - 1) / (math.exp(rate/12) - 1)

            self.fv_result_var.set(f'Future Value: ${fv:,.2f}')
            self.log_output(f"Annuity FV calculated: ${fv:,.2f}")
            
        except Exception as e:
            messagebox.showerror("Error", f"Error calculating future value: {str(e)}")
    
    def calculate_mortgage(self):
        try:
            P = float(self.principal_var.get())
            r = float(self.mortgage_rate_var.get()) / 100 / 12
            n = int(self.loan_term_var.get()) * 12

            if r == 0:  # Handle 0% interest case
                monthly_payment = P / n
            else:
                monthly_payment = P * (r * (1 + r)**n) / ((1 + r)**n - 1)

            self.payment_result_var.set(f'Monthly Payment: ${monthly_payment:,.2f}')
            self.log_output(f"Mortgage payment calculated: ${monthly_payment:,.2f}")
            
        except Exception as e:
            messagebox.showerror("Error", f"Error calculating mortgage: {str(e)}")
    
    def calculate_retirement(self):
        try:
            P = float(self.initial_investment_var.get())
            C = float(self.monthly_contribution_var.get())
            r = float(self.retirement_rate_var.get()) / 100 / 12
            n = int(self.retirement_years_var.get()) * 12

            if r == 0:  # Handle 0% interest case
                FV = P + C * n
            else:
                FV = P * (1 + r)**n + C * ((1 + r)**n - 1) / r

            self.retirement_balance_var.set(f'Future Balance: ${FV:,.2f}')
            self.log_output(f"Retirement balance calculated: ${FV:,.2f}")
            
        except Exception as e:
            messagebox.showerror("Error", f"Error calculating retirement balance: {str(e)}")
    
    def calculate_doubling_time(self):
        try:
            rate = float(self.doubling_rate_var.get()) / 100
            if rate <= 0:
                messagebox.showwarning("Warning", "Rate must be positive")
                return

            # Rule of 72 approximation
            time = 72 / (rate * 100)
            self.doubling_time_result_var.set(f'Time to Double: {time:.2f} years')
            self.log_output(f"Doubling time calculated: {time:.2f} years at {rate*100}% rate")
            
        except Exception as e:
            messagebox.showerror("Error", f"Error calculating doubling time: {str(e)}")
    
    def calculate_logarithm(self):
        try:
            base = float(self.log_base_var.get())
            argument = float(self.log_argument_var.get())

            if base <= 0 or base == 1:
                messagebox.showwarning("Warning", "Base must be positive and not equal to 1")
                return
            if argument <= 0:
                messagebox.showwarning("Warning", "Argument must be positive")
                return

            result = math.log(argument, base)
            self.log_result_var.set(f'Result: {result:.4f}')
            self.log_output(f"Log base {base} of {argument} = {result:.4f}")
            
        except Exception as e:
            messagebox.showerror("Error", f"Error calculating logarithm: {str(e)}")
    
    def to_scientific(self):
        try:
            number = float(self.standard_number_var.get())
            scientific = f"{number:.4e}"
            self.scientific_number_var.set(scientific)
            self.log_output(f"Converted {number} to scientific notation: {scientific}")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number")
    
    def from_scientific(self):
        try:
            # Handle scientific notation (e.g., 1.23e4 or 1.23E4)
            sci_num = self.scientific_number_var.get().lower().replace('×10^', 'e').replace('·10^', 'e')
            number = float(sci_num)
            self.standard_number_var.set(f"{number:,}")
            self.log_output(f"Converted {sci_num} to standard notation: {number:,}")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid scientific notation (e.g., 1.23e4)")
    
    def run(self):
        self.root.mainloop()

# Run the calculator
if __name__ == "__main__":
    print("💰 Financial Calculator")
    print("=========================================")
    print("A comprehensive financial calculator with multiple tools:")
    print("• Annuity Calculator")
    print("• Mortgage Calculator")
    print("• Retirement Calculator")
    print("• Doubling Time Calculator")
    print("• Logarithmic Equation Solver")
    print("• Scientific Notation Converter")
    print()
    
    calculator = FinancialCalculator()
    calculator.run()