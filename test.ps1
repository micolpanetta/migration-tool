.\venv\Scripts\Activate.ps1

Remove-Item C:\Users\Betacom\Desktop\Example\migration_tool\diff.xlsx

echo "C:\Users\Betacom\Desktop\Example\migration_tool\dist\B2B
C:\Users\Betacom\Desktop\Example\migration_tool\dist\SEE

" | python main.py

$Excel = New-Object -ComObject Excel.Application
$Workbook = $Excel.Workbooks.Open("C:\Users\Betacom\Desktop\Example\migration_tool\diff.xlsx")

$Excel.Visible = $true


