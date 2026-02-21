# Save this as run.ps1
Clear-Host

$Title = "Automated Candid Conversation"
$Width = $Title.Length + 10
$Line = "*" * $Width

Write-Host $Line -ForegroundColor Cyan
Write-Host "* $Title    *" -ForegroundColor Yellow
Write-Host $Line -ForegroundColor Cyan
Write-Host ""

# Executes the python script
python ./main.py
