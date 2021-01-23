.\venv\Scripts\Activate.ps1

Remove-Item C:\Users\Betacom\Desktop\Example\migration_tool\diff.xlsx

echo "C:\Users\Betacom\Desktop\Example\migration_tool\B2B3
C:\Users\Betacom\Desktop\Example\migration_tool\SEE3
ORF

" | python main.py

$Excel = New-Object -ComObject Excel.Application
#l'apertura automatica dell'excel funziona togliendo il timestamp nel save del metodo make_excel di excel.py
$Workbook = $Excel.Workbooks.Open("C:\Users\Betacom\Desktop\Example\migration_tool\diff.xlsx")

$Excel.Visible = $true


