import tkinter as tk
import tkinter.filedialog as filedialog
import webbrowser
import requests

class AntivirusScannerGUI:
    def __init__(self, master):
        self.master = master
        master.title("Antivirus Scanner")

        self.label = tk.Label(master, text="Select a file to scan:")
        self.label.pack()

        self.select_button = tk.Button(master, text="Select file", command=self.select_file)
        self.select_button.pack()

        self.scan_button = tk.Button(master, text="Scan file", state='disabled', command=self.scan_file)
        self.scan_button.pack()

        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

        self.file_path = ''
        self.resource = ''

    def select_file(self):
        self.file_path = filedialog.askopenfilename()
        if self.file_path:
            self.scan_button.config(state='normal')

    def scan_file(self):
        url = 'https://www.virustotal.com/vtapi/v2/file/scan'
        params = {'apikey': 'YOUR_API_KEY'}

        with open(self.file_path, 'rb') as f:
            files = {'file': (self.file_path, f)}
            response = requests.post(url, files=files, params=params)

            if response.status_code == 200:
                self.resource = response.json()['resource']
                report_url = f"https://www.virustotal.com/gui/file/{self.resource}/detection"
                self.result_label.config(text=f"File uploaded to VirusTotal for scanning. Click on the link below to view the scan results:\n{report_url}")
                self.result_label.bind("<Button-1>", self.open_report_page)
            elif response.status_code == 204:
                self.result_label.config(text="Scan rate limit exceeded. Please try again later.")
            else:
                self.result_label.config(text=f"Scan failed with status code {response.status_code}.")

    def open_report_page(self, event):
        if self.resource:
            report_url = f"https://www.virustotal.com/gui/file/{self.resource}/detection"
            webbrowser.open(report_url)

if __name__ == '__main__':
    root = tk.Tk()
    app = AntivirusScannerGUI(root)
    root.mainloop()
